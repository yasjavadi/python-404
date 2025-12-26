import pymysql
mdb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='new_db'
)
con = mdb.cursor()
kala_name=input('enetr name:')
kala_price=input('enetr price:')
kala_count=input('enetr count:')

try:
     sql = 'INSERT INTO `kala`(`name`, `price`, `count`) VALUES(%s,%s,%s)'
     Myvar= (kala_name,kala_price,kala_count)
     con.execute(sql, Myvar)
     mdb.commit()
     print('insert data')
except:
     print('can not insert')  
     mdb.rollback()   
