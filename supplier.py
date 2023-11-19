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

        self.var_sup_id=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        #====searchFrame=====
        SearchFrame=LabelFrame(self.root,text="Search supplier",bg="White")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #====options====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=("Select","Email","Name","ID","Contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightblue").place(x=200,y=10)

        #*****button*****
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf49",fg="white",cursor="hand2").place(x=410,y=10,width=140,height=30)

        #====text====
        title=Label(self.root,text="supplier Details",font=("Goudy old style",15),bg ="blue",fg="white").place(x=50,y=100,width=1000)

        #*****Content*****
        #*****Row1*******
        lbl_supid=Label(self.root,text="Emp ID",font=("Goudy old style",15),bg ="White").place(x=50,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("Goudy old style",15),bg ="White").place(x=800,y=150)


        txt_supid=Entry(self.root,textvariable=self.var_emp_id,font=("Goudy old style",15),bg ="lightblue").place(x=120,y=150,width=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("Goudy old style",15),bg="lightblue").place(x=870,y=150,width=180)

        #******Row2*******

        lbl_name=Label(self.root,text="Name",font=("Goudy old style",15),bg ="White").place(x=50,y=190)
       
        txt_name=Entry(self.root,textvariable=self.var_name,font=("Goudy old style",15),bg ="lightblue").place(x=120,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("Goudy old style",15),bg="lightblue").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("Goudy old style",15),bg="lightblue").place(x=870,y=190,width=180)

        #******Row3*******

        lbl_email=Label(self.root,text="Email",font=("Goudy old style",15),bg ="White").place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",font=("Goudy old style",15),bg ="White").place(x=420,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("Goudy old style",15),bg ="White").place(x=780,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("Goudy old style",15),bg ="lightblue").place(x=120,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("Goudy old style",15),bg="lightblue").place(x=500,y=230,width=180)
        txt_utype=Entry(self.root,textvariable=self.var_utype,font=("Goudy old style",15),bg="lightblue").place(x=870,y=230,width=180)
        
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype, values=("Admin","Employess"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_utype.place(x=870,y=230,width=180)
        cmb_utype.current(0)

         #******Row4*******

        lbl_address=Label(self.root,text="Address",font=("Goudy old style",15),bg ="White").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("Goudy old style",15),bg ="White").place(x=500,y=270)

        self.txt_address=Text(self.root,font=("Goudy old style",15),bg ="lightblue")
        self.txt_address.place(x=120,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("Goudy old style",15),bg="lightblue").place(x=580,y=270,width=200)

        #******Buttons******
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=30)
        btn_update=Button(self.root,text="update",command=self.Update,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="grey",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=30)

        #*****Details of suppliers****

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("eid", text="EMP ID")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("email", text="Email")
        self.supplierTable.heading("gender", text="Gender")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("dob", text="D.O.B")
        self.supplierTable.heading("doj", text="D.O.J")
        self.supplierTable.heading("pass", text="Password")
        self.supplierTable.heading("utype", text="User Type")
        self.supplierTable.heading("address", text="Address")
        self.supplierTable.heading("salary", text="Salary")

        self.supplierTable["show"]="headings"

        self.supplierTable.column("eid", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("email", width=100)
        self.supplierTable.column("gender", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("dob", width=100)
        self.supplierTable.column("doj", width=100)
        self.supplierTable.column("pass", width=100)
        self.supplierTable.column("utype", width=100)
        self.supplierTable.column("address", width=100)
        self.supplierTable.column("salary", width=200)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#*************Functions*************************

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor();
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","supplier ID must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This supplier ID already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
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
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])
#*********Update-Function*****************
    def Update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor();
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","supplier ID must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid supplier ID",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),
                                                self.var_pass.get(),
                                                self.var_utype.get(),
                                                self.txt_address.get('1.0',END),
                                                self.var_salary.get(),
                                                self.var_emp_id.get(),
                                                     
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
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","supplier ID must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid supplier ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","supplier Deleted Deleted Successfully",parent=self.root)
                        self.clear()
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#*******Clear-Function********

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END)
        self.var_salary.set("")
        self.show()
#***********Search-Function**********

    def search():
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor();
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search Input is required",parent=self.root)
            else:
                cur.execute("select * from supplier where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


        

if __name__=="__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()