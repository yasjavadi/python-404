import csv

with open ('newfhie1.csv','w') as csvfile:

  f = csv.DictWriter (csvfile,fieldnames=['name','age','grade'])
  f.writeheader()
  f.writerow ({'name':'ali','age':23,'grade':13})
  f.writerow({'name':'reza','age':25,'grade':18})



'''with open ('person.csv','r') as csvfile:
 f= csv.reader(csvfile)
 for x in f :
  print(x)'''



