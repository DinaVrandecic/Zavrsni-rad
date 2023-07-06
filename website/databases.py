from . import db 

class Brand(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    slug= db.Column(db.String(100), unique=True)

class Top_by_interest(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    slug= db.Column(db.String(100), unique=True)

class Top_by_fans(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    slug= db.Column(db.String(100), unique=True)
    
class Latest(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    slug= db.Column(db.String(100), unique=True)

class Phones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(100))
    brand_slug= db.Column(db.String(100))
    phone_name = db.Column(db.String(100))
    phone_slug= db.Column(db.String(100))
    image =db.Column(db.String(200))

    
