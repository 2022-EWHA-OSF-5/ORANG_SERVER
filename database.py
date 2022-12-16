import sqlite3

try:
    conn = sqlite3.connect("db.sqlite")
    cur = conn.cursor()

    user_list = [
        (1, 'doyeon', '0000'),
        (2, 'hyojin', '0000'),
        (3, 'dayoon', '0000'),
        (4, 'sooyoung', '0000'),
        (5, 'seojin', '0000'),
        ]
        
    cur.executemany("INSERT INTO users VALUES(?,?,?);", user_list)
   
    restaurant_list = [
        (1, '까이식당', 'static/image/restaurant/rst1.JPG', '정문', '서울특별시 서대문구 이화여대2가길 24 1층', '아시아', '07077798899', '치킨라이스를 전문으로 하는 동남아 음식점입니다. 일 100인분만 조리 및 한정 판매합니다.', 'https://Instagram.com/bistrogai', '5', '1'), 
        (2, '포포나무', 'static/image/restaurant/rst2.JPG', '정문', '서울특별시 서대문구 이화여대2가길 24', '한식', '023634552', '호텔 주방장 출신의 요리사가 선보이는 저렴하고 맛있는 스테이크!', ' ', '5', '1'),
        (3, '돈천동식당', 'static/image/restaurant/rst3.JPG', '정문', '서울특별시 서대문구 이화여대길 52-35 2층', '일식', '01077348321', '이대역 근처, 맛있으면서 저렴한 돈천동식당! 김치나베돈까스', ' ', '4', '1'),
        (4, '소녀방앗간', 'static/image/restaurant/rst4.JPG', '정문', '서울특별시 서대문구 대현동 34-19 1층', '한식', '050714450603', '소녀방앗간은 땅과 공기가 줄 수 있는 에너지를 온전히 담은 재료로 수준 높은 식문화를 전합니다.', 'http://www.millcompany.co.kr/', '5', '1'), 
        (5, '비아37', 'static/image/restaurant/rst5.JPG', '정문', '서울특별시 서대문구 대현동 37-36', '양식', '050713630900', '이대 안의 작은 유럽을 경험할 수 있는 감성 이탈리안 레스토랑 비아37, 좋은 사람과 최고의 이탈리안을 느껴보세요.', 'https://blog.naver.com/coffeekyum', '0', '0'), 
        (6, '모미지식당', 'static/image/restaurant/rst6.JPG', '정문', ' 서울특별시 서대문구 대현동 37-75 2층', '한식', '050713162029', '모미지식당 11월 메뉴 소고기 가지덮밥 9500원, 육회덮밥 11000원, 굴국밥 12000원', 'http://www.instagram.com/momiji_cook', '5', '1'),
        (7, '낭만식탁', 'static/image/restaurant/rst7.jpg', '정문', '서울특별시 서대문구 대현동 56-110', '일식', '023121238', '이대 스타벅스 맞은편 계단으로 내려오세요. 일요일은 쉬는 날입니다.', 'https://www.instagram.com/romantic_table01', '0', '0'),
        (8, '딸기골', 'static/image/restaurant/rst8.jpg', '후문', '서울특별시 서대문구 연대동문길 29', '분식', '033635563', '이대에 위치한 딸기골 분식입니다. 생방송 금요와이드 40회 출연', ' ', '5', '0'),
        (9, '란주탕슉', 'static/image/restaurant/rst9.jpg', '정문', '서울특별시 서대문구 이화여대2가길 18', '중식', '050713249370', '국내산 등심만을 사용하는 꿔바로우에 매콤새콤달콤한 소스가 특징입니다. 모든 면은 직접 반죽하여 칼로 쳐내어 만드는 두툼한 도삭면으로 요리됩니다. 기본적으로 어린 아이들이 먹기에는 모두 매콤할 수 있으나 사천자장도삭면과 새우볶음밥은 아이들만을 위한 변경이 가능합니다.', ' ', '0', '0'),
        (10, '방콕익스프레스', 'static/image/restaurant/rst10.jpg', '신기역', '서울특별시 서대문구 연세로2길 91', '아시아', '0264017793', '신촌 방콕익스프레스 가성비 좋은 태국 음식 맛집', 'https://www.bangkokexp.com/', '0', '0'),
        (11, '아콘스톨', 'static/image/restaurant/rst11.jpg', '신기역', '서울특별시 서대문구 신촌역로 17 1층 110호', '분식', '023641301', '경의선 신촌기차역에서 2분, 이대 정문에서 5분 거리에 있는 도시락, 김밥 판매점입니다. 실내에 8석, 실외에 4석의 식사 장소도 있어요. 혼밥, 혼술, 포장 모두 가능해요. 즐거운 음악과 식사를 즐기러 오세요.', ' ', '0', '0'),
        (12, '고냉지', 'static/image/restaurant/rst12.jpg', '신기역', '서울특별시 서대문구 연세로2마길 30', '한식', '023130845', '이대 앞에 학생들이 많이 찾는 고냉지 김치찌개입니다. 입맛대로 골라 먹는 신개념 토핑 김치찌개로 돼지고기, 부대, 참치, 만두, 순두부 등 다양한 토핑을 고를 수 있습니다. 찌개 1인분에 토핑재료 1가지를 선택할 수 있으며 보쌈과 같이 먹는 고냉지 정식, 비빔밥과 함께 먹을 수 있는 비빔밥 정식이 있습니다.', '-', '0', '0'),
        (19, '리카', 'static/image/restaurant/rst19.jpg', '정문', '서울 서대문구 이화여대길 72-3 2층', '일식', '00000000000', '분위기 좋고 깔끔한 이자카야', '-', '0', '0'),
        (20, '전티마이', 'static/image/restaurant/rst20.jpg', '정문', '서울 서대문구 이화여대길 59 메르체쇼핑몰 3층', '아시아', '07082501235', '베트남 현지의 맛과 착한가격 4,500원, 그리고 보면 놀라는 넉넉한 양', '-', '0', '0'),
        (21, '스탠바이키친', 'static/image/restaurant/rst21.jpeg', '후문', '서울 서대문구 연대동문길 49', '양식', '023656353', '연대 외국어학당과 외국인 기숙사가 가까워 외국 친구들이 많이 이용하는 샌드위치 맛집!', '-', '0', '0'),
        (22, '아웃닭', 'static/image/restaurant/rst22.jpg', '정문', '서울 서대문구 이화여대5길 16', '양식', '023634375', '맛도 좋고 가성비도 좋은 이대 앞 치킨 호프집', 'http://www.outdark.co.kr/', '0', '0'),
        (23, '너스레', 'static/image/restaurant/rst23.jpeg', '정문', '서울 서대문구 이화여대7길 22', '한식', '023642221', '이대 레몬소주로 유명한 술집', '-', '0', '0'),
        (24, '원즈오운', 'static/image/restaurant/rst24.jpg', '정문', '서울 서대문구 이화여대길 20 1층', '양식', '023133190', '매일 굽는 빵과 신선한 재료로 풍부한 맛을 선물해드리고 싶어요. 맛있는 샌드위치, 커피 한 잔과 함께 원즈오운에서 편안하고 여유로운 나만의 시간을 보내다 가세요.', 'https://www.instagram.com/ones.own.bakery/?utm_medium=copy_link', '0', '0'),

        ]
    cur.executemany("INSERT INTO restaurants VALUES(?,?,?,?,?,?,?,?,?,?,?);", restaurant_list)
 
    menu_list = [
        (1, '치킨라이스(특)', '13000원', 'static/image/menu/menu1_2.JPG', 1), (2, '치킨라이스(보통)', '9000원', 'static/image/menu/menu1_1.JPG', 1), (3, '싱하맥주', '5000원', 'static/image/menu/menu1_3.JPG', 1), (4, '콜라', '2000원', 'static/image/menu/menu1_4.JPG', 1),
        (5, '떡갈비 스테이크+흑미밥', '9900원','static/image/menu/menu2_1.JPG',2), (6, '데리야끼 치킨 스테이크+흑미밥', '11900원', 'static/image/menu/menu2_2.JPG', 2), (7, '실크 스테이크+흑미밥', '9900원', 'static/image/menu/menu2_3.JPG', 2), (8, '샐러드', '9900원', 'static/image/menu/menu2_4.JPG', 2),
        (9, '카레 돈카츠', '8300원', 'static/image/menu/menu3_1.JPG', 3), (10, '가츠동', '7800원', 'static/image/menu/menu3_2.JPG', 3), (11, '김치나베', '7800원', 'static/image/menu/menu3_3.JPG', 3),
        (12, '산나물밥', '8800원', 'static/image/menu/menu4_1.JPG', 4), (13, '고춧가루제육볶음', '11800원', 'static/image/menu/menu4_2.JPG', 4), (14, '참명란비빔밥', '10800원', 'static/image/menu/menu4_3.JPG', 4),
        (15, '바질페스토 크림 뇨끼', '20000원', 'static/image/menu/menu5_1.JPG', 5), (16, '클래식 라자냐', '20000원', 'static/image/menu/menu5_2.JPG', 5), (17, '링귀니 스콜리오', '23000원', 'static/image/menu/menu5_3.JPG', 5),
        (18, '채끝 스테이크', '38000원', 'static/image/menu/menu5_4.JPG', 5), (19, '육회덮밥', '11000원', 'static/image/menu/menu6_1.JPG', 6), (20, '소고기가지덮밥', '9500원', 'static/image/menu/menu6_2.JPG', 6),
        (21, '굴국밥', '12000원', 'static/image/menu/menu6_3.JPG', 6), (22, '사케동', '12000원', 'static/image/menu/menu7_1.png', 7), (23, '간장새우', '10000원', 'static/image/menu/menu7_2.jpg', 7),
        (24, '치즈김치순두부', '5500원', 'static/image/menu/menu8_1.png', 8), (25, '부대찌개', '5500원', 'static/image/menu/menu8_2.png', 8), (26, '김치알밥', '5500원', 'static/image/menu/menu8_3.jpeg', 8), (27, '떡볶이', '3000원', 'static/image/menu/menu8_4.jpeg', 8),
        (28, '사천해물자장도삭면', '6000원', 'static/image/menu/menu9_1.jpg', 9), (29, '사천짬뽕도삭면', '9000원', 'static/image/menu/menu9_2.jpg', 9), (30, '사천꿔빠로우(R)', '17000원', 'static/image/menu/menu9_3.jpg', 9), (32, '사천탕수새우(R)', '2300원', 'static/image/menu/menu9_4.jpg', 9),
        (33, '뿌팟퐁 커리', '13500원', 'static/image/menu/menu10_1.jpg', 10), (34, '베트남 소고기 쌀국수', '7500원', 'static/image/menu/menu10_2.jpg', 10), (35, '새우팟타이', '7500원', 'static/image/menu/menu10_3.jpg', 10),
        (36, '순대떡볶음', '3900원', 'static/image/menu/menu11_1.jpg', 11), (37, '참치밥샌드', '4000원', 'static/image/menu/menu11_2.jpeg', 11), (38, '김밥', '3000원', 'static/image/menu/menu11_3.jpg', 11), 
        (39, '고냉지 정식', '14000원', 'static/image/menu/menu12_1.jpeg', 12), (40, '김치찌개+비빔밥', '8000원', 'static/image/menu/menu12_2.jpeg', 12), (41, '보쌈(소)', '25000원', 'static/image/menu/menu12_3.jpeg', 12), (42, '계란말이', '8000원', 'static/image/menu/menu12_4.jpg', 12),
        (60, '간장새우장', '16000원', 'static/image/menu/menu19_1.jpg', 19),
        (61, '새우덴뿌라', '18000원', 'static/image/menu/menu19_2.jpg', 19),
        (62, '고추치킨 가라아게', '18000원', 'static/image/menu/menu19_3.jpg', 19),
        (63, '소고기 쌀국수', '4900원', 'static/image/menu/menu20_1.jpg', 20),
        (64, '파인애플 볶음밥', '5500원', 'static/image/menu/menu20_2.JPG', 20),
        (65, '프리미엄 쌀국수', '5500원', 'static/image/menu/menu20_3.jpeg', 20),
        (66, '갈릭 쉬림프 아보카도', '9300원', 'static/image/menu/menu21_1.jpg', 21),
        (67, '필리 치즈 스테이크', '8800원', 'static/image/menu/menu21_2.jpg', 21),
        (68, '모짜렐라 토마토', '8300원', 'static/image/menu/menu21_3.jpg', 21),
        (69, '마틴 간장치킨', '19900원', 'static/image/menu/menu22_1.jpg', 22),
        (70, '튀김모둠', '15000원', 'static/image/menu/menu22_2.jpg', 22),
        (71, '봄베이 하이볼', '7800원', 'static/image/menu/menu22_3.jpg', 22),
        (72, '너스레전', '14000원', 'static/image/menu/menu23_1.jpg', 23),
        (73, '두부김치', '13000원', 'static/image/menu/menu23_2.jpg', 23),
        (74, '계란찜', '11000원', 'static/image/menu/menu23_3.jpg', 23),
        (75, '잠봉뵈르', '8900원', 'static/image/menu/menu24_1.jpg', 24),
        (76, '사과 콩포트 브리치즈 바게트', '8500원', 'static/image/menu/menu24_2.jpg', 24),
        (77, '초당옥수수 스프', '5000원', 'static/image/menu/menu24_3.jpg', 24)
        ]
    cur.executemany("INSERT INTO menus VALUES(?,?,?,?,?);", menu_list)
    
    review_list = [(1, '까이는 진짜 언제 먹어도 너무 맛있어요... 부드럽고 든든하고 짱입니당', '5', 'static/image/review/rv1.JPG', 1, 1), 
    (2, '고기 촉촉하고 치즈감자 고소하고 양도 많아요ㅎㅎ 계란국까지 최고의 한끼!!!', '5', 'static/image/review/rv2.JPG', 2, 1), (3, '저번보다 김치나베 국물 양이 조금 부족했어요.. 아쉽ㅠㅠ', '4', 'static/image/review/rv3.JPG', 3, 1), 
    (4, '자극적인 맛을 좋아하면 좀 싱겁게 느껴질 수도 있지만 나한텐 딱 맞았음~~ 반찬도 다양하고 맛도 괜찮고 깔끔!', '5', 'static/image/review/rv4.JPG', 4, 1),(5, '오랜만에 갔는데 여전히 맛있당 샐러드랑 파인애플도 있어서 더 좋음ㅎㅎ 다음엔 굴국밥 먹어봐야지', '5', 'static/image/review/rv5.JPG', 6, 1)]
    cur.executemany("INSERT INTO reviews VALUES (?,?,?,?,?,?);", review_list)

    bookmark_list = [(1, 1, 1),(2, 2, 1), (3, 3, 1) ]
    cur.executemany("INSERT INTO bookmarks VALUES (?,?,?);", bookmark_list)

    conn.commit()

finally:
    conn.close()