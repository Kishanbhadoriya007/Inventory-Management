from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Kishan and Abhikash")
        self.root.config(bg="White")
        self.root.focus_force()
        #*******Variables******
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()

        #====searchFrame=====
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="White")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #====options====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=("Select","Email","Name","ID","Contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightblue").place(x=200,y=10)

        #*****button*****
        btn_search=Button(SearchFrame,textvariable=self.var_searchby,font=("goudy old style",15),bg="#4caf49",fg="white",cursor="hand2").place(x=410,y=10,width=140,height=30)

        #====text====
        title=Label(self.root,text="Employee Details",font=("Goudy old style",15),bg ="blue",fg="white").place(x=50,y=100,width=1000)

        #*****Content*****
        #*****Row1*******
        lbl_empid=Label(self.root,text="Emp ID",font=("Goudy old style",15),bg ="White").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("Goudy old style",15),bg ="White").place(x=430,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("Goudy old style",15),bg ="White").place(x=800,y=150)

        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender, values=("Select","male","female","other"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("Goudy old style",15),bg ="lightblue").place(x=120,y=150,width=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("Goudy old style",15),bg="lightblue").place(x=870,y=150,width=180)

        #******Row2*******

        lbl_name=Label(self.root,text="Name",font=("Goudy old style",15),bg ="White").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("Goudy old style",15),bg ="White").place(x=430,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("Goudy old style",15),bg ="White").place(x=800,y=190)

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
        btn_update=Button(self.root,text="update",font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=30)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="grey",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=30)

        #*****Details of employees****

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=200)
        self.EmployeeTable.pack(fill=BOTH,expand=1)

        self.show()

#*************Functions*************************

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor();
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This employee ID already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
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
                    messagebox.showinfo("Success","Employee added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor();
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):
        pass

if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()