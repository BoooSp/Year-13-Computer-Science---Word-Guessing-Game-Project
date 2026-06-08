import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path
from tkinter import mainloop

from PIL.ImageOps import expand
from PIL.ImageTk import PhotoImage
import pyglet
import ctypes
import os
import random
import json

from wordle import StellaVerbaGamePage


class Verba:
    def __init__(self, root):
        self.root = root
#the page thingy with self
        self.Home = tk.Frame(root)
        self.Difficulty = tk.Frame(root)
        self.GameH = tk.Frame(root)
        self.GameM = tk.Frame(root)
        self.GameE = tk.Frame(root)


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
        self.assets={"darkmode":{"background":"dbg.png","star":"dstar.png","moon":"dmoon.png","sun":"dsun.png","bgc":"#363636","bgt":"white","descbg":"#5D5D5D","descfg":"#FFFFFF"},
                     "lightmode":{"background":"lbg.png","star":"lstar.png","moon":"lmoon.png","sun":"lsun.png","bgc":"#DBDBDB","bgt":"#2E2E2E","descbg":"#706F6F","descfg":"#FFFFFF"}}

        # background image for my home page and the directory for it, side note - remember to leave bg in top of code so that it would be placed behind other functions
        data = self.assets[self.mode]
        self.Homebg = PhotoImage(file=str(self.img / data["background"]))
        self.star = PhotoImage(file=str(self.img / data["star"]))
        self.sun = PhotoImage(file=str(self.img / data["sun"]))
        self.moon = PhotoImage(file=str(self.img / data["moon"]))
        #code that allows initially for my code to have the hover function as the function didnt work when i havent switched the mode
        if self.mode =="darkmode":
             self.starhover = PhotoImage(file=str(self.img/"hstar.png"))
        self.starhover = PhotoImage(file=str(self.img / "hstar.png"))

        #Code for my title in the home page
        self.my_label = tk.Label(self.Home, image=self.Homebg, bd=0,bg=data["bgc"],fg=data["bgt"]) #remember what the code purpose was (maybe text idk)
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)
        # The code for the "StellaVerba text in homgpage
        self.home_label = tk.Label(self.Home, text="Stella Verba", font=("Rubik Bubbles",33),bg=data["bgc"],fg=data["bgt"] )
        self.home_label.pack()

#Code for the star button and the hover effect and stuff
#Code for the button in the home page that leads the user to the difficulty selection page - and also make
# it so that it doesn't have any brick effect and when you hover over the button it makes a pointer effect to indicate it's a button
        self.starb = tk.Label(self.Home, image=self.star, bd=0, cursor="hand2",bg=data["bgc"], text="PLAY")
        self.starb.place(relx=0.425, rely=0.5, relwidth=0.15, relheight=0.2)
        def hover_in(event):self.starb.config(image=self.starhover)
        def hover_out(event):self.starb.config(image=self.star)
        self.starb.bind("<Enter>", hover_in)
        self.starb.bind("<Leave>", hover_out)
        self.starb.bind("<ButtonRelease-1>", lambda e: self.Home_Diff())

        #Code for the sun and moon buttons which is the buttons for the light and dark mode
        #releif makes it so that there is no more button brick effect and cursor 2 makes the cursor point when it hovers over the button
        self.lightbutton = tk.Button(self.Home, image=self.sun,command=lambda: self.load_button("lightmode"), bd=0, highlightthickness=0, relief="flat", cursor="hand2",bg=data["bgc"],activebackground=data["bgc"])
        self.lightbutton.place(relx=0.25, rely=0.05)
        #code so that there is an image that would be played for a hover effect before the user click on the button to make it more aesthetic


        self.darkbutton = tk.Button(self.Home, image=self.moon,command=lambda: self.load_button("darkmode"),bd=0, highlightthickness=0, relief="flat", cursor="hand2",bg=data["bgc"],activebackground=data["bgc"])
        self.darkbutton.place(relx=0.70, rely=0.05)

        #Design for Difficulty Selection Page
        self.diff_bg = tk.Label(self.Difficulty, image=self.Homebg, bd=0)
        self.diff_bg.place(x=0, y=0, relwidth=1, relheight=1)
        self.diff_label = tk.Label(self.Difficulty, text="DIFFICULTY SELECTION", font=("Rubik Bubbles",50),bg=data["bgc"],fg=data["bgt"]  )
        self.diff_label.pack()

