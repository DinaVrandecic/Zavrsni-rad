from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db= SQLAlchemy()
DB_NAME = "phones_data"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:Buterica12@localhost/{DB_NAME}'
    db.init_app(app)

    from .views import views, fetch_data

    app.register_blueprint(views, url_prefix='/')

    from .databases import Brand

    with app.app_context():
        db.create_all()
        # fetch_data()

    return app

def create_database(app):
    if not path('website/'+ DB_NAME):
        db.create_all(app=app)
        print('Created database!')