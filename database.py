import sqlite3

try:
    conn = sqlite3.connect("db.sqlite")
    cur = conn.cursor()


    user_list = [(1, 'kim', 'abc1'), (2, 'lee', 'xyz2'), (3, 'park', 'osp3'), (4, 'seo', 'ttt4')]
    cur.executemany("INSERT INTO users VALUES(?,?,?);", user_list)
   
    
    restaurant_list = [(1, '까이식당', 'static/image/restaurant/sample.jpeg', '정문', '서울특별시 서대문구 이화여대2가길 24 1층', '아시아음식', '07077798899', '치킨라이스를 전문으로 하는 동남아 음식점입니다. 일 100인분만 조리 및 한정 판매합니다.', 'https://Instagram.com/bistrogai', '4.6', '115'), 
    (2, '포포나무', 'static/image/restaurant/sample.jpeg', '정문', '서울특별시 서대문구 이화여대2가길 24', '한식', '023634552', '호텔 주방장 출신의 요리사가 선보이는 저렴하고 맛있는 스테이크!', ' ', '4.5', '278'),
     (3, '돈천동식당', 'static/image/restaurant/sample.jpeg', '정문', '서울특별시 서대문구 이화여대길 52-35 2층', '일식', '01077348321', '이대역 근처, 맛있으면서 저렴한 돈천동식당! 김치나베돈까스', ' ', '4.5', '285'),
      (4, '소녀방앗간', 'static/image/restaurant/sample.jpeg', '정문', '서울특별시 서대문구 대현동 34-19 1층', '한식', '050714450603', '소녀방앗간은 땅과 공기가 줄 수 있는 에너지를 온전히 담은 재료로 수준 높은 식문화를 전합니다.', 'http://www.millcompany.co.kr/', '4.4', '264'), 
      (5, '비아37', 'static/image/restaurant/sample.jpeg', '정문', '서울특별시 서대문구 대현동 37-36', '양식', '050713630900', '이대 안의 작은 유럽을 경험할 수 있는 감성 이탈리안 레스토랑 비아37, 좋은 사람과 최고의 이탈리안을 느껴보세요.', 'https://blog.naver.com/coffeekyum', '4.6', '522'), 
      (6, '모미지식당', 'static/image/restaurant/sample.jpeg', '정문', ' 서울특별시 서대문구 대현동 37-75 2층', '한식', '050713162029', '모미지식당 11월 메뉴 소고기 가지덮밥 9500원, 육회덮밥 11000원, 굴국밥 12000원', 'http://www.instagram.com/momiji_cook', '4.7', '337')]
    cur.executemany("INSERT INTO restaurants VALUES(?,?,?,?,?,?,?,?,?,?,?);", restaurant_list)
 
    menu_list = [(1, '치킨라이스(특)', '13000원', 'static/image/menu/sample.jpeg', 1), (2, '치킨라이스(보통)', '9000원', 'static/image/menu/sample.jpeg', 1), (3, '싱하맥주', '5000원', 'static/image/menu/sample.jpeg', 1), (4, '콜라', '2000원', 'static/image/menu/sample.jpeg', 1)]
    cur.executemany("INSERT INTO menus VALUES(?,?,?,?,?);", menu_list)
    
    review_list = [(1, '너무 맛있어요!', '5', 'static/image/review/sample.jpeg', 1, 1), (2, '최고입니당', '5', 'static/image/review/sample.jpeg', 1, 2), (3, '양이 조금 부족했어요', '4', 'static/image/review/sample.jpeg', 1, 3), (4, '까이 최고...', '5', 'static/image/review/sample.jpeg', 1, 4)]
    cur.executemany("INSERT INTO reviews VALUES (?,?,?,?,?,?);", review_list)

    conn.commit()

finally:
    conn.close()