
'''class Person:
    def __init__(self):
       self.name=name
       self.age=age
object_person=Person('roz',23) 
print(f"I'm {object_person.name} I'm {object_person.age} years old")      
from datetime import date
class  Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # classmethod
    def calculate_age(cls,name,birth_year):

        return cls(name,date.today().year-birth_year)  
    def show(self):
        print(self.name+"'s age is:"+ str(self.age))
bob= Student.calculate_age("bob",1995)  
bob.show()   '''     
import tkinter as tk
from tkinter import messagebox
import json
import os
# نام فایل برای ذخیره اطلاعات کتابخانه
LIBRARY_FILE = "library.json"

# تابع برای بارگذاری اطلاعات کتابخانه از فایل JSON
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # اگر فایل خالی یا خراب بود، لیست خالی برگردان
                return []
    return []

# تابع برای ذخیره اطلاعات کتابخانه در فایل JSON
def save_library(library_data):
    with open(LIBRARY_FILE, 'w', encoding='utf-8') as f:
        json.dump(library_data, f, indent=4, ensure_ascii=False)

# تابع برای اضافه کردن کتاب
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    try:
        count = int(entry_count.get())
        if not title or not author or count <= 0:
            messagebox.showwarning("ورودی نامعتبر", "لطفاً عنوان، نویسنده و تعداد معتبر وارد کنید.")
            return
    except ValueError:
        messagebox.showwarning("ورودی نامعتبر", "تعداد باید یک عدد صحیح باشد.")
        return

    # بررسی اینکه آیا کتاب با این عنوان و نویسنده از قبل وجود دارد
    for book in library:
        if book["title"] == title and book["author"] == author:
            book["count"] = str(int(book["count"]) + count) # افزایش تعداد
            update_book_list()
            save_library(library)
            messagebox.showinfo("موفقیت", f"تعداد کتاب '{title}' به‌روز شد.")
            clear_entries()
            return

    # اضافه کردن کتاب جدید
    book_id = len(library) + 1 # یک شناسه ساده برای کتاب
    library.append({"id": str(book_id), "title": title, "author": author, "count": str(count)})
    update_book_list()
    save_library(library)
    messagebox.showinfo("موفقیت", "کتاب با موفقیت اضافه شد.")
    clear_entries()

# تابع برای حذف کتاب
def delete_book():
    selected_item = listbox_books.curselection()
    if not selected_item:
        messagebox.showwarning("انتخاب نشده", "لطفاً کتابی را برای حذف از لیست انتخاب کنید.")
        return

    book_index = selected_item[0]
    book_to_delete = library[book_index]
    
    # تایید حذف
    confirm = messagebox.askyesno("تایید حذف", f"آیا از حذف کتاب '{book_to_delete['title']}' مطمئن هستید؟")
    if confirm:
        del library[book_index]
        update_book_list()
        save_library(library)
        messagebox.showinfo("موفقیت", "کتاب با موفقیت حذف شد.")
        clear_entries()

# تابع برای به‌روزرسانی لیست نمایش کتاب‌ها
def update_book_list():
    listbox_books.delete(0, tk.END)
    for book in library:
        listbox_books.insert(tk.END, f"ID: {book['id']} - عنوان: {book['title']} - نویسنده: {book['author']} - تعداد: {book['count']}")

# تابع برای پاک کردن فیلدهای ورودی
def clear_entries():
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_count.delete(0, tk.END)

# تابع برای انتخاب کتاب از لیست و پر کردن فیلدهای ورودی (برای ویرایش یا حذف راحت‌تر)
def select_book(event):
    selected_item = listbox_books.curselection()
    if not selected_item:
        return

    book_index = selected_item[0]
    book = library[book_index]

    clear_entries()
    entry_title.insert(0, book['title'])
    entry_author.insert(0, book['author'])
    entry_count.insert(0, book['count'])

# --- راه‌اندازی رابط کاربری ---
root = tk.Tk()
root.title("مدیریت کتابخانه")
root.geometry("600x500")
root.resizable(False, False) # جلوگیری از تغییر اندازه پنجره

# --- فریم ورودی‌ها ---
frame_input = tk.Frame(root, padx=10, pady=10)
frame_input.pack(pady=10)

tk.Label(frame_input, text="عنوان کتاب:").grid(row=0, column=0, sticky=tk.W, pady=2)
entry_title = tk.Entry(frame_input, width=40)
entry_title.grid(row=0, column=1, pady=2)

tk.Label(frame_input, text="نویسنده:").grid(row=1, column=0, sticky=tk.W, pady=2)
entry_author = tk.Entry(frame_input, width=40)
entry_author.grid(row=1, column=1, pady=2)

tk.Label(frame_input, text="تعداد:").grid(row=2, column=0, sticky=tk.W, pady=2)
entry_count = tk.Entry(frame_input, width=40)
entry_count.grid(row=2, column=1, pady=2)

# --- دکمه‌ها ---
frame_buttons = tk.Frame(root, padx=10, pady=5)
frame_buttons.pack()

btn_add = tk.Button(frame_buttons, text="افزودن کتاب", command=add_book, width=15)
btn_add.grid(row=0, column=0, padx=5)

btn_delete = tk.Button(frame_buttons, text="حذف کتاب انتخاب شده", command=delete_book, width=15)
btn_delete.grid(row=0, column=1, padx=5)

# --- لیست کتاب‌ها ---
frame_list = tk.Frame(root, padx=10, pady=10)
frame_list.pack(fill=tk.BOTH, expand=True)

tk.Label(frame_list, text="لیست کتاب‌ها:").pack(anchor=tk.W)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_books = tk.Listbox(frame_list, height=15, width=70, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
listbox_books.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox_books.yview)

# اتصال رویداد انتخاب آیتم در لیست به تابع select_book
listbox_books.bind('<<ListboxSelect>>', select_book)

# --- بارگذاری اطلاعات اولیه ---
library = load_library()
update_book_list()

# --- اجرای برنامه ---
root.mainloop()
