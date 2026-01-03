import csv

'''with open("newfile1.csv","w") as csvfile:  
 f= csv.DictWriter (csvfile,fieldnames=['name','age','class'])
 f.writeheader()
 f.writerow({'name':'zahra','age':22,'class':204})
 f.writerow({'name':'reza','age':22,'class':205})'''

with open ('person.csv','r') as csvfile:
 f= csv.reader(csvfile)
 for x in f :
  print(x)



