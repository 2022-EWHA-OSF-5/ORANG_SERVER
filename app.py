from flask import Flask, current_app
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'users'
    id = db.db.Column(db.db.Integer, primary_key=True, unique=True, autoincrement=True)
    username = db.db.Column(db.db.String(50), unique=True)
    password = db.db.Column(db.db.String(120))

    Reviews = db.relationship('Review', backref='user', lazy=True)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(50))
    image = db.Column(db.String(200))
    address = db.Column(db.String(200))
    category = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    description = db.Column(db.String(200))
    homepage = db.Column(db.String(200))
    score = db.Column(db.Float)
    review_count = db.Column(db.Integer)

    Menus = db.relationship('Menu', backref='restaurant', lazy=True)
    Reviews = db.relationship('Review', backref='restaurant', lazy=True)

    def __repr__(self):
        return '<Restaurant %r>' % (self.name)

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    image = db.Column(db.String(200))
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return '<Menu %r>' % (self.name)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    content = db.Column(db.String())
    score = db.Column(db.Integer)
    image = db.Column(db.String(200))

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Review %r>' % (self.content)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)