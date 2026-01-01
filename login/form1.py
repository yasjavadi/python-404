from tkinter import*
from tkinter import ttk
def add():
    with open('student_file.txt','a',encoding='utf-8') as f :
        f.write(Entry_name.get()+'')
        f.write(Entry_course.get()+'')
        f.write(Entry_class.get()+'')
        Entry_name.delete(0,END)
        Entry_course.delete(0,END)
        Entry_class.delete(0,END)
#*********************************************************
def search():
    with open('student_file.txt','r',encoding='utf-8') as f :
     Alltext = f.readlines()
    print(Alltext)
    if Entry_name in Alltext:
        print('ok')
    else:
        print('Can not found')   
#*********************************************************
def show() :
   print(combo.get)
win = Tk()
win.geometry("400x500")
win.title('form')
#name
lb1=Label(win,text='Enter Name:')
Entry_name=Entry(win,bg='lightblue')
lb1.place(x=30,y=50)
Entry_name.place(x=120,y=50)
#course

mylist=['python','javascripy','c++']
combo=ttk.Combobox(win,valuse= mylist)
combo.place(x=120,y=100)
Button(win,text='select',command= show).pack()
#class
lb3= Label(win,text='Enter class:')
Entry_class= Entry(win,bg='lightblue')
lb3.place(x=30,y=150)
Entry_class.place(x=120,y=150)
#*******************************
but= Button(win,text='add',command=add)
but.place(x=150,y=200)
but1=Button(win,text='search',command=search)
but1.place(x=200,y=200)



win.mainloop()