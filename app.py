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

        restaurant = Restaurant.query.filter(Restaurant.id == restaurant.id).first()

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

        menu = Menu.query.filter(Menu.id == menu.id).first()

        return_data = {
            'message': '메뉴 등록 성공',
            'data': menu.serialize()
        }
        return return_data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

