from tkinter import*
import tkinter as tk 
win =tk.Tk()
win.title('test')
win.geometry('300x400')

lable= tk.Label(win,text='welcome',font=('arial',25),bg='lightblue')
lable.pack(anchor='w',fill='x'padx=10,pady=5)

entry= tk.Entry(win)
entry.pack()

btn= tk.Button(win,text='click me',bg='lightgreen',command= lambda: lable.config(text=f'hello {entry.get()}'))
btn.pack()
 
win.mainloop() 