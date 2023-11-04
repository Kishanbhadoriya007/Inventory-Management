from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk

class SalesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Kishan and Abhikash")
        self.root.config(bg="White")
        self.root.focus_force()
        
        #===searchframe===
        SearchFrame=LabelFrame(self.root,text="Search Sales",bg="White")
        SearchFrame.place(x=250,y=20,width=600,height=70)

         #====options====
        cmb_search=ttk.Combobox(SearchFrame, values=("Select","Email","Name","ID","Contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf49",fg="white",cursor="hand2").place(x=410,y=10,width=140,height=30)

        #====text====
        title=Label(self.root,text="Sales Details",font=("Goudy old style",15),bg ="blue",fg="white").place(x=50,y=100,width=1000)


if __name__=="__main__":

    root = Tk()
    obj = SalesClass(root)
    root.mainloop()