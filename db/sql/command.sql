charset utf8mb4;
insert into users_genres values (1, 1, '日本食');
insert into users_genres values (2, 1, '洋食');
insert into users_genres values (3, 1, '中華');

insert into foods values (1, 1, '寿司', './food_img/sushi.jpg', 10, 5, 20, 5, 3);
insert into foods values (2, 1, '天ぷら', './food_img/tenpura.jpg', 30, 50, 20, 2, 2);
insert into foods values (3, 1, 'すき焼き', './food_img/sukiyaki.jpg', 50, 20, 20, 10, 5);
insert into foods values (4, 1, 'ラーメン', './food_img/ramen.jpg', 10, 40, 60, 10, 0);
insert into foods values (5, 2, 'ハンバーガー', './food_img/hamburger.jpg', 30, 20, 25, 30, 15);
insert into foods values (6, 2, 'ステーキ', './food_img/steak.jpg', 11, 73, 84, 100, 57);
insert into foods values (7, 2, 'パスタ', './food_img/spaghetti.jpg', 22, 24, 13, 53, 34);
insert into foods values (8, 2, 'ピザ', './food_img/pizza.jpg', 3, 58, 82, 27, 47);
insert into foods values (9, 3, '麻婆豆腐', './food_img/mabodoufu.jpg', 94, 95, 56, 11, 44);
insert into foods values (10, 3, '炒飯', './food_img/chahan.jpg', 75, 9, 24, 64, 70);
insert into foods values (11, 3, '肉まん', './food_img/nikuman.jpg', 44, 12, 84, 12, 36);

show variables like '%char%';