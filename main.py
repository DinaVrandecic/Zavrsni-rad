from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

def fun():
    print("dina")
def fun():
    print("dina")
def fun():
    print("dina")

# from flask import Flask, render_template, url_for, redirect, request,jsonify
# import requests
# import random


# base_url = "https://phone-specs-api.azharimm.dev/"
# top_by_interest_endpoint = 'top-by-interest'
# top_by_fans_endpoint = 'top-by-fans'
# latest_endpoint = 'latest'
# search_endpoint= '/search?query='

# app = Flask(__name__)

# base = 'http://phone-specs-api.vercel.app/'
# def get_top(base,endpoint):
#         api_url = base + endpoint
#         response = requests.get(api_url)
#         data = response.json()
#         top_phones = data['data']
#         return top_phones

# @app.route("/home")
# def display_top_phones():
#     top_by_interest = get_top(base,'top-by-interest')['phones']
#     top_by_fans = get_top(base,'top-by-fans')['phones']
#     latest = get_top(base,'latest')['phones'][:10]
#     brands=get_top(base, '/brands')
#     brands = random.sample(brands, 5)
#     all_phones=top_by_fans + top_by_interest + latest
#     random_phones = random.sample(all_phones, 10)
#     pictures=[]
#     for i in random_phones:
#         pics =  get_top(i['detail'], '')['phone_images']
#         pictures.append(pics)
#     return render_template('base.html',brands=brands, pictures=pictures, top_by_interest = top_by_interest, top_by_fans= top_by_fans, latest = latest, enumerate=enumerate)

# @app.route("/brands")
# def brands():
#     all_brands = get_top(base,'brands')
#     return render_template("brands.html", brands=all_brands)

# @app.route("/brands/<brand_slug>")
# def phones(brand_slug):
#     brand_url = f'http://phone-specs-api.vercel.app/brands/{brand_slug}'
#     response = requests.get(brand_url)
#     data = response.json()
#     phones = data['data']['phones']
#     brand_name= data['data']['title']

#     brands=get_top(base, '/brands')
#     brands = random.sample(brands, 5)
#     return render_template('phones.html',brand_name=brand_name, phones=phones ,brands=brands)

# @app.route("/<phone_slug>")
# def specs( phone_slug):
#     brand_url = f'http://phone-specs-api.vercel.app/{phone_slug}'
#     response = requests.get(brand_url)
#     data = response.json()
#     specs = data['data']

#     brands=get_top(base, '/brands')
#     brands = random.sample(brands, 5)
#     return render_template("specs.html", phone=specs,brands=brands)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# import requests
# import psycopg2

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Buterica12@localhost/phone_db'
# db = SQLAlchemy(app)

# class Phone(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     brand = db.Column(db.String(100))

# @app.route('/')
# def index():
#     phones = Phone.query.all()
#     return render_template('index.html', phones=phones)

# @app.route('/fetch_data')
# def fetch_data():
#     api_url = 'http://phone-specs-api.vercel.app/brands'
#     response = requests.get(api_url)
#     data = response.json()

#     for brand in data['data']:
#         brand_name = brand['brand_name']

#         new_phone = Phone(brand=brand_name)
#         db.session.add(new_phone)
    
#     db.session.commit()
#     return 'Data fetched successfully and stored in the database.'

# if __name__ == '__main__':
#     app.run(debug=True)
