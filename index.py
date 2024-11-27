import tkinter as tk
from tkinter import ttk
import os
from var import project_path
#Everything main window related. Mostly misc
root = tk.Tk()
root.geometry("800x500")
root.maxsize(1000, 900)

#Checking whether database exists />/ creating it 
if(os.path.exists(project_path+"\\db.db")==False):
    import func.createdb
    print(func.createdb.createdb())


tabControl = ttk.Notebook(root) 
tabAdd = tk.Frame(tabControl) 
tabDel = tk.Frame(tabControl) 
tabView = tk.Frame(tabControl) 

tabControl.add(tabView, text ='Przeglądaj') 
tabControl.add(tabAdd, text ='Dodaj') 
tabControl.add(tabDel, text ='Usuń') 
tabControl.pack(expand = 1, fill ="both") 

tk.Label(tabView,  text ="przegladanie itemow", width=40).grid(padx = 30, pady = 30,)   
tk.Label(tabAdd,  
    text ="dodawanie itemow").grid(column = 0,  row = 0,pady = 30)   
tk.Label(tabDel, 
    text ="usuwanie itemow").grid(column = 0, row = 0)

name_var=tk.StringVar()
passw_var=tk.StringVar()


def submit():

    name=name_var.get()
    
    print("The name is : " + name)
    
    name_var.set("")


name_label = tk.Label(tabView, text = 'Username', font=('calibre',10, 'bold'), width=30).grid(padx=20,pady=20)

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(tabView,textvariable = name_var, font=('calibre',10,'normal'), width=30).grid(padx=20,pady=20)

sub_btn=tk.Button(tabView,text = 'Submit', command = submit).grid(padx=20,pady=20)






















root.mainloop()
