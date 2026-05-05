import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path
from tkinter import mainloop
from PIL.ImageTk import PhotoImage
import pyglet
from tkinter import Tk, Label
from tkextrafont import Font

pyglet.options['win32_gdi_font'] = True
pyglet.font.add_file('Inter.ttf')
my_font = Font(file="C:/Users/22488/PycharmProjects/Year-13-Computer-Science---Word-Guessing-Game-Project/Fonts/Inter.ttf", family="Inter", size=20)

root = tk.Tk()
Home=tk.Frame(root)
Difficulty=tk.Frame(root)
Game=tk.Frame(root)

def Home_Diff():
    Home.pack_forget()
    Difficulty.pack(fill="both", expand=True)

#The title of the game in the bar thingy on top of the normal interface page
root.title("StellaVerba")
#The size of my page
root.geometry("1200x737")
#Prevent the width or the height being changed by users to prevent any errors from decreasing or increasing size of the screen
root.resizable(False,False)
#background image for my home page and the directory for it, side note - remember to leave bg in top of code so that it would be placed behind other functions
HomePagebg = PhotoImage(file = "C:/Users/22488/PycharmProjects/Year-13-Computer-Science---Word-Guessing-Game-Project/Images/backstar.png")

#Home Page
#Code for my title in the home page
my_label = tk.Label(Home, image=HomePagebg, bd=0)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
my_label = tk.Label(Home, text="Stella Verba", font=("Times New Roman",23))
my_label.pack()

#Code for the button in the home page that leads the user to the difficulty selection page
button = tk.Button(Home, text="Bye", width = 25,command=Home_Diff)
button.place(relx=0.425,rely=0.5)



def Diff_Game():
    Difficulty.pack_forget()
    Game.pack(fill="both", expand=True)


#Design for Difficulty Selection Page
my_label = tk.Label(Difficulty, image=HomePagebg, bd=0)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
my_label = tk.Label(Difficulty, text="Difficulty Selection", Font=my_font )
my_label.pack()

button = tk.Button(Difficulty, text="Hard", width = 25,command=Diff_Game)
button.place(relx=0.425,rely=0.5)


Home.pack(fill="both",expand=True)
image = ImageTk
root.mainloop()