#button for the hard mode difficulty in the difficluty page
        self.hardbutton = tk.Button(self.Difficulty, text="Hard", width = 25,command=lambda:self.Diff_Game("hard"),bg="#C7141F", font=("Inter",20,"bold"))
        self.hardbutton.place(relx=0.2,rely=0.6,relwidth=0.1,relheight=0.1)
        #Code for the info of each difficulty
        self.harddesc = tk.Label(self.Difficulty,font=("Inter",12,"bold"),justify="left",bg=data["descbg"],fg=data["descfg"],text = "6 letter combination with more objectively harder terms\nHardest difficulty out of the three modes")
        self.harddesc.place(relx=0.35, rely=0.6, relwidth=0.4, relheight=0.1)
        self.hardbutton.bind("<Enter>", lambda e: self.hardbutton.config(bg="#D81212"))
        self.hardbutton.bind("<Leave>", lambda e: self.hardbutton.config(bg="#C7141F"))

        self.mediumbutton = tk.Button(self.Difficulty, text="Medium", width = 25,command=lambda:self.Diff_Game("medium"),bg="#C27E01", font=("Inter",20,"bold"))
        self.mediumbutton.place(relx=0.2, rely=0.4, relwidth=0.1, relheight=0.1)
        self.meddesc = tk.Label(self.Difficulty, font=("Inter", 12, "bold"), justify="left", bg=data["descbg"],fg=data["descfg"],text = "5 letter combination with more objectively moderate terms\nMedium difficulty out of the three modes")
        self.meddesc.place(relx=0.35, rely=0.4, relwidth=0.4, relheight=0.1)
        self.mediumbutton.bind("<Enter>", lambda e: self.mediumbutton.config(bg="#D98F06"))
        self.mediumbutton.bind("<Leave>", lambda e: self.mediumbutton.config(bg="#C27E01"))

        self.easybutton = tk.Button(self.Difficulty, text="Easy", width = 25,command=lambda:self.Diff_Game("easy"),bg="#558B36", font=("Inter",20,"bold"))
        self.easydesc = tk.Label(self.Difficulty, font=("Inter", 12, "bold"), justify="left", bg=data["descbg"],fg=data["descfg"],text = "4 letter combination with more objectively simpler terms\nEasiest difficulty out of the three modes")
        self.easydesc.place(relx=0.35, rely=0.2, relwidth=0.4, relheight=0.1)
        self.easybutton.place(relx=0.2, rely=0.2, relwidth=0.1, relheight=0.1)
        self.easybutton.bind("<Enter>", lambda e: self.easybutton.config(bg="#68AF3E"))
        self.easybutton.bind("<Leave>", lambda e: self.easybutton.config(bg="#558B36"))


        self.Home.pack(fill="both", expand=True)

#the code that allows to create the actual page or smt
    def Home_Page(self):
        self.Home.pack(fill="both", expand=True)
        self.Difficulty.pack(fill="both", expand=True)

    def Home_Diff(self):
        self.Home.pack_forget()
        self.Difficulty.pack(fill="both", expand=True)

#change this so that it connnects to the code of the wordle page FINALLY
    def Diff_Game(self,difficulty):
        self.Difficulty.pack_forget()
        if hasattr(self,"gameframeofwordle") and self.gameframeofwordle.winfo_exists():
            self.gameframeofwordle.destroy()
        self.gameframeofwordle=tk.Frame(self.root,bg="white")
        self.gameframeofwordle.pack(fill="both",expand=True)
        StellaVerbaGamePage(self.gameframeofwordle,difficulty,self)

    def displayingtheresults(self,won,word,guesses):
        if hasattr(self,"gameframeofwordle"):
            self.gameframeofwordle.destroy()
        self.Home.pack(fill="both",expand=True)





#Things to do - connec the wordle page, add single line box that shows answers,

    def load_button(self,mode):
        self.mode=mode
        data=self.assets[mode]
        self.Homebg = PhotoImage(file=str(self.img / data["background"])) #The bg for home and diff
        self.star = PhotoImage(file=str(self.img / data["star"])) #star img of button
        self.sun = PhotoImage(file=str(self.img / data["sun"])) #sun img of button
        self.moon = PhotoImage(file=str(self.img / data["moon"])) #moon img button
        self.starhover = PhotoImage(file=str(self.img / "hstar.png")) #the hover image that it switches to
        #The actual pages
        self.Home.config(bg=data["bgc"])
        self.Difficulty.config(bg=data["bgc"])
        self.diff_bg.config(image=self.Homebg,bg=data["bgc"],fg=data["bgt"] )
        #all the labels and text
        self.my_label.config(image=self.Homebg, bg=data["bgc"])
        self.home_label.config(bg=data["bgc"], fg=data["bgt"])
        self.diff_label.config(bg=data["bgc"], fg=data["bgt"])
        #The buttons for the home page eg the sun the star and the moon
        self.starb.config(image=self.star,bg=data["bgc"])
        self.lightbutton.config(image=self.sun,bg=data["bgc"],activebackground=data["bgc"])
        self.darkbutton.config(image=self.moon,bg=data["bgc"],activebackground=data["bgc"])

root=tk.Tk()
app=Verba(root)
root.mainloop()




