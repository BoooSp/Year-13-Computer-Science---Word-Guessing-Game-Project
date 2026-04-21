import tkinter as tk
import random
from tkinter import messagebox
#from PIL import Image, ImageTk

def main_page(self):
    for widget in self.winfo_children():
        widget.destroy()
#I shall put all the thingy things inside this
        label = tk.Label(root,text="Stella Verba")
        label.pack()
        self.root.geometry("1200x800")
        self.root.title("StellaVerba")

root = tk.Tk()
root.mainloop()