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

        # The title of the game in the bar thingy on top of the normal interface page
        self.root.title("StellaVerba")
        # The size of my page
        self.root.geometry("1200x737")
        # Prevent the width or the height being changed by users to prevent any errors from decreasing or increasing size of the screen
        self.root.resizable(False, False)

        #this is so that I can like make two codes so that like I am able to do the light and dark mode things
        self.mode="darkmode"
        self.assets={"darkmode":{"background":"backstar.png","star":"dstar.png","moon":"dmoon.png","sun":"dsun.png"},
                     "lightmode":{"background":"lbg.png","star":"lstar.png","moon":"lmoon.png","sun":"lsun.png"}}

        # background image for my home page and the directory for it, side note - remember to leave bg in top of code so that it would be placed behind other functions
        data = self.assets[self.mode]
        self.HomePagebg = PhotoImage(file=str(self.img / data["background"]))
        self.star = PhotoImage(file=str(self.img / data["star"]))
        self.sun = PhotoImage(file=str(self.img / data["sun"]))
        self.moon = PhotoImage(file=str(self.img / data["moon"]))

        #this makes it so that I am able to like link all the font thingy and make it work in windows/the cheatsheet for easy acess
        if os.name == "nt":
                for font_file in os.listdir(self.font):
                    if font_file.endswith(".ttf"):
                        ctypes.windll.gdi32.AddFontResourceExW(str(self.font / font_file),0x10,0)


        #Code for my title in the home page
        self.my_label = tk.Label(self.Home, image=self.HomePagebg, bd=0)
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.home_label = tk.Label(self.Home, text="Stella Verba", font=("Rubik Bubbles",33),bg="#363636")
        self.home_label.pack()

#Code for the button in the home page that leads the user to the difficulty selection page - and also make
# it so that it doesn't have any brick effect and when you hover over the button it makes a pointer effect to indicate it's a button
        self.starb = tk.Label(self.Home, image=self.star, bg="#363636", bd=0, cursor="hand2")
        self.starb.place(relx=0.425, rely=0.5, relwidth=0.15, relheight=0.2)
        self.starb.bind("<ButtonRelease-1>", lambda e: self.Home_Diff())

        #Code for the sun and moon buttons which is the buttons for the light and dark mode
        self.lightbutton = tk.Button(self.Home, image=self.sun,command=lambda: self.load_button("lightmode"), bd=0, highlightthickness=0, relief="flat", cursor="hand2")
        self.lightbutton.place(relx=0.25, rely=0.05)

        self.darkbutton = tk.Button(self.Home, image=self.moon,command=lambda: self.load_button("darkmode"),bd=0, highlightthickness=0, relief="flat", cursor="hand2")
        self.darkbutton.place(relx=0.70, rely=0.05)

        #Design for Difficulty Selection Page
        self.diff_bg = tk.Label(self.Difficulty, image=self.HomePagebg, bd=0)
        self.diff_bg.place(x=0, y=0, relwidth=1, relheight=1)
        self.diff_label = tk.Label(self.Difficulty, text="DIFFICULTY SELECTION", font=("Rubik Bubbles",50),bg="#363636" )
        self.diff_label.pack()
#button for the hard mode difficulty in the difficluty page
        button = tk.Button(self.Difficulty, text="Hard", width = 25,command=self.Diff_Game,bg="#CE2727", font=("Inter",25))
        button.place(relx=0.25,rely=0.2,relwidth=0.1,relheight=0.1)


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

    def load_button(self,mode):
        self.mode=mode
        self.HomePagebg = PhotoImage(file=str(self.img /data["background"]))
        self.star = PhotoImage(file=str(self.img / data["star"]))
        self.sun = PhotoImage(file=str(self.img / data["sun"]))
        self.moon = PhotoImage(file=str(self.img / data["moon"]))
        self.bg_label.config(image=self.HomePagebg)
        self.bg_label.image = self.HomePagebg
        self.diff_bg.config(image=self.HomePagebg)
        self.diff_bg.image = self.HomePagebg
        self.starb.config(image=self.star)
        self.starb.image = self.star
        self.lightbutton.config(image=self.sun)
        self.darkbutton.config(image=self.moon)


root=tk.Tk()
app=Verba(root)
root.mainloop()





