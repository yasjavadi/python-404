from tkinter import*
win=Tk()
win.geometry('300x400+300+300')
win.title('login')
fields={}
fields['user_name_lable']= Label(win,text='username')
fields['user_name']= Entry(win)
fields['password_lable']= Label(win,text='password')
fields['password']= Entry(win,show='*')
for f in fields.values():
    f.pack(anchor=W , fill=X , padx= 10 ,pady= 5)
Button(win,text='login').pack(anchor=W  , padx=10 , pady=5)
win.mainloop()