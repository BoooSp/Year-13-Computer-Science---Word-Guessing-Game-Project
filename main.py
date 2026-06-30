import tkinter as tk
from PIL import ImageTk, Image
from pathlib import Path
from PIL.ImageTk import PhotoImage
import pyglet
from game import StellaVerbaGamePage,StellaVerbaResultPage


class Verba:
    def __init__(self, root):
        self.root = root
        #the page thingy with self
        self.Home = tk.Frame(root)
        self.Difficulty = tk.Frame(root)


        #the shortcut thingy that makes it so that it doesn't rely on my desktop files
        self.shortcut = Path(__file__).parent
        self.img = self.shortcut / "images"
        self.font = self.shortcut / "Fonts"


        # The title of the game in the bar thingy on top of the normal interface page
        self.root.title("StellaVerba")
        # The size of my page
        self.root.geometry("1200x737")
        # Prevent the width or the height being changed by users to prevent any errors from decreasing or increasing size of the screen
        self.root.resizable(False, False)

        #this is so that I can like make two codes so that like I am able to do the light and dark mode things
        self.mode="darkmode"
        self.assets={"darkmode":{"background":"dbg.png","star":"dstar.png","moon":"dmoon.png","sun":"dsun.png","bgc":"#363636","bgt":"white","descbg":"#5D5D5D","descfg":"#FFFFFF","bgt2":"#FFFFAE","bgc2":"#363636"},
                     "lightmode":{"background":"lbg.png","star":"lstar.png","moon":"lmoon.png","sun":"lsun.png","bgc":"#DBDBDB","bgt":"#2E2E2E","descbg":"#706F6F","descfg":"#FFFFFF","bgt2":"#2E2E2E","bgc2":"#DBDBDB"}}

        # this makes it so that I am able to like link all the font thingy and make it work in windows/the cheatsheet for easy acess
        for font_file in self.font.glob("*.ttf"):
            pyglet.font.add_file((str(font_file)))
        # background image for my home page and the directory for it, side note - remember to leave bg in top of code so that it would be placed behind other functions
        data = self.assets[self.mode]
        self.Home_background = PhotoImage(file=str(self.img / data["background"]))
        self.star = PhotoImage(file=str(self.img / data["star"]))
        self.sun = PhotoImage(file=str(self.img / data["sun"]))
        self.moon = PhotoImage(file=str(self.img / data["moon"]))
        #code that allows initially for my code to have the hover function as the function didnt work when i havent switched the mode
        if self.mode =="darkmode":
             self.starhover = PhotoImage(file=str(self.img/"hstar.png"))
        self.starhover = PhotoImage(file=str(self.img / "hstar.png"))

        #the background that holds everything together
        self.home_background = tk.Label(self.Home, image=self.Home_background, bd=0,bg=data["bgc2"],fg=data["bgt"])
        self.home_background.place(x=0, y=0, relwidth=1, relheight=1)
        # The code for the "StellaVerba text in homgpage
        self.hometitlepart1 = tk.Label(self.Home, text="Stella", font=("Italianno",80),bg=data["bgc"],fg=data["bgt"] )
        self.hometitlepart1.place(relx=0.34, rely=0.01)
        self.hometitlepart2 = tk.Label(self.Home, text="Verba", font=("Rubik Bubbles",45),bg=data["bgc"],fg=data["bgt"] )
        self.hometitlepart2.place(relx=0.5, rely=0.05)

        #Code for the star button and the hover effect and stuff
        #Code for the button in the home page that leads the user to the difficulty selection page - and also make
        # it so that it doesn't have any brick effect and when you hover over the button it makes a pointer effect to indicate it's a button
        self.star_button = tk.Label(self.Home, image=self.star, bd=0, cursor="hand2",bg=data["bgc"], text="PLAY")
        self.star_button.place(relx=0.425, rely=0.5, relwidth=0.15, relheight=0.2)
        def hover_in(event):self.star_button.config(image=self.starhover)
        def hover_out(event):self.star_button.config(image=self.star)
        self.star_button.bind("<Enter>", hover_in)
        self.star_button.bind("<Leave>", hover_out)
        self.star_button.bind("<ButtonRelease-1>", lambda e: self.Home_Diff())

        #Code for the sun and moon buttons which is the buttons for the light and dark mode
        #releif makes it so that there is no more button brick effect and cursor 2 makes the cursor point when it hovers over the button
        self.lightbutton = tk.Button(self.Home, image=self.sun,command=lambda: self.load_button("lightmode"), bd=0, highlightthickness=0, relief="flat", cursor="hand2",bg=data["bgc"],activebackground=data["bgc"])
        self.lightbutton.place(relx=0.25, rely=0.05)
        #code so that there is an image that would be played for a hover effect before the user click on the button to make it more aesthetic


        self.darkbutton = tk.Button(self.Home, image=self.moon,command=lambda: self.load_button("darkmode"),bd=0, highlightthickness=0, relief="flat", cursor="hand2",bg=data["bgc"],activebackground=data["bgc"])
        self.darkbutton.place(relx=0.69, rely=0.07)

        #Design for Difficulty Selection Page
        self.difficulty_background = tk.Label(self.Difficulty, image=self.Home_background, bd=0)
        self.difficulty_background.place(x=0, y=0, relwidth=1, relheight=1)
        self.difficultytitles = tk.Label(self.Difficulty, text="DIFFICULTY SELECTION", font=("Rubik Bubbles",50),bg=data["bgc"],fg=data["bgt"]  )
        self.difficultytitles.pack()

        #button for the hard mode difficulty in the difficluty page
        self.Hard_button = tk.Button(self.Difficulty, text="Hard", width = 25,command=lambda:self.Diff_Game("hard"),bg="#C7141F", font=("Inter",20,"bold"))
        self.Hard_button.place(relx=0.2,rely=0.6,relwidth=0.1,relheight=0.1)
        #Code for the info of each difficulty
        self.Hard_Mode_Word_description = tk.Label(self.Difficulty,font=("Inter",12,"bold"),justify="left",bg=data["descbg"],fg=data["descfg"],text = "6 letter combination with more objectively harder terms\nHardest difficulty out of the three modes")
        self.Hard_Mode_Word_description.place(relx=0.35, rely=0.6, relwidth=0.4, relheight=0.1)
        #added overlay effect on the button when the user hovers over the button
        self.Hard_button.bind("<Enter>", lambda e: self.Hard_button.config(bg="#D81212"))
        self.Hard_button.bind("<Leave>", lambda e: self.Hard_button.config(bg="#C7141F"))
        #code for the medium button
        self.Medium_button = tk.Button(self.Difficulty, text="Medium", width = 25,command=lambda:self.Diff_Game("medium"),bg="#C27E01", font=("Inter",20,"bold"))
        self.Medium_button.place(relx=0.2, rely=0.4, relwidth=0.1, relheight=0.1)
        self.Medium_Mode_Word_description = tk.Label(self.Difficulty, font=("Inter", 12, "bold"), justify="left", bg=data["descbg"],fg=data["descfg"],text = "5 letter combination with more objectively moderate terms\nMedium difficulty out of the three modes")
        self.Medium_Mode_Word_description.place(relx=0.35, rely=0.4, relwidth=0.4, relheight=0.1)
        self.Medium_button.bind("<Enter>", lambda e: self.Medium_button.config(bg="#D98F06"))
        self.Medium_button.bind("<Leave>", lambda e: self.Medium_button.config(bg="#C27E01"))
        #code for the easy button
        self.Easy_button = tk.Button(self.Difficulty, text="Easy", width = 25,command=lambda:self.Diff_Game("easy"),bg="#558B36", font=("Inter",20,"bold"))
        self.Easy_Mode_Word_description = tk.Label(self.Difficulty, font=("Inter", 12, "bold"), justify="left", bg=data["descbg"],fg=data["descfg"],text = "4 letter combination with more objectively simpler terms\nEasiest difficulty out of the three modes")
        self.Easy_Mode_Word_description.place(relx=0.35, rely=0.2, relwidth=0.4, relheight=0.1)
        self.Easy_button.place(relx=0.2, rely=0.2, relwidth=0.1, relheight=0.1)
        self.Easy_button.bind("<Enter>", lambda e: self.Easy_button.config(bg="#68AF3E"))
        self.Easy_button.bind("<Leave>", lambda e: self.Easy_button.config(bg="#558B36"))
        self.Go_back_to_home_page=tk.Button(self.Difficulty,text="<-- Back", font = ("Inter", 14,"bold"), command = self.Go_back, bg = "#84817f", fg = "white", bd = 0, cursor = "hand2")
        self.Go_back_to_home_page.place(x=20, y=20)
        self.Home.pack(fill="both", expand=True)

    #the code that allows the home page to appear
    def Home_Page(self):
        self.Home.pack(fill="both", expand=True)
    #def code that allows the difficulty page to appear
    def Home_Diff(self):
        self.Home.pack_forget()
        self.Difficulty.pack(fill="both", expand=True)

        #change this so that it connects to the code of the wordle page
    def Diff_Game(self,difficulty):
        self.Difficulty.pack_forget()
        if hasattr(self,"frameofgamepage") and self.frameofgamepage.winfo_exists():
            self.frameofgamepage.destroy()
        self.frameofgamepage=tk.Frame(self.root,bg="white")
        self.frameofgamepage.pack(fill="both",expand=True)
        StellaVerbaGamePage(self.frameofgamepage,difficulty,self)
    #code that displays the result page itself
    def displayingtheresults(self,won,word,guesses):
        if hasattr(self,"resultframe") and self.resultframe.winfo_exists():
            self.resultframe.destroy()
        if hasattr(self,"frameofgamepage") and self.frameofgamepage.winfo_exists():
            self.frameofgamepage.destroy()
        self.Difficulty.pack(fill="both",expand=True)

    #code that displays the pop up of the result page
    def showresultpage(self, won, word, guesses):
        if hasattr(self, "frameofgamepage") and self.frameofgamepage.winfo_exists():
            self.frameofgamepage.destroy()
        self.resultframe = tk.Frame(self.root, bg="white")
        self.resultframe.pack(fill="both", expand=True)
        StellaVerbaResultPage(self.resultframe, won, word, guesses, self)

    #Things to do - connec the wordle page, add single line box that shows answers,
    def load_button(self,mode):
        self.mode=mode
        data=self.assets[mode]
        self.Home_background = PhotoImage(file=str(self.img / data["background"])) #The bg for home and diff
        self.star = PhotoImage(file=str(self.img / data["star"])) #star img of button
        self.sun = PhotoImage(file=str(self.img / data["sun"])) #sun img of button
        self.moon = PhotoImage(file=str(self.img / data["moon"])) #moon img button
        self.starhover = PhotoImage(file=str(self.img / "hstar.png")) #the hover image that it switches to
        #The actual pages
        self.Home.config(bg=data["bgc"])
        self.Difficulty.config(bg=data["bgc"])
        self.difficulty_background.config(image=self.Home_background,bg=data["bgc"],fg=data["bgt"] )
        #all the labels and text
        self.home_background.config(image=self.Home_background, bg=data["bgc"])
        self.hometitlepart2.config(bg=data["bgc"], fg=data["bgt"])
        self.hometitlepart1.config(bg=data["bgc2"], fg=data["bgt2"])
        self.difficultytitles.config(bg=data["bgc"], fg=data["bgt"])
        #The buttons for the home page eg the sun the star and the moon
        self.star_button.config(image=self.star,bg=data["bgc"])
        self.lightbutton.config(image=self.sun,bg=data["bgc"],activebackground=data["bgc"])
        self.darkbutton.config(image=self.moon,bg=data["bgc"],activebackground=data["bgc"])

    def Go_back(self):
        self.Difficulty.pack_forget()
        self.Home.pack(fill="both", expand=True)

    def Go_back_to_difficulty_page(self):
        Go_Back_pop_up = tk.Toplevel(self.root)
        Go_Back_pop_up.geometry("400x250")
        Go_Back_pop_up.resizable(False, False)
        Go_Back_pop_up.configure(bg="#2E2E2E")
        Go_Back_pop_up.transient(self.root)
        Go_Back_pop_up.grab_set()
        tk.Label(Go_Back_pop_up, text="Leave Game Page?", font=("Rubik Bubbles", 20), bg="#2E2E2E", fg="white").pack(pady=(20, 10))
        tk.Label(Go_Back_pop_up,text="Leave current game page and return\nto difficulty selection?\n\n(Leaving will lose your current progress)",font=("Inter", 11), bg="#2E2E2E", fg="#AAAAAA").pack()
    #if the user had pressed yes it would destroy the game page and then lead back to the difficulty page
        def yes():
            Go_Back_pop_up.destroy()
            if hasattr(self, "frameofgamepage"):
                self.frameofgamepage.destroy()
            self.Difficulty.pack(fill="both", expand=True)
            #when the user presses no in the message box it would just destroy the frame
        def no():
            Go_Back_pop_up.destroy()
        buttonframe = tk.Frame(Go_Back_pop_up, bg="#2E2E2E")
        buttonframe.pack(pady=20)
        tk.Button(buttonframe, text="Leave", bg="#C7141F", fg="white", font=("Inter", 12, "bold"), bd=0,command=yes).pack(side="left", padx=10)
        tk.Button(buttonframe, text="Stay", bg="#558B36", fg="white", font=("Inter", 12, "bold"), bd=0,command=no).pack(side="left", padx=10)

root=tk.Tk()
app=Verba(root)
root.mainloop()
