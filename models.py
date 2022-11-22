from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(120))

    Reviews = relationship('Review', backref='user', lazy=True)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    image = Column(String(200))
    address = Column(String(200))
    category = Column(String(120))
    phone = Column(String(120))
    description = Column(String(200))
    homepage = Column(String(200))
    score = Column(Float)
    review_count = Column(Integer)

    Menus = relationship('Menu', backref='restaurant', lazy=True)
    Reviews = relationship('Review', backref='restaurant', lazy=True)

    def __repr__(self):
        return '<Restaurant %r>' % (self.name)

class Menu(Base):
    __tablename__ = 'menus'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    image = Column(String(200))
    
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return '<Menu %r>' % (self.name)

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    content = Column(String())
    score = Column(Integer)
    image = Column(String(200))

    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Review %r>' % (self.content)
