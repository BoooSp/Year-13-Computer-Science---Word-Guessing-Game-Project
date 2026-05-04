import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path

from tkinter import mainloop

from PIL.ImageTk import PhotoImage

root = tk.Tk()
#The title of the game in the bar thingy on top of the normal interface page
root.title("StellaVerba")
#The size of my page
root.geometry("1200x800")
#Prevent the width or the height being changed by users to prevent any errors from decreasing or increasing size of the screen
root.resizable(False,False)
bg = PhotoImage(file = "C:/Users/22488/PycharmProjects/Year-13-Computer-Science---Word-Guessing-Game-Project/Images/starbackground.png")

my_label = tk.Label(root, image=bg, bd=0)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
my_label = tk.Label(root, text="Stella Verba", font="Ariel")
my_label.pack()
button = tk.Button(root, text="Bye", width = 25,command=root.destroy)
button.place(relx=0.425,rely=0.5)
image = ImageTk
root.mainloop()