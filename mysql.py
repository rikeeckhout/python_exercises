import pymysql
import pymysql.cursor
conn= pymysql.connect(host='localhost',user='user',password='user',db='testdb',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
a=conn.cursor()
sql='CREATE TABLE `users` (`id` int(11) NOT NULL AUTO_INCREMENT,`email` varchar(255) NOT NULL,`password` varchar(255) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;'
a.execute(sql)
