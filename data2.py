import pymysql
mdb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='new_db'
)
con = mdb.cursor()
try:
  Mysql = 'DELETE FROM `kala` WHERE  name ="tv"'
  con.execute(Mysql)
  mdb.commit()
  print('deleted record')
except:
  print("can not delet")
