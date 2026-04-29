import tkinter as tk
from tkinter import mainloop
class StellaVerba:
    def __init__(self, root):
        self.root = root
        self.home_page = ()
root = tk.Tk()
#The title of the game in the bar thingy on top of the normal interface page
root.title("StellaVerba")
#The size of my page
root.geometry("1200x800")
#Prevent the width or the height being changed by users to prevent any errors from decreasing or increasing size of the screen
label = tk.Label(root, text="Stella Verba")
label.pack()
button = tk.Button(root, text="Bye", width = 25,command=root.destroy)
button.pack()
root.mainloop()