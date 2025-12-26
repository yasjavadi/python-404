import pymysql
mdb =pymysql.connect(
    host= 'localhost',
    user = 'root',
    password = '',
    database = 'new_db'
)
con= mdb.cursor()
name_kala= input('Enter name:')
code_kala=input("Entsr code:")
sql = 'select * from kala where name=%s and cod>=%s'
myval= (name_kala,code_kala)
con.execute(sql,myval)
r=con.fetchall()
for x in r:
 print(x)

