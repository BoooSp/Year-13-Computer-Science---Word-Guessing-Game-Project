import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path
from tkinter import mainloop
from PIL.ImageTk import PhotoImage
import pyglet
import ctypes
import os


class Verba:
    def __init__(self, root):
        self.root = root
#the page thingy with self
        self.Home = tk.Frame(root)
        self.Difficulty = tk.Frame(root)
        self.Game = tk.Frame(root)
#the shortcut thingy that makes it so that it doesn't rely on my desktop files
        self.shortcut = Path(__file__).parent
        self.img = self.shortcut / "images"
        self.font = self.shortcut / "Fonts"
#all the font files dir connected with the sef font thingy to make my life easier
        pyglet.font.add_file(str(self.font / "Inter-Italic-VariableFont_opsz,wght.ttf"))
        pyglet.font.add_file(str(self.font / "Italianno-Regular.ttf"))
        pyglet.font.add_file(str(self.font / "RubikBubbles-Regular.ttf"))
        pyglet.font.add_file(str(self.font / "RubikPuddles-Regular.ttf"))

    #this makes it so that I am able to like link all the font thingy and make it work in windows/the cheatsheet for easy acess
        for font_file in os.listdir(self.font):
            if font_file.endswith(".ttf"):
                ctypes.windll.gdi32.AddFontResourceExW(str(self.font / font_file),0x10,0)

            #The title of the game in the bar thingy on top of the normal interface page
            self.root.title("StellaVerba")
            #The size of my page
            self.root.geometry("1200x737")
            #Prevent the width or the height being changed by users to prevent any errors from decreasing or increasing size of the screen
            self.root.resizable(False,False)
            #background image for my home page and the directory for it, side note - remember to leave bg in top of code so that it would be placed behind other functions
            self.HomePagebg = PhotoImage(file = (str(self.img/"backstar.png")))
            self.star = PhotoImage(file=(str(self.img / "dstar.png")))

#Code for my title in the home page
        my_label = tk.Label(self.Home, image=self.HomePagebg, bd=0)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)
        my_label = tk.Label(self.Home, text="Stella Verba", font=("Rubik Bubbles",33),bg="#363636")
        my_label.pack()

#Code for the button in the home page that leads the user to the difficulty selection page
        button = tk.Button(self.Home, text="Bye", image=self.star,width = 25,command=self.Home_Diff,bg="#363636")
        button.place(relx=0.425,rely=0.5, relwidth=0.15, relheight=0.2)

#Design for Difficulty Selection Page
        my_label = tk.Label(self.Difficulty, image=self.HomePagebg, bd=0)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)
        my_label = tk.Label(self.Difficulty, text="DIFFICULTY SELECTION", font=("Rubik Bubbles",50),bg="#363636" )
        my_label.pack()

        button = tk.Button(self.Difficulty, text="Hard", width = 25,command=self.Diff_Game,bg="red")
        button.place(relx=0.425,rely=0.5)

        self.Home.pack(fill="both", expand=True)

#the code that allows to create the actual page or smt
    def Home_Page(self):
        self.Home.pack(fill="both", expand=True)
        self.Difficulty.pack(fill="both", expand=True)

    def Home_Diff(self):
        self.Home.pack_forget()
        self.Difficulty.pack(fill="both", expand=True)

    def Diff_Game(self):
        self.Difficulty.pack_forget()
        self.Game.pack(fill="both", expand=True)




root=tk.Tk()
ap=Verba(root)
root.mainloop()





