import tkinter as tk
from tkinter import messagebox
FILE_NAME ="books.txt"   #نام فایل برای ذخیره اطلاعات
#تابع ذخیره کتاب جدید
def add_book():
    name =name_entry.get().strip()
    author =author_entry.get().split()
    count=count_entry.get().split()
    if not name or not author or not count :
        messagebox.showwarning("لطفا همه فیلدها را پر کنید","خطا!")
        return
    #ذخیره در فایل
    with open("FILE_NAME","a",encoding="utf_8") as f:
        f.write(f"{name}|{author}|{count}\n")
    listbox.insert(tk.END,f"{name}-{author}({count})")
    #پاک کردن ورودی ها
    name_entry.delete(0,tk.END)
    author_entry.delete(0,tk.END)
    count_entry.delete(0,tk.END) 
    # تابع حذف کتاب انتخاب شده از لیست       
def delete_book():
    selected=listbox.curselection()
    if not selected:
        messagebox.showinfo("هیچ کتابی انتخاب نشده است.","توجه!")
        return
    index =selected[0]
    book_text= listbox.get(index)
    #بازنویسی فایل بعد از حذف کتاب انتخابی
    with open("FILE_NAME","r",encoding='utf_8') as f :
        lines = f.readlines()
    with open("FILE_NAME","r",encoding='utf_8') as f:
        for line in lines :
            if book_text.strip("()[0]not in line"):
                f.write(line)
                # تابع بارگذاری کتابها از فایل 
def load_book():
    listbox.delete(0,tk.END)
    try:
        with open("FILE_NAME","r",encoding="utf_8") as f:
            for line in f:
                name,author,count=line.split().split("|")
                listbox.insert(tk.END,f"{name}-{author}({count})")
    except FileNotFoundError:
        pass


       

root=tk.Tk()
root.title("مدیریت کتابخانه")
root.geometry("400x400")
 # ورودی ها  
lable = tk. Label(root,text='نام کتاب').pack()
name_entry= tk.Entry(root)
name_entry.pack()
lable= tk.Label(root,text="نام نویسنده").pack()
author_entry= tk.Entry(root)
author_entry.pack()
lable = tk.Label(root,text="تعداد").pack()
count_entry= tk.Entry(root)
count_entry.pack()

tk.Button(root,text="افزودن کتاب",fg="blue",bg="yellow",command=add_book).pack(pady=5)
tk.Button(root,text="حذف کتاب",fg="blue",bg="yellow",command="delete_book").pack()

listbox= tk.Listbox(root,width=50)
listbox.pack(pady=10)

root.mainloop()