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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

