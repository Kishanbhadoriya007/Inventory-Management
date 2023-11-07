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

        #====searchFrame=====
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="White")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #====options====
        cmb_search=ttk.Combobox(SearchFrame, values=("Select","Email","Name","ID","Contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchby,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,textvariable=self.var_searchby,text="Search",font=("goudy old style",15),bg="#4caf49",fg="white",cursor="hand2").place(x=410,y=10,width=140,height=30)

        #====text====
        title=Label(self.root,text="Employee Details",font=("Goudy old style",15),bg ="blue",fg="white").place(x=50,y=100,width=1000)
        #*****Content*****
        label_empid=Label(self.root,text="Emp ID",font=("Goudy old style",15),bg ="White").place(x=50,y=150)
        label_gender=Label(self.root,text="Gender",font=("Goudy old style",15),bg ="White").place(x=550,y=150)

        cmb_gender=ttk.Combobox(SearchFrame,textvariable=self.var_gender, values=("Select","Email","Name","ID","Contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_gender.place(x=10,y=10,width=180)
        cmb_gender.current(0)

        label_contact=Label(self.root,text="Contact",font=("Goudy old style",15),bg ="White").place(x=950,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("Goudy old style",15),bg ="White").place(x=50,y=150,width=180)
        txt_gender=Entry(self.root,textvariable=self.var_gender,font=("Goudy old style",15),bg ="White").place(x=550,y=150,width=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("Goudy old style",15),bg ="White").place(x=950,y=150,width=180)


if __name__=="__main__":

    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
