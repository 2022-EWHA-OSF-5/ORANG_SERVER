from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource 
from werkzeug.utils import secure_filename
import os
from models import *
import sqlite3


app = Flask(__name__)
api = Api(app) 

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db.init_app(app)
db.app = app
with app.app_context():
    db.create_all()

#메인 페이지
@api.route('/home')
class MainAPI(Resource):
    def get(self):
        reviews = Review.query.limit(5).all()
        restaurants = Restaurant.query.order_by(Restaurant.review_count.desc()).limit(5).all()
        
        return_data = {
            'message': '메인 페이지 조회 성공',
            'data': {
                'reviews' : [review.serialize() for review in reviews],
                'restaurants' : [restaurant.serialize() for restaurant in restaurants]
            }
        }
        return return_data

#회원가입
@api.route('/signup')
class Signup(Resource):
    def post(self): 
        data = request.get_json()
        user = User(username=data['username'], password=data['password'])

        try:
            db.session.add(user)
            db.session.commit()
            db.session.refresh(user)
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close() 

        user = User.query.filter(User.id == user.id).first()

        return_data = {
            'message': '유저 등록 성공',
            'data': user.serialize()
        }
        return return_data

#로그인
@api.route('/login')
class Login(Resource):
    def post(self): 
        data = request.get_json()
        user = User.query.filter(User.username == data['username'], User.password == data['password']).first()

        return_data = {
            'message': '유저 인증 성공',
            'data': user.serialize()
        }
        return return_data

#식당 등록
@api.route('/restaurants')
class RestaurantAPI(Resource):
    def post(self): 
        if request.files["image"]:
            image_file=request.files["image"] 
            image_path = "static/image/restaurant/{}".format(image_file.filename)
            image_file.save(image_path) 
        else:
            image_path=""

        data = request.form
        restaurant = Restaurant(name=data['name'], image=image_path, address=data['address'], category=data['category'], phone=data['phone'], description=data['description'], homepage=data['homepage'], score=0.0, review_count=0)
        try:
            db.session.add(restaurant)
            db.session.commit()
            db.session.refresh(restaurant)
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close() 

        restaurant = Restaurant.query.get(restaurant.id)

        return_data = {
            'message': '식당 등록 성공',
            'data': restaurant.serialize()
        }
        return return_data

#메뉴 등록
@api.route('/restaurants/<int:pk>/menus')
class MenuAPI(Resource):
    def post(self, pk): 
        if request.files["image"]:
            image_file=request.files["image"] 
            image_path = "static/image/menu/{}".format(image_file.filename)
            image_file.save(image_path) 
        else:
            image_path=""

        data = request.form
        menu = Menu(restaurant_id=pk, name=data['name'], price=data['price'], image=image_path)

        try:
            db.session.add(menu)
            db.session.commit()
            db.session.refresh(menu)
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close() 

        menu = Menu.query.get(menu.id)

        return_data = {
            'message': '메뉴 등록 성공',
            'data': menu.serialize()
        }
        return return_data

#리뷰 등록
@api.route('/restaurants/<int:pk>/reviews')
class ReviewAPI(Resource):
    def post(self, pk): 
        if request.files["image"]:
            image_file=request.files["image"] 
            image_path = "static/image/menu/{}".format(image_file.filename)
            image_file.save(image_path) 
        else:
            image_path=""

        data = request.form
        review = Review(restaurant_id=pk, user_id=data['user_id'], content=data['content'], score=data['score'], image=image_path)

        try:
            db.session.add(review)
            db.session.commit()
            db.session.refresh(review)
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close() 

        restaurant = Restaurant.query.get(pk)
        restaurant.review_count += 1
        restaurant.score = (restaurant.score*(restaurant.review_count-1)+review.score)/restaurant.review_count

        review = Review.query.get(review.id)

        return_data = {
            'message': '리뷰 등록 성공',
            'data': review.serialize()
        }
        return return_data

#내가 쓴 리뷰
@api.route('/mypage/review')
class MyReview(Resource):
    def get(self): 
        data = request.get_json()
        reviews = Review.query.filter(Review.user_id == data['user_id']).all()
        return_data = {
            'message': '작성한 리뷰 조회 성공',
            'data': [review.serialize() for review in reviews]
        }
        return return_data

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)