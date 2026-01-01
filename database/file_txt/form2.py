'''f=open("newfile.txt",'r+')
f.write('how are you?')
txt=input("Enter message:")
f.write(txt)
f.seek(5)
a=f.readline()
print(a)
print(f.tell())
f.close()'''
myfile= open("newfile.txt",'w+')
for x in range(3):
    name=input('Enter Name:')
    myfile.write(name+'\n')
myfile.seek(0)
for x in range(3):
    print(f'name {x+1} is:')
    print(myfile.readline())
myfile.close()


