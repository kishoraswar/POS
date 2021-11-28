from tkinter import*
from tkinter import font
import sqlite3
from typing import ContextManager
#from typing_extensions import ParamSpec
from PIL import Image,ImageTk    #pip install pillow
from tkinter import ttk,messagebox
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130") #width*height+x and y axis
        self.root.title("POS | By Kishor Aswar")
        self.root.config(bg="white")
        self.root.focus_force()
        #======================
        #All variable
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()


        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        
        

        
        #=====search Fram=======#
        SearchFrame=LabelFrame(self.root,text="Search Invoice",bd=2,font=("goudy old style",12,"bold"),bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #=====Options=====#
        lbl_search=Label(SearchFrame,text="Search By Invoice No.",bg="white", font=("goudy  old style",15))
        lbl_search.place(x=10,y=10)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg='lightyellow').place(x=200,y=10)
        btn_search=Button(SearchFrame,text="search", command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=10,width=150,height=30)
       
        #=====supplier title=====#
        title=Label(self.root,text="Supplier Details",font=("goudy old style",15),bg='#0f4d7d',fg="white").place(x=50,y=100,width=1000)
        
        #====Content====
        #===row one=====
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg='white').place(x=50,y=150)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg='lightyellow').place(x=150,y=150,width=180)
        #txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg='white').place(x=500,y=150,width=180)
        
        #====row2=====
        lbl_name=Label(self.root,text="Sup Name",font=("goudy old style",15),bg='white').place(x=50,y=190)       
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg='lightyellow').place(x=150,y=190,width=180)
      
        #====row3=====
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg='white').place(x=50,y=230)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg='lightyellow').place(x=150,y=230,width=180)
        
        #====row4=====
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg='white').place(x=50,y=270)
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg='lightyellow')
        self.txt_desc.place(x=150,y=270,width=300,height=60)
        
        #====Buttons====
        btn_add=Button(self.root,text="Save",command=self.add, font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update, font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete, font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear, font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)
        
        #====Employee  Details=====
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.SupplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice",text="Invoice")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("desc",text="Description")
        self.SupplierTable.heading("contact",text="Contact")
       

        self.SupplierTable["show"]="headings"

        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("desc",width=100)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        #self.show()
#=============================================================
#
#or self.var_name.get()==""
    def add(self):
        con=sqlite3.connect(database=r'pos.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": 
                messagebox.showerror("Error","Invoice Must Be Required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice Number already assigned try Different",parent=self.root)
                else:
                    cur.execute("Insert into supplier(invoice,name,contact,desc) values (?,?,?,?)",(
                                         self.var_sup_invoice.get(),
                                         self.var_name.get(),                                       
                                         self.var_contact.get(),
                                         self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()
           
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)

#=============================================================
#or self.var_name.get()==""
    def show(self):
        con=sqlite3.connect(database=r'pos.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
                                     
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)
#=================================

    def update(self):
        con=sqlite3.connect(database=r'pos.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": 
                messagebox.showerror("Error","Invoice No. Must Be Required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                         #self.var_sup_invoice.get(),
                                         self.var_name.get(),
                                         self.var_contact.get(),
                                         self.txt_desc.get('1.0',END),
                                         self.var_sup_invoice.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
           
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)

#==========================
    def delete(self):
        con=sqlite3.connect(database=r'pos.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": 
                messagebox.showerror("Error","Invoice No Must Be Required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op==True:
                         cur.execute("Delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                         con.commit()
                         messagebox.showinfo("Success","Supplier Deleted Successfully",parent=self.root)
                         self.clear()
                         

        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)
#=================on click display content inside field===treeview data to field
    def get_data(self, ev):
              f=self.SupplierTable.focus()
              content=(self.SupplierTable.item(f))
              row=content['values']
              #print(row)
              self.var_sup_invoice.set(row[0])
              self.var_name.set(row[1])
              self.var_contact.set(row[2])
              self.txt_desc.delete('1.0',END)
              self.txt_desc.insert(END,row[3])
            


#=================================

    def clear(self):
              self.var_sup_invoice.set("")
              self.var_name.set("")
              self.var_contact.set("")
              self.txt_desc.delete('1.0',END)
              #self.var_sup_invoice.set(row[11]),
              self.var_searchtxt.set("")
            
              self.show()

#================search box

    def search(self):
        con=sqlite3.connect(database=r'pos.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()==" ":
                messagebox.showerror("Error","Invoice No.Should Be Required",parent=self.root)
            else:
             cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
             row=cur.fetchone()
             if row!=None:
                self.SupplierTable.delete(*self.SupplierTable.get_children())
                self.SupplierTable.insert('',END,values=row)
             else:
                 messagebox.showerror("Error", "No Record Found ", parent=self.root)          
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)

if __name__=="__main__":    
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()


