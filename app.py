from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource 
from werkzeug.utils import secure_filename
import os
from models import *
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app) 


basdir = os.path.abspath(os.path.dirname(__file__))
# basdir 경로안에 DB파일 만들기
dbfile = os.path.join(basdir, 'db.sqlite')

# 내가 사용 할 DB URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
# 비지니스 로직이 끝날때 Commit 실행(DB반영)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 수정사항에 대한 TRACK
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db.init_app(app)
db.app = app
with app.app_context():
    db.create_all()


#메인 페이지
@api.route('/home')
class Home(Resource):
    def get(self):
        reviews = Review.query.limit(5).all()
        restaurants = Restaurant.query.order_by(Restaurant.score.desc()).limit(5).all()

        return_data = {
            'message': '메인 페이지 조회 성공',
            'data': {
                'reviews': [review.serialize() for review in reviews],
                'restaurants': [restaurant.serialize() for restaurant in restaurants]
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
        restaurant = Restaurant(name=data['name'], image=image_path, location=data['location'], address=data['address'], category=data['category'], phone=data['phone'], description=data['description'], homepage=data['homepage'], score=0.0, review_count=0)
        try:
            db.session.add(restaurant)
            db.session.commit()
            db.session.refresh(restaurant)
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close() 

        restaurant = Restaurant.query.filter(Restaurant.id == restaurant.id).first()

        return_data = {
            'message': '식당 등록 성공',
            'data': restaurant.serialize()
        }
        return return_data

    #식당 조회
    def get(self):
        category = request.headers.get('category')

        if not category:
            restaurants = Restaurant.query.all()
        else:
            data = request.args.get('category')
            restaurants = Restaurant.query.filter(Restaurant.category == data['category']).all()

        return_data = {
                'message': '식당 리스트 조회 성공',
                'data': [restaurant.serialize() for restaurant in restaurants]
            }
            
        return return_data


#메뉴
@api.route('/restaurants/<int:pk>/menus')
class MenuAPI(Resource):
    #메뉴 등록
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

        menu = Menu.query.filter(Menu.id == menu.id).first()

        return_data = {
            'message': '메뉴 등록 성공',
            'data': menu.serialize()
        }
        return return_data

    #메뉴 조회
    def get(self, pk):
        restaurant_id = request.headers.get('Restaurant')
        print('헤더', restaurant_id)
        menus = Menu.query.filter(Menu.restaurant_id == restaurant_id, Menu.id <= 3).all()
        return_data = {
            'message': '맛집 세부 화면(메뉴) 조회 성공',
            'data': [menu.serialize() for menu in menus]
        }
        return return_data


#메뉴 전체 조회
@api.route('/restaurants/<int:primary_key>/menus/all')
class MenuDetailAPI(Resource):
    def get(self, pk):
        menus = Menu.query.filter(Menu.restaurant_id == pk).all()
        return_data = {
            'message': '맛집 세부 화면(메뉴 전체) 조회 성공',
            'data': [menu.serialize() for menu in menus]
        }
        return return_data


#리뷰
@api.route('/restaurants/<int:pk>/reviews')
class ReviewAPI(Resource):
    #리뷰 등록
    def post(self, pk): 
        if request.files["image"]:
            image_file=request.files["image"] 
            image_path = "static/image/menu/{}".format(image_file.filename)
            image_file.save(image_path) 
        else:
            image_path=""

        data = request.form
        review = Review(restaurant_id=pk, user_id=data['user_id'], content=data['content'], score=data['score'], image=image_path)
        
        restaurant = Restaurant.query.get(pk)
        restaurant.review_count += 1
        restaurant.score = (restaurant.score*(restaurant.review_count-1)+float(review.score))/restaurant.review_count

        try:
            db.session.add(review)
            db.session.commit()
            db.session.refresh(review)
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close() 

        review = Review.query.get(review.id)

        return_data = {
            'message': '리뷰 등록 성공',
            'data': review.serialize()
        }
        return return_data

    #리뷰 조회
    def get(self, pk):
        reviews = Review.query.filter(Review.restaurant_id == pk, Review.id <= 3).all()
        return_data = {
            'message': '맛집 세부 화면(리뷰) 조회 성공',
            'data': [review.serialize() for review in reviews]
        }
        return return_data


#리뷰 전체
@api.route('/restaurants/<int:primary_key>/reviews/all')
class ReviewDetailAPI(Resource):
    def get(self, pk):
        reviews = Review.query.filter(Review.restaurant_id == pk).all()
        return_data = {
            'message': '맛집 세부 화면(리뷰 전체) 조회 성공',
            'data': [review.serialize() for review in reviews]
        }
        return return_data


#내가 쓴 리뷰
@api.route('/mypage/reviews')
class MyReview(Resource):
    def get(self): 
        user_id = request.headers.get('User')
        #user_id = request.headers

        print('헤더',user_id)
        reviews = Review.query.filter(Review.user_id == user_id).all()
        return_data = {
            'message': '작성한 리뷰 조회 성공',
            'data': [review.serialize() for review in reviews]
        }

#내가 찜한 북마크
@api.route('/mypage/bookmarks')
class MyReview(Resource):
    def get(self): 
        user_id = request.headers.get('User')
        #user_id = request.headers

        print('헤더',user_id)
        bookmarks = Bookmark.query.filter(Bookmark.user_id == user_id).first()
        restaurants = Restaurant.query.filter(Restaurant.id == Bookmark.restaurant_id).all()
        return_data = {
            'message': '내가 찜한 북마크 조회 성공',
            'data': [restaurant.serialize() for restaurant in restaurants]
        }
        return return_data


#리스트 화면 (필터링 - 카테고리)
@api.route('/restaurants')
class ListAPI(Resource):
    def get(self):
        category = request.headers.get('category')

        if not category:
            restaurants = Restaurant.query.all()
        else:
            data = request.args.get('category')
            restaurants = Restaurant.query.filter(Restaurant.category == data['category']).all()

        return_data = {
                'message': '식당 리스트 조회 성공',
                'data': [restaurant.serialize() for restaurant in restaurants]
            }
            
        return return_data


#맛집 세부 화면 - 정보
@api.route('/restaurants/<int:primary_key>')
class DetailPageAPI(Resource):
    def get(self, primary_key):
        restaurant_id = request.headers.get('Restaurant')
        print('헤더', restaurant_id)
        restaurants = Restaurant.query.filter(Restaurant.id == restaurant_id).all()
        return_data = {
            'message': '맛집 세부 화면(정보) 조회 성공',
            'data': [restaurant.serialize() for restaurant in restaurants]
        }
        return return_data
    

#북마크 추가
@api.route('/restaurants/<int:primary_key>/bookmark')
class BookmarkAPI(Resource):
    def post(self, primary_key):
        data = request.json
        bookmark = Bookmark(restaurant_id=primary_key, user_id=data['user_id'])

        try:
            db.session.add(bookmark)
            db.session.commit()
            db.session.refresh(bookmark)
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

        return_data = {
            'message': '북마크 추가 성공'
        }

        return return_data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)