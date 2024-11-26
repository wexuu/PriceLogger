import tkinter
from tkinter import ttk
import sv_ttk, os
from var import project_path
import func
#Everything main window related. Mostly misc
root = tkinter.Tk()
root.geometry("800x500")
root.maxsize(1000, 900)

#Checking whether database exists />/ creating it 
if(os.path.exists(project_path+"\\db.db")==False):
    func.createdb()

tabControl = ttk.Notebook(root) 
tabAdd = ttk.Frame(tabControl) 
tabDel = ttk.Frame(tabControl) 
tabView = ttk.Frame(tabControl) 

tabControl.add(tabView, text ='Przeglądaj') 
tabControl.add(tabAdd, text ='Dodaj') 
tabControl.add(tabDel, text ='Usuń') 
tabControl.pack(expand = 1, fill ="both") 
  
ttk.Label(tabView,  
          text ="przegladanie itemow").grid(column = 0,  
                               row = 0, 
                               padx = 30, 
                               pady = 30)   
ttk.Label(tabAdd,  
          text ="dodawanie itemow").grid(column = 0,  
                               row = 0, 
                               padx = 30, 
                               pady = 30)   
ttk.Label(tabDel, 
          text ="usuwanie itemow").grid(column = 0, 
                                    row = 0,  
                                    padx = 30, 
                                    pady = 30) 













root.mainloop()
