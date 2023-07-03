from flask import Blueprint
from flask import render_template, url_for, redirect, request,jsonify
from .databases import Brand, Top_by_interest, Top_by_fans, Latest, Phones
from sqlalchemy import func
from . import db
import requests
import random

views = Blueprint('views', __name__)

base = 'http://phone-specs-api.vercel.app/'
def get_top(base,endpoint):
        api_url = base + endpoint
        response = requests.get(api_url)
        data = response.json()
        top_phones = data['data']
        return top_phones


def create_Phones():
    brands = get_top(base, 'brands')

    for brand in brands:
        brand_name = brand['brand_name']
        brand_slug = brand['brand_slug']
        phones = get_top(base, 'brands/' + brand_slug)['phones']
        for phone in phones:
            name = phone['phone_name']
            phone_slug = phone['slug']
            image = phone['image']

            existing_phone = Phones.query.filter_by(brand_name= brand_name, phone_name=name).first()
            if existing_phone == None:
                new_phone = Phones(brand_name=brand_name, brand_slug= brand_slug, phone_name=name, phone_slug=phone_slug, image = image)
                db.session.add(new_phone)
    
    db.session.commit()
    return 'Data fetched successfully and stored in the database.'

# Ne radi jer ima previse zahtjeva oko 3100 a treba bit max 1000 za Vercel
# def add_img():
#     mobile = Phones.query.all()
#     for mob in mobile:
#         specifications = get_top(base, mob.phone_slug)
#         os = specifications['os']
#         mob.os = os

#     db.session.commit()

def fetch_data():
    brands = get_top(base, 'brands')
    top_by_interest = get_top(base,'top-by-interest')['phones']
    top_by_fans = get_top(base,'top-by-fans')['phones']
    latest = get_top(base,'latest')['phones'][:10]


    for brand in brands:
        brand_name = brand['brand_name']
        brand_slug = brand['brand_slug']

        existing_phone = Brand.query.filter_by(name=brand_name).first()
        if existing_phone == None:
            new_phone = Brand(name=brand_name, slug=brand_slug)
            db.session.add(new_phone)

    db.session.query(Top_by_interest).delete()
    for phone in top_by_interest:
        phone_name = phone['phone_name']
        phone_slug = phone['slug']

        existing_phone = Top_by_interest.query.filter_by(name=phone_name).first()
        if existing_phone == None:
            new_phone = Top_by_interest(name=phone_name, slug=phone_slug)
            db.session.add(new_phone)
    
    db.session.query(Top_by_fans).delete()
    for phone in top_by_fans:
        phone_name = phone['phone_name']
        phone_slug = phone['slug']

        existing_phone = Top_by_fans.query.filter_by(name=phone_name).first()
        if existing_phone == None:
            new_phone = Top_by_fans(name=phone_name, slug=phone_slug)
            db.session.add(new_phone)

    db.session.query(Latest).delete()
    for phone in latest:
        full_phone_name = phone['phone_name']
        phone_slug = phone['slug']
        image = phone['image']

        existing_phone = Latest.query.filter_by(name=phone_name).first()
        if existing_phone == None:
            new_phone = Latest(name=full_phone_name, slug=phone_slug)
            db.session.add(new_phone)
    
        phone_data = get_top(base, phone_slug)
        brand_name = phone_data['brand']
        phone_name=phone_data['phone_name']

        existing_phone = Phones.query.filter_by(brand_name= brand_name, phone_name=phone_name).first()
        brand_slug = Phones.query.filter_by(brand_name=brand_name).first()
        if existing_phone == None:
            new = Phones(brand_name=brand_name, brand_slug= brand_slug.brand_slug, phone_name=phone_name, phone_slug=phone_slug, image = image)
            db.session.add(new)
    db.session.commit()
    return 'Data fetched successfully and stored in the database.'


@views.route("/home", methods=['GET', 'POST'])
def display_top_phones():
    brands = Brand.query.order_by(db.func.random()).limit(10)
    random_phones = Phones.query.order_by(func.random()).limit(10).all()
    
    top_by_fans = Top_by_fans.query.all()
    top_by_interest= Top_by_interest.query.all()
    latest = Latest.query.all()

    if request.method == 'POST':
        search_query = request.form.get('search')
        search_results = Phones.query.filter(Phones.phone_name.like(f'%{search_query}%')).all()
        return render_template('index.html', search_results=search_results, search_query=search_query,brands=brands)
    
    return render_template('base.html',random_phones = random_phones, brands=brands,top_by_interest=top_by_interest, top_by_fans=top_by_fans, latest=latest, enumerate=enumerate)

@views.route("/brands")
def brands():
    brands = Brand.query.all()

    if request.method == 'POST':
        search_query = request.form.get('search')
        search_results = Phones.query.filter(Phones.phone_name.like(f'%{search_query}%')).all()
        return render_template('index.html', search_results=search_results, search_query=search_query,brands=brands)
    
    return render_template("brands.html", brands=brands)

@views.route("/brands/<brand_slug>")
def phones(brand_slug):
    phones = Phones.query.filter_by(brand_slug= brand_slug).all()
    brand_name = Phones.query.filter_by(brand_slug= brand_slug).first()
    brands = Brand.query.order_by(db.func.random()).limit(10)

    return render_template('phones.html',brand_name=brand_name, phones=phones ,brands=brands)

@views.route("/<phone_slug>")
def specs( phone_slug):
    brands = Brand.query.order_by(db.func.random()).limit(10)
    specs = get_top(base, phone_slug)

    return render_template("specs.html", phone=specs,brands=brands)