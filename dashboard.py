import tkinter as tk
from PIL import Image, ImageTk
from employee import employeeClass
from products import ProductsClass
from category import CategoryClass
from supplier import SupplierClass
from sales import SalesClass

print("streak 1")
print("streak 2")
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Kishan and Abhikash")
        self.root.config(bg="White")
        

        # ===title===
        #self.icon_title = tk.PhotoImage(file="Git_and_github/Inventory-management/inventory.png")
        #title = tk.Label(self.root, text="Inventory Management system", image=self.icon_title, compound="left",
#                         font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(
#            x=0, y=0, relwidth=1, height=70)
        # ====button-logout
        btn_logout = tk.Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow").place(
            x=1100, y=10, height=50, width=150)
        # ====clock====
        self.lbl_clock = title = tk.Label(self.root,
                                          text="Welcome to Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time: HH:MM:SS",
                                          font=("times new roman", 15), bg="#4d636c", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        # ===left menu===
        #self.MenuLogo = Image.open("Git_and_github/Inventory-management/logoaboveframe.png")
        #self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        #self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        #lbl_menulogo = tk.Label(LeftMenu, image=self.MenuLogo)
        #lbl_menulogo.pack(side=tk.TOP, fill=tk.X)

        lbl_menu = tk.Label(LeftMenu, text="Menu", font=("times new roman",20), bg="#009688").pack(side=tk.TOP,fill=tk.X)
        btn_employee = tk.Button(LeftMenu, text="Employee",command=self.employee, font=("times new roman", 20, "bold"), bg="White",bd=3,cursor="hand2").pack(side=tk.TOP,fill=tk.X)
        btn_Supplier = tk.Button(LeftMenu, text="Supplier",command=self.supplier, font=("times new roman", 20, "bold"), bg="White",bd=3,cursor="hand2").pack(side=tk.TOP,fill=tk.X)
        btn_category = tk.Button(LeftMenu, text="category",command=self.category, font=("times new roman", 20, "bold"), bg="White",bd=3,cursor="hand2").pack(side=tk.TOP,fill=tk.X)
        btn_Products = tk.Button(LeftMenu, text="Products",command=self.products, font=("times new roman", 20, "bold"), bg="White",bd=3,cursor="hand2").pack(side=tk.TOP,fill=tk.X)
        btn_Sales = tk.Button(LeftMenu, text="Sales",command=self.sales, font=("times new roman", 20, "bold"), bg="White",bd=3,cursor="hand2").pack(side=tk.TOP,fill=tk.X)
        btn_Exit = tk.Button(LeftMenu, text="Exit", font=("times new roman", 20, "bold"), bg="White",bd=3,cursor="hand2").pack(side=tk.TOP,fill=tk.X)

        #===content==
        self.lbl_employee=tk.Label(self.root,text="Total employee\n[0]",bd=5,relief=tk.RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_Supplier=tk.Label(self.root,text="Total Supplier\n[0]",bd=5,relief=tk.RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_Category=tk.Label(self.root,text="Total Category\n[0]",bd=5,relief=tk.RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Category.place(x=1000,y=120,height=150,width=300)

        self.lbl_Products=tk.Label(self.root,text="Total Products\n[0]",bd=5,relief=tk.RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Products.place(x=300,y=300,height=150,width=300)
        
        self.lbl_Sales=tk.Label(self.root,text="Total Sales\n[0]",bd=5,relief=tk.RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Sales.place(x=650,y=300,height=150,width=300)

#======================================================================================
    def employee(self):
        self.new_win=tk.Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    def products(self):
        self.new_win=tk.Toplevel(self.root)
        self.new_obj=ProductsClass(self.new_win)
    def category(self):
        self.new_win=tk.Toplevel(self.root)
        self.new_obj=CategoryClass(self.new_win)
    def supplier(self):
        self.new_win=tk.Toplevel(self.root)
        self.new_obj=SupplierClass(self.new_win)
    def sales(self):
        self.new_win=tk.Toplevel(self.root)
        self.new_obj=SalesClass(self.new_win)

#Streak


if __name__=="__main__":

    root = tk.Tk()
    obj = IMS(root)
    root.mainloop()