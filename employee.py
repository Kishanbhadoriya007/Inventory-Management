from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk

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

         #******Row3*******

        lbl_address=Label(self.root,text="Address",font=("Goudy old style",15),bg ="White").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("Goudy old style",15),bg ="White").place(x=420,y=270)

        self.xt_address=Text(self.root,font=("Goudy old style",15),bg ="lightblue").place(x=120,y=270,width=180)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("Goudy old style",15),bg="lightblue").place(x=500,y=230,width=180)



if __name__=="__main__":

    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
