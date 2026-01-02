from tkinter import*
from tkinter import messagebox

def save_data():
   name= book_name.get() 
   writer=writer_name.get()
   book_count= count_b.get()
   
   if not book_name or writer_name or count_b:
      messagebox.showwarning("لطفا همه فیلدها را پر کنید","اخطار")
      return
   data = f"نام کتاب{name},نام نویسنده{writer},تعداد{book_count}\n"
   #نمایش در کادر متنی
   text_box.insert(END,data)
   #ذخیره در فایل
   with open('data_txt','a',encoding='utf-8') as file:
      file.write(data)

  # پاک کردن فیلدها
   book_name.delete(0,END) 
   writer_name.delete(0,END)
   count_b.delete(0,END)
   messagebox.showinfo("اطلاعات با موفقیت ذخیره شد","موفقیت")
   
root=Tk()
root.title('کتابخانه')
root.geometry('500x500')

lb1=Label(root,text='نام کتاب',font=('bnazanin',12))
lb1.place(x=350,y=10)
book_name=Entry(root)
book_name.place(x=220,y=10)

lb2=Label(root,text='نام نویسنده',font=('bnazani',12))
lb2.place(x=350,y=50)
writer_name=Entry(root)
writer_name.place(x=220,y=50)

lb3=Label(root,text='تعداد',font=('bnazanin',12))
lb3.place(x=350,y=90)
count_b=Entry(root)
count_b.place(x=220,y=90)

btn_save=Button(root,text='افزودن',command=save_data,bg="blue",fg="white")
btn_save.place(x=250,y=120)

text_box= Text(root,width=50,height=10)
text_box.place(x=50,y=180)

root.mainloop()