import pymysql
mdb = pymysql.connect(
  host ='localhost',
  user ='root',
  passwd ='',
  database ='new_db'
)
con = mdb.cursor()
name_kala= input("enter name:")
price_kala= input("enter price:")
count_kala= input("enter count:")
try:
  Mysql = 'insert into kala (name,price,count) values(%s,%s,%s)'
  Myval = (name_kala,price_kala,count_kala)
  con.execute(Mysql,Myval)
  mdb.commit()
  print('insert record')
except:
  print("can not insert")

'''kala_name= input("what  is change? Enter kala name:")
up_name = input("Enter kala new  name:")
kala_price = input('Enter new price:')
sql = 'update kala  set name=%s , price=%s where name=%s' 
Myval= (kala_name,kala_price,up_name)
con.execute(sql, Myval)
mdb.commit()'''
   
