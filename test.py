from flask import Flask, request, jsonify, session, abort, flash
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from models import db
import sqlite3

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' 
app.config['JSON_AS_ASCII'] = False

#리스트 화면 (필터링 - 카테고리)
@api.route('/restaurant')
class restaurant_list(Resource):
    def get(self):
        category = request.args.get("category", "all")
        if category=="all":
            conn = sqlite3.connect("db.sqlite")
            cur = conn.cursor()
            cur.execute('SELECT name, address, category, description, score, review_count FROM restaurants')
        else:
            conn = sqlite3.connect("db.sqlite")
            cur = conn.cursor()
            cur.execute('SELECT name, address, category, description, score, review_count FROM restaurants WHERE category=category')
        return jsonify(cur.fetchall())

#맛집 세부 화면 - 정보
@api.route('/restaurant/<int:primary_key>/')
class detail_page(Resource):
    def get(self, primary_key):
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        cur.execute('SELECT * FROM restaurants')
        return jsonify(cur.fetchall())


#맛집 세부 화면 - 메뉴
@api.route('/restaurant/<int:primary_key>/menu_detail')
class detail_menu(Resource):
    def get(self, primary_key):
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        cur.execute('SELECT * FROM menus')
        return jsonify(cur.fetchmany(size=3))

#맛집 세부 화면 - 메뉴 - 전체 메뉴 보기
@api.route('/restaurant/<int:primary_key>/menu_detail/all')
class detail_menu(Resource):
    def get(self, primary_key):
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        cur.execute('SELECT * FROM menus')
        return jsonify(cur.fetchall())

#맛집 세부 화면 - 리뷰
@api.route('/restaurant/<int:primary_key>/review_detail')
class detail_review(Resource):
    def get(self, primary_key):
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        cur.execute('SELECT * FROM reviews')
        return jsonify(cur.fetchmany(size=2))

#맛집 세부 화면 - 리뷰 - 전체 리뷰 보기
@api.route('/restaurant/<int:primary_key>/review_detail/all')
class detail_review(Resource):
    def get(self, primary_key):
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        cur.execute('SELECT * FROM reviews')
        return jsonify(cur.fetchall())


@api.route('/restaurant/<int:primary_key>/bookmark')
class bookmark(Resource):
    def post(self, primary_key):
        
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        cur.execute('INSERT INTO bookmarks ')


#리뷰 등록 화면
@api.route('/restaurants/<int:primary_key>/reviews')
class review_register(Resource):
    def post(self, primary_key):
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        try:
            score = request.form['score']
            content = request.form['content']
            image = request.form['image']
        #image.save(secure_filename(image.filename))
            review = {'score':score, 'content':content, 'image':image}
            cur.execute('INSERT INTO reviews (score, content, image) VALUES (?,?,?)', (score, content, image))
            conn.commit()
        finally:
            conn.close()
            return jsonify(review)
   
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)