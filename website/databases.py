from . import db 

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    slug= db.Column(db.String(100), unique=True)

class Top_by_interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    slug= db.Column(db.String(100), unique=True)

class Top_by_fans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    slug= db.Column(db.String(100), unique=True)
    
class Latest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    slug= db.Column(db.String(100), unique=True)

class Phones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(100))
    brand_slug= db.Column(db.String(100))
    phone_name = db.Column(db.String(100))
    phone_slug= db.Column(db.String(100))
    image =db.Column(db.String(200))
    os =db.Column(db.String(200))

    
