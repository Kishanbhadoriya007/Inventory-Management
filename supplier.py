from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class SupplierClass: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Kishan and Abhikash")
        self.root.config(bg="White")
        self.root.focus_force()
        #*******Variables******
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        #====searchFrame=====
        SearchFrame=LabelFrame(self.root,text="Search supplier",bg="White")
        #SearchFrame.place(x=250,y=20,width=600,height=70)

        #====options====
        lbl_search=Label(SearchFrame,text="Search by invoice No.",bg="white",font=("times new roman",15))
        lbl_search.place(x=10,y=10)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightblue").place(x=200,y=10)

        #*****button*****
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf49",fg="white",cursor="hand2").place(x=410,y=10,width=140,height=30)

        #====title====
        title=Label(self.root,text="Supplier Details",font=("Goudy old style",25,"bold"),bg ="blue",fg="white").place(x=50,y=10,width=1000,height=40)

        #*****Content*****
        #*****Row1******* 
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("Goudy old style",15),bg ="White").place(x=30,y=60)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("Goudy old style",15),bg ="lightblue").place(x=120,y=60,width=180)

        #******Row2*******

        lbl_name=Label(self.root,text="Name",font=("Goudy old style",15),bg ="White").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("Goudy old style",15),bg ="lightblue").place(x=120,y=100,width=180)

        #******Row3*******

        lbl_contact=Label(self.root,text="Contact",font=("Goudy old style",15),bg ="White").place(x=50,y=140)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("Goudy old style",15),bg ="lightblue").place(x=120,y=140,width=180)

         #******Row4*******

        lbl_desc=Label(self.root,text="Description",font=("Goudy old style",15),bg ="White").place(x=25,y=180)

        self.txt_desc=Text(self.root,font=("Goudy old style",15),bg ="lightblue")
        self.txt_desc.place(x=120,y=180,width=300,height=60)
    
        #******Buttons******
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=120,y=305,width=110,height=30)
        btn_update=Button(self.root,text="update",command=self.Update,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=240,y=305,width=110,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=360,y=305,width=110,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="grey",fg="white",cursor="hand2").place(x=480,y=305,width=110,height=30)

        #*****Details of suppliers****

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice", text="EMP ID")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("desc", text="Description")

        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        #self.show()

#*************Functions*************************

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor();
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice No. already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","supplier added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

#*********Show-Function***********
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor();
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#******Get-data******
    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])      
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])
#*********Update-Function*****************
    def Update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        cur.prepare("select * from supplier where invoice=?")
        cur.execute(self.var_sup_invoice.get())

        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_desc.get('1.0',END),
                                                self.var_sup_invoice.get(),                                                     
                    ))
                    con.commit()
                    messagebox.showinfo("Success","supplier Updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#***************Delete**********************
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor();
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","supplier Deleted Successfully",parent=self.root)
                        self.clear()
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#*******Clear-Function********

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()
#***********Search-Function**********

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor();
        try:
           
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. is required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(+ self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


        

if __name__=="__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()