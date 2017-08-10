create table stock(
    num int primary key auto_increment,
    date varchar(30),
    name varchar(20),
    price int,
    count int
);
insert into stock(date,name,price,count) values('2017-03-20','다음',84900,500);
insert into stock(date,name,price,count) values('2017-03-20','넥슨',1756,300);
insert into stock(date,name,price,count) values('2017-03-20','NC',292000,200);
insert into stock(date,name,price,count) values('2017-03-21','다음',86100,450);
insert into stock(date,name,price,count) values('2017-03-21','넥슨',1787,220);
insert into stock(date,name,price,count) values('2017-03-21','NC',295000,320);
commit;
