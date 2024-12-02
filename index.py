import tkinter as tk
from tkinter import ttk
import os, pyglet
from var import project_path
import sqlite3 
#Mostly misc
root = tk.Tk()
root.geometry("900x600")
root.maxsize(900, 600)
pyglet.font.add_file("PriceLogger\LEMONMILK.otf")
#Checking whether database exists />/ creating it 
#if(os.path.exists(project_path+"\\db.db")==False):
#   import func.createdb
#  print(func.createdb.createdb())
con = sqlite3.connect("db.db")

tabControl = ttk.Notebook(root) 
tabAdd = tk.Frame(tabControl) 
tabDel = tk.Frame(tabControl) 
tabView = tk.Frame(tabControl) 

tabControl.add(tabView, text ='Przeglądaj') 
tabControl.add(tabAdd, text ='Dodaj') 
tabControl.add(tabDel, text ='Usuń') 
tabControl.pack(expand = 1, fill ="both") 




#View Tab
tk.Label(tabView,  text ="przegladanie itemow", width=40).grid(padx = 30, pady = 30,)   





#Add Tab
tk.Label(tabAdd,  
    text ="Dodaj przedmiot",font=("LEMON MILK",20),justify="left").grid(column = 0,  row = 0,pady = 10)
tree = ttk.Treeview(tabAdd,columns=("name","type","price","shop","date"))
tree.heading("name", text="Name")
tree.heading("type", text="Type")
tree.heading("price", text="Price")
tree.heading("shop", text="Shop")
tree.heading("date", text="Date")
tree.grid(column=0,row=1)
tree.insert("", tk.END, text="Item 1")






#Delete Tab
tk.Label(tabDel, 
    text ="usuwanie itemow").grid(column = 0, row = 0)

#name_var=tk.StringVar()
#type_var=tk.StringVar()
#price_var=tk.StringVar()
#shop_var=tk.StringVar()
#date_var=tk.StringVar()


#def submit():

#    name=name_var.get()
#    type = type_var.get()
#    price = price_var.get()
#    shop = shop_var.get()
#    date = date_var.get()
#    cur = con.cursor()
#    cur.execute(f"""
#    INSERT INTO products VALUES ({type},{price},{shop},{name},{date})
#    """)
#    con.commit()


#name_label = tk.Label(tabAdd, text = 'Username1', font=('calibre',10, 'bold'), width=30).grid(padx=20,pady=20)

# creating a entry for input
# name using widget Entry
#name_entry = tk.Entry(tabAdd,textvariable = name_var, font=('calibre',10,'normal'), width=30).grid(padx=20,pady=20)
#type_entry = tk.Entry(tabAdd,textvariable = type_var, font=('calibre',10,'normal'), width=30).grid(padx=20,pady=20)
#price_entry = tk.Entry(tabAdd,textvariable = price_var, font=('calibre',10,'normal'), width=30).grid(padx=20,pady=20)
#shop_entry = tk.Entry(tabAdd,textvariable = shop_var, font=('calibre',10,'normal'), width=30).grid(padx=20,pady=20)
#date_entry = tk.Entry(tabAdd,textvariable = date_var, font=('calibre',10,'normal'), width=30).grid(padx=20,pady=20)

#sub_btn=tk.Button(tabView,text = 'Submit', command = submit).grid(padx=20,pady=20)






















root.mainloop()
