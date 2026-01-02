from tkinter import*
from tkinter import ttk 
from tkinter import messagebox
win= Tk()

'''def show():
    print(combo.get())
Mylist = ['a','b','r','g']
combo= ttk.Combobox(win,values=Mylist)
combo.set("select a char")
Button(win,text="select",command=show)

messagebox.showinfo('showinfo','information')
messagebox.showwarning('showwarning','warning')
messagebox.showerror('showerror','error')   
print(messagebox.askquestion('askquestion','Are you sure?')) 
print(messagebox.askokcancel('askokcancel','want to continue?'))                   
print(messagebox.askyesno('askyesno','find the value?'))
print(messagebox.askretrycancel('askretrycancel','try again'))
var1=messagebox.askokcancel('askokcancel','Want to continue?')'''
win.geometry('300x400')
win.title('welcome')
w= Label(text='',font=('Aria',12))
w.pack()
var1 = messagebox.askokcancel('askokcancel','want to continue?')
print(var1)

if var1== True :
    w.config(bg='green')
else :
    w.config(bg='red')       
w.config(text='{}'.format(var1))
win.mainloop()



            
