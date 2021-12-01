from os import stat
from tkinter import*
from tkinter import font
import sqlite3
from typing import ContextManager
#from typing_extensions import ParamSpec
from PIL import Image,ImageTk    #pip install pillow
from tkinter import ttk,messagebox
class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130") #width*height+x and y axis
        self.root.title("POS | By Kishor Aswar")
        self.root.config(bg="white")
        self.root.focus_force()
#=============title
        lbl_title=Label(self.root,text="View Customer Bills", font=("goudy old style",30),fg="white",bd=3,relief=RIDGE,bg="#184a45").pack(side=TOP,fill=X,padx=10,pady=20)



if __name__=="__main__":    
    root=Tk()
    obj=salesClass(root)
    root.mainloop()