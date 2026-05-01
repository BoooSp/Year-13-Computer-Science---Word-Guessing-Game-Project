import tkinter as tk
from PIL import ImageTk, Image

from tkinter import mainloop

root = tk.Tk()
#The title of the game in the bar thingy on top of the normal interface page
root.title("StellaVerba")
#The size of my page
root.geometry("1200x800")
#Prevent the width or the height being changed by users to prevent any errors from decreasing or increasing size of the screen
root.resizable(False,False)
label = tk.Label(root, text="Stella Verba", font="Rubik Bubbles")
label.pack()
button = tk.Button(root, text="Bye", width = 25,command=root.destroy)
button.place(relx=0.425,rely=0.5)

image = ImageTk
root.mainloop()