# -*- coding: utf-8 -*-
import sqlite3

try:
    conn = sqlite3.connect("db.sqlite")
    conn.text_factory = str
    cur = conn.cursor()
        
    # restaurant_list = [
    #     (25, '굿바이 슈가베어', 'static/image/restaurant/rst25.jpeg', '정문', '서울특별시 서대문구 이화여대길 72-6', '양식', '023931559', '건강하고 맛있는 무설탕 포케와 샐러드를 드실 수 있어요! Believe your own choice', 'http://www.instagram.com/goodbyesugarbear/', '0', '0'),
    #     (26, '화라라마라탕', 'static/image/restaurant/rst26.jpg', '정문', '서울특별시 서대문구 이화여대길 88-16', '중식', '023130158', '마라탕, 마라샹궈, 꿔바로우 맛집', '', '0', '0'),
    #     (27, '돈노코돈먹기', 'static/image/restaurant/rst27.jpeg', '신기역', '서울 서대문구 신촌역로 43 2층', '한식', '023929993', '신촌기차역 가성비 삼겹살집', '', '0', '0'),
    #     (28, '대치영지', 'static/image/restaurant/rst28.jpeg', '후문', '서울 서대문구 성산로 519', '한식', '0269514847', '이대 후문 한식 맛집', '', '0', '0'),
    #     (29, '로드샌드위치', 'static/image/restaurant/rst29.jpeg', '후문', '서울 서대문구 연대동문길 45 1층 로드샌드위치', '양식', '050714344554', '연대동문길에 위치한 로드샌드위치는 2010년에 오픈하여 지금까지 최고의 샌드위치를 만들기 위해 노력하는 고메 샌드위치 매장입니다.', 'http://www.lordsandwich.co.kr', '0', '0'),
    # ]
    # cur.executemany("INSERT INTO restaurants VALUES(?,?,?,?,?,?,?,?,?,?,?);", restaurant_list)

    menu_list = [
        (78, '선셋탱고(연어망고 포케&샐러드)', '11900d원', 'static/image/menu/menu25_1.jpeg', 25),
        (79, '로지클라우드(명란아보카도 포케&샐러드)', '8500원', 'static/image/menu/menu25_2.jpeg', 25),
        (80, '시머링왈츠(떡갈비 포케&샐러드)', '8500원', 'static/image/menu/menu25_3.jpeg', 25),
        (81, '꿔바로우', '11900원', 'static/image/menu/menu26_1.png', 26),
        (82, '마라탕', '1800원', 'static/image/menu/menu26_2.jpeg', 26),
        (83, '마라샹궈', '3000원', 'static/image/menu/menu26_3.jpeg', 26),
        (84, '냉동삼겹살', '7000원', 'static/image/menu/menu27_1.jpeg', 27),
        (85, '소금구이', '8000원', 'static/image/menu/menu27_2.jpeg', 27),
        (86, '생삼겹살', '10000원', 'static/image/menu/menu27_3.jpeg', 27),
        (87, '닭곰탕', '8500원', 'static/image/menu/menu28_1.jpeg', 28),
        (88, '제육비빔밥', '9000원', 'static/image/menu/menu28_2.jpeg', 28),
        (89, '닭개장', '9000원', 'static/image/menu/menu28_3.jpeg', 28),
        (90, '비엘티 샌드위치', '10000원', 'static/image/menu/menu29_1.jpeg', 29),
        (91, '살라미 샌드위치', '10000원', 'static/image/menu/menu29_2.jpeg', 29),
        (92, '에그머니 샌드위치', '10000원', 'static/image/menu/menu29_3.jpeg', 29),
    ]
    cur.executemany("INSERT INTO menus VALUES(?,?,?,?,?);", menu_list)
    conn.commit()

finally:
    conn.close()