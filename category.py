from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class CategoryClass: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Kishan and Abhikash")
        self.root.config(bg="White")
        self.root.focus_force()
        #******title********
        lbl_title=Label(self.root,text="Manage Category")


if __name__=="__main__":
    root = Tk()
    obj = CategoryClass(root)
    root.mainloop()