from flask import Blueprint
from flask import render_template, url_for, redirect, request,jsonify
from .databases import Brand, Top_by_interest, Top_by_fans, Latest, Phones
from . import db
import requests
import random

views = Blueprint('views', __name__)

base_url = "https://phone-specs-api.azharimm.dev/"
top_by_interest_endpoint = 'top-by-interest'
top_by_fans_endpoint = 'top-by-fans'
latest_endpoint = 'latest'
search_endpoint= '/search?query='


base = 'http://phone-specs-api.vercel.app/'
def get_top(base,endpoint):
        api_url = base + endpoint
        response = requests.get(api_url)
        data = response.json()
        top_phones = data['data']
        return top_phones


def fetch_data():
    brands = get_top(base, 'brands')
    top_by_interest = get_top(base,'top-by-interest')['phones']
    top_by_fans = get_top(base,'top-by-fans')['phones']
    latest = get_top(base,'latest')['phones'][:10]

    for brand in brands:
        brand_name = brand['brand_name']
        brand_slug = brand['brand_slug']
        # phones = get_top(base, 'brands/' + brand_slug)['phones']
        phones_url = f'http://phone-specs-api.vercel.app/brands/{brand_slug}'
        response = requests.get(phones_url)
        phones_data = response.json()
        phones = phones_data['data']['phones']
        for phone in phones:
            name = phone['phone_name']
            phone_slug = phone['slug']
            # phone_data = get_top(base, phone_slug)
            # os = phone_data['os']

            existing_phone = Phones.query.filter_by(brand_name= brand_name, phone_name=name).first()
            if existing_phone == None:
                new_phone = Phones(brand_name=brand_name, brand_slug= brand_slug, phone_name=name, phone_slug=phone_slug)
                db.session.add(new_phone)

            

    for brand in brands:
        brand_name = brand['brand_name']
        brand_slug = brand['brand_slug']

        existing_phone = Brand.query.filter_by(name=brand_name).first()
        if existing_phone == None:
            new_phone = Brand(name=brand_name, slug=brand_slug)
            db.session.add(new_phone)


    for phone in top_by_interest:
        phone_name = phone['phone_name']
        phone_slug = phone['slug']

        existing_phone = Top_by_interest.query.filter_by(name=phone_name).first()
        if existing_phone == None:
            new_phone = Top_by_interest(name=phone_name, slug=phone_slug)
            db.session.add(new_phone)
    

    for phone in top_by_fans:
        phone_name = phone['phone_name']
        phone_slug = phone['slug']

        existing_phone = Top_by_fans.query.filter_by(name=phone_name).first()
        if existing_phone == None:
            new_phone = Top_by_fans(name=phone_name, slug=phone_slug)
            db.session.add(new_phone)


    for phone in latest:
        phone_name = phone['phone_name']
        phone_slug = phone['slug']

        existing_phone = Latest.query.filter_by(name=phone_name).first()
        if existing_phone == None:
            new_phone = Latest(name=phone_name, slug=phone_slug)
            db.session.add(new_phone)

    db.session.commit()
    return 'Data fetched successfully and stored in the database.'

# @views.route("/search", methods=['POST'])
# def search():


@views.route("/home", methods=['GET', 'POST'])
def display_top_phones():
    brands = Brand.query.order_by(db.func.random()).limit(10)
    top_by_fans = Top_by_fans.query.all()
    top_by_interest= Top_by_interest.query.all()
    latest = Latest.query.all()

    if request.method == 'POST':
        search_query = request.form.get('search')
        search_results = Phones.query.filter(Phones.phone_name.like(f'%{search_query}%')).first()
        return render_template('base.html', search_results=search_results, search_query=search_query,brands=brands,top_by_interest=top_by_interest, top_by_fans=top_by_fans, latest=latest, enumerate=enumerate)
    
    return render_template('base.html',brands=brands,top_by_interest=top_by_interest, top_by_fans=top_by_fans, latest=latest, enumerate=enumerate)

    # all_phones=Top_by_fans + Top_by_interest + Latest
    # random_phones = random.sample(all_phones, 10)
    # pictures=[]
    # for i in random_phones:
    #     pics =  get_top(i['detail'], '')['phone_images']
    #     pictures.append(pics)
   # return render_template('base.html',brands=brands,top_by_interest=top_by_interest, top_by_fans=top_by_fans, latest=latest, enumerate=enumerate)

@views.route("/brands")
def brands():
    brands = Brand.query.all()
    return render_template("brands.html", brands=brands)

@views.route("/brands/<brand_slug>")
def phones(brand_slug):
    brand_url = f'http://phone-specs-api.vercel.app/brands/{brand_slug}'
    response = requests.get(brand_url)
    data = response.json()
    phones = data['data']['phones']
    brand_name= data['data']['title']

    brands = Brand.query.order_by(db.func.random()).limit(10)

    return render_template('phones.html',brand_name=brand_name, phones=phones ,brands=brands)

# @views.route("/<phone_slug>")
# def specs( phone_slug):
#     brand_url = f'http://phone-specs-api.vercel.app/{phone_slug}'
#     response = requests.get(brand_url)
#     data = response.json()
#     specs = data['data']

#     brands=get_top(base, '/brands')
#     brands = random.sample(brands, 5)
#     return render_template("specs.html", phone=specs,brands=brands)