from flask import Flask, request, jsonify, session, abort
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from models import db
from flask_paginate import get_page_args
import sqlite3

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' 
app.config['JSON_AS_ASCII'] = False

#리스트 화면 (필터링 - 위치, 카테고리)
@api.route('/restaurant')
class restaurant_list(Resource):
    def get(self):
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        cur.execute('SELECT name, address, category, description, score, review_count FROM restaurants')
        return jsonify(cur.fetchall())

@api.route('/restaurant/<string:address>/')
class restaurant_list(Resource):
    def get(self, address):
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        cur.execute('SELECT name, address, category, description, score, review_count FROM restaurants WHERE address=address')
        return jsonify(cur.fetchall())

@api.route('/restaurant/<string:category>/')
class restaurant_list(Resource):
    def get(self, category):
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

#북마크 & 북마크 취소
@api.route('/restaurants/<int:restaurant_id>/bookmarks')
class bookmark(Resource):
    def post(self):
        return

#리뷰 등록 화면
@api.route('/restaurants/<int:restaurant_id>/reviews')
class review_register(Resource):
    def post(self, restaurant_id):
        if not session.get('logged_in'):
            abort(401)
        try:
            score = request.form['score']
            content = request.form['content']
            image = request.file['image']
            image.save(secure_filename(image.filename))
            with sqlite3.connect("db.sqlite") as conn:
                cur = conn.cursor()
                cur.execute('INSERT INTO reviews (score, content, image) VALUES (?,?,?)', (score, content, image))
                conn.commit()
        finally:
            conn.close()
            return
   
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)