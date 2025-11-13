#عددی را دریافت کرده و اعدد کوچکتر از آن را چاپ کنید 
'''n=int(input("enter number:"))
for i in range(n) :
    print(i)

 #اعداد زوج دو رقمی 
for i in range(10,99):
    if i%2!=0:
     continue
    print(i) 
# مضربهای عدد پنج کمتر از دویست
for i in range(5,200) :
 if i%5==0 :
  print(i) 
#چاپ اعداد اول کوچکتر از عدد دریافتی 
n=int(input("enter number:"))
def is_prime(n):
  for i in range(2,n) :
    if n%i == 0 :
      return False
    else:
     return True      
counter=0
prime_list = [] 
for j in range(2,n) :
         if is_prime(j)== True:
             counter+=1
             prime_list.append(j)
print(counter)
print(prime_list)
 #دو عدد دریافت کرده و مقسوم علی های مشترکشان را چاپ کند
n=int(input('enter first number:'))
m=int(input("enter second number:"))
for i in range (1, min(n,m)) :
 if n%i==0 and m%i ==0 :
  print(i) 
# دو عدد دریافت کرده و با انتخاب کاربر اعداد زوج یا فرد بین آنها رو چاپ کند
n=int(input('Enter first number:'))
m=int(input("Enter second number:"))
meno=(input("Select 1 or 2:"))
if n>m :
 max=n
 min=m
else:
   max=m
   min=n 

match (meno) :
    case "1" :
        for i in range(min,max+1) :
          if i %2 != 0:
             print(i)
    case "2" :
         for i in range(min,max+1):
           if i %2 == 0  :
              print(i)
    case _:
      print("Eror")'''
#تعدادی نمره از کاربر بگیر که پایان مشخصی داشته باشد و سپس بزرگترین و مجموع آنرا چاپ کند    
n=int(input("Enter cout number:"))
numbers=[]
for i in range(n):
      num=float(input(" number:"))
      if  num==-1 :
         break
      numbers.append(num)
sum_numbers=sum(numbers) 
max_numbers=max(numbers) 
print("sum of numbers:",sum_numbers)
print("max of numbers:",max_numbers)    
   


                 
          

          
  

     