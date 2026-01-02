from tkinter import*
def close():
    win1.withdraw()
def open():
    win1.deiconify()    
win= Tk()
win1= Tk()
win.title("test") 
win.geometry('600x500')
frm1= Frame(win,bg='lightblue')
frm1.place(width=500,height=200,x=20,y=10)
lb= Label(frm1,text="welcome",width=50,height=4 )
lb.place(width=480,height=50,x=10,y=10)
bt= Button(frm1,text="close win1",command=close)
bt1=Button(frm1,text="open win1" ,command=open)
bt.place(x=100,y=100)
bt1.place(x=250,y=100)
win.mainloop()

