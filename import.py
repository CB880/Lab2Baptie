import psycopg2

conn = psycopg2.connect(database="dl3ljeqivof4h",
						user='ugxkzsmzkjbeeg', password='5b1c427f10839729222de1527cc5604ad404e505c05d7a04a5fa23c168ee62e6',
						host='ec2-35-175-68-90.compute-1.amazonaws.com', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()


sql = '''CREATE TABLE DETAILS(employee_id int NOT NULL,\
employee_name char(20),\
employee_email varchar(30), employee_salary float);'''

#cursor.execute(sql)

#sql2 = '''COPY Books(isbn,title,author,year)
#FROM 'books.csv'
#DELIMITER ','
#CSV HEADER;'''

with open('books.csv', 'r') as f:
    next(f)
    cursor.copy_from(f, "Books", sep=',')

#cursor.execute(sql2)

sql3 = '''select * from "Books";'''
cursor.execute(sql3)
for i in cursor.fetchall():
	print(i)

conn.commit()
conn.close()
