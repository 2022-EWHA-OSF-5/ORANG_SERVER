from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(120))

    Reviews = db.relationship('Review', backref='user', lazy=True)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username
        }

    def __repr__(self):
        return '<User %r>' % (self.username)

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    image = db.Column(db.String(200))
    location = db.Column(db.String(200))
    address = db.Column(db.String(200))
    category = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    description = db.Column(db.String(200))
    homepage = db.Column(db.String(200))
    score = db.Column(db.Float)
    review_count = db.Column(db.Integer)

    Menus = db.relationship('Menu', backref='restaurant', lazy=True)
    Reviews = db.relationship('Review', backref='restaurant', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'location': self.location,
            'address': self.address,
            'category': self.category,
            'phone': self.phone,
            'description': self.description,
            'homepage': self.homepage,
            'score': self.score,
            'review_count': self.review_count,
        }

    def __repr__(self):
        return '<Restaurant %r>' % (self.name)

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    image = db.Column(db.String(200))
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'image': self.image
        }

    def __repr__(self):
        return '<Menu %r>' % (self.name)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    score = db.Column(db.Integer)
    image = db.Column(db.String(200))

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serialize(self):
        restaurant = Restaurant.query.filter(Restaurant.id == self.restaurant_id).first()
        
        return {
            'id': self.id,
            'restaurant': restaurant.name,
            'content': self.content,
            'score': self.score,
            'image': self.image
        }

    def __repr__(self):
        return '<Review %r>' % (self.content)

class Bookmark(db.Model):
    __tablename__ = 'bookmarks'
    id = db.Column(db.Integer, primary_key=True)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    