from tkinter import *
def add():
    lb.config(text=int(txt1.get())+int(txt2.get()))
# **********************************************
def minus():
    lb.config(text=int(txt1.get())-int(txt2.get()))  
 #***********************************************
def multi():
    lb.config(text=int(txt1.get)*int(txt2.get())) 
# *************************************************
def division():
    lb.config(text=int(txt1.get())/int(txt2.get()))
 #******************************************
      
win=Tk()
win.title("test")
win.geometry("300x400")
lb1 = Label(win,text="Number1:",bg='orange',fg='blue')
lb2 = Label(win,text="Number2:",bg='orange',fg='blue')
txt1= Entry(win)
txt2 = Entry(win)
but1 = Button(win,text='+',bg='red',fg='black',width=4,height=2,command=add)
but2 = Button(win,text='-',bg='red',fg='black',width=4,height=2,command=minus)
but3 = Button(win,text='*',bg='red',fg='black',width=4,height=2,command=multi)
but4 = Button(win,text='/',bg='red',fg='black',width=4,height=2,command=division)
lb3= Label(win,text='Result:',bg='orange',fg='blue')
lb=Label(win,text='-----')
lb1.grid(row=0,column=2)
txt1.grid(row=1,column=2)
lb2.grid(row=2,column=2)
txt2.grid(row=3,column=2)
but1.grid(row=4,column=0)
but2.grid(row=4,column=1)
but3.grid(row=4,column=2)
but4.grid(row=4,column=3)
lb3.grid(row=7,column=2)
lb.grid(row=8,column=2)
win.mainloop() 
