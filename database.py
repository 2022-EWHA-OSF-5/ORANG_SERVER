import sqlite3

try:
    conn = sqlite3.connect("db.sqlite")
    cur = conn.cursor()
   
    restaurant_list = [(1, '까이식당', 'static/image/restaurant/rst1.JPG', '정문', '서울특별시 서대문구 이화여대2가길 24 1층', '아시아음식', '07077798899', '치킨라이스를 전문으로 하는 동남아 음식점입니다. 일 100인분만 조리 및 한정 판매합니다.', 'https://Instagram.com/bistrogai', '5', '1'), 
    (2, '포포나무', 'static/image/restaurant/rst2.JPG', '정문', '서울특별시 서대문구 이화여대2가길 24', '한식', '023634552', '호텔 주방장 출신의 요리사가 선보이는 저렴하고 맛있는 스테이크!', ' ', '5', '1'),
     (3, '돈천동식당', 'static/image/restaurant/rst3.JPG', '정문', '서울특별시 서대문구 이화여대길 52-35 2층', '일식', '01077348321', '이대역 근처, 맛있으면서 저렴한 돈천동식당! 김치나베돈까스', ' ', '4', '1'),
      (4, '소녀방앗간', 'static/image/restaurant/rst4.JPG', '정문', '서울특별시 서대문구 대현동 34-19 1층', '한식', '050714450603', '소녀방앗간은 땅과 공기가 줄 수 있는 에너지를 온전히 담은 재료로 수준 높은 식문화를 전합니다.', 'http://www.millcompany.co.kr/', '5', '1'), 
      (5, '비아37', 'static/image/restaurant/rst5.JPG', '정문', '서울특별시 서대문구 대현동 37-36', '양식', '050713630900', '이대 안의 작은 유럽을 경험할 수 있는 감성 이탈리안 레스토랑 비아37, 좋은 사람과 최고의 이탈리안을 느껴보세요.', 'https://blog.naver.com/coffeekyum', '0', '0'), 
      (6, '모미지식당', 'static/image/restaurant/rst6.JPG', '정문', ' 서울특별시 서대문구 대현동 37-75 2층', '한식', '050713162029', '모미지식당 11월 메뉴 소고기 가지덮밥 9500원, 육회덮밥 11000원, 굴국밥 12000원', 'http://www.instagram.com/momiji_cook', '5', '1')]
    cur.executemany("INSERT INTO restaurants VALUES(?,?,?,?,?,?,?,?,?,?,?);", restaurant_list)
 
    menu_list = [(1, '치킨라이스(특)', '13000원', 'static/image/menu/menu1_2.JPG', 1), (2, '치킨라이스(보통)', '9000원', 'static/image/menu/menu1_1.JPG', 1), (3, '싱하맥주', '5000원', 'static/image/menu/menu1_3.JPG', 1), (4, '콜라', '2000원', 'static/image/menu/menu1_4.JPG', 1),
    (5, '떡갈비 스테이크+흑미밥', '9900원','static/image/menu/menu2_1.JPG',2), (6, '데리야끼 치킨 스테이크+흑미밥', '11900원', 'static/image/menu/menu2_2.JPG', 2), (7, '실크 스테이크+흑미밥', '9900원', 'static/image/menu/menu2_3.JPG', 2), (8, '샐러드', '9900원', 'static/image/menu/menu2_4.JPG', 2),
    (9, '카레 돈카츠', '8300원', 'static/image/menu/menu3_1.JPG', 3), (10, '가츠동', '7800원', 'static/image/menu/menu3_2.JPG', 3), (11, '김치나베', '7800원', 'static/image/menu/menu3_3.JPG', 3),
    (12, '산나물밥', '8800원', 'static/image/menu/menu4_1.JPG', 4), (13, '고춧가루제육볶음', '11800원', 'static/image/menu/menu4_2.JPG', 4), (14, '참명란비빔밥', '10800원', 'static/image/menu/menu4_3.JPG', 4),
    (15, '바질페스토 크림 뇨끼', '20000원', 'static/image/menu/menu5_1.JPG', 5), (16, '클래식 라자냐', '20000원', 'static/image/menu/menu5_2.JPG', 5), (17, '링귀니 스콜리오', '23000원', 'static/image/menu/menu5_3.JPG', 5),
    (18, '채끝 스테이크', '38000원', 'static/image/menu/menu5_4.JPG', 5), (19, '육회덮밥', '11000원', 'static/image/menu/menu6_1.JPG', 6), (20, '소고기가지덮밥', '9500원', 'static/image/menu/menu6_2.JPG', 6),
    (21, '굴국밥', '12000원', 'static/image/menu/menu6_3.JPG', 6)]
    cur.executemany("INSERT INTO menus VALUES(?,?,?,?,?);", menu_list)
    
    '''

    review_list = [(1, '까이는 진짜 언제 먹어도 너무 맛있어요... 부드럽고 든든하고 짱입니당', '5', 'static/image/review/rv1.JPG', 1, 1), 
    (2, '고기 촉촉하고 치즈감자 고소하고 양도 많아요ㅎㅎ 계란국까지 최고의 한끼!!!', '5', 'static/image/review/rv2.JPG', 2, 1), (3, '저번보다 김치나베 국물 양이 조금 부족했어요.. 아쉽ㅠㅠ', '4', 'static/image/review/rv3.JPG', 3, 1), 
    (4, '자극적인 맛을 좋아하면 좀 싱겁게 느껴질 수도 있지만 나한텐 딱 맞았음~~ 반찬도 다양하고 맛도 괜찮고 깔끔!', '5', 'static/image/review/rv4.JPG', 4, 1),(5, '오랜만에 갔는데 여전히 맛있당 샐러드랑 파인애플도 있어서 더 좋음ㅎㅎ 다음엔 굴국밥 먹어봐야지', '5', 'static/image/review/rv5.JPG', 6, 1)]
    cur.executemany("INSERT INTO reviews VALUES (?,?,?,?,?,?);", review_list)    '''

    bookmark_list = [(1, 1, 1),(2, 2, 1), (3, 3, 1) ]
    cur.executemany("INSERT INTO bookmarks VALUES (?,?,?);", bookmark_list)


    conn.commit()

finally:
    conn.close()