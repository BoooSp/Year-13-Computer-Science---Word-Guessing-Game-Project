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
        self.mode="dark_mode"
        self.assets={"dark_mode":{"background":"dbg.png","star":"dstar.png","moon":"dmoon.png","sun":"dsun.png","bgc":"#363636","bgt":"white","description_box_bg":"#5D5D5D","description_box_font":"#FFFFFF","bgt2":"#FFFFAE","bgc2":"#363636"},
                     "light_mode":{"background":"lbg.png","star":"lstar.png","moon":"lmoon.png","sun":"lsun.png","bgc":"#DBDBDB","bgt":"#2E2E2E","description_box_bg":"#706F6F","description_box_font":"#FFFFFF","bgt2":"#2E2E2E","bgc2":"#DBDBDB"}}

        # this makes it so that I am able to like link all the font thingy and make it work in windows/the cheatsheet for easy access
        for font_file in self.font.glob("*.ttf"):
            pyglet.font.add_file((str(font_file)))
        # background image for my home page and the directory for it, side note - remember to leave bg in top of code so that it would be placed behind other functions
        data = self.assets[self.mode]
        self.Home_background = PhotoImage(file=str(self.img / data["background"]))
        self.star = PhotoImage(file=str(self.img / data["star"]))
        self.sun = PhotoImage(file=str(self.img / data["sun"]))
        self.moon = PhotoImage(file=str(self.img / data["moon"]))
        #code that allows initially for my code to have the hover function as the function didn't work when I haven't switched the mode
        if self.mode =="dark_mode":
             self.hovering_over_star_button = PhotoImage(file=str(self.img/"hstar.png"))
        self.hovering_over_star_button = PhotoImage(file=str(self.img / "hstar.png"))

        #the background that holds everything together
        self.home_background = tk.Label(self.Home, image=self.Home_background, bd=0,bg=data["bgc2"],fg=data["bgt"])
        self.home_background.place(x=0, y=0, relwidth=1, relheight=1)
        # The code for the "StellaVerba" text in home page
        self.home_title_part_1 = tk.Label(self.Home, text="Stella", font=("Italianno",80),bg=data["bgc"],fg=data["bgt"] )
        self.home_title_part_1.place(relx=0.34, rely=0.01)
        self.home_title_part_2 = tk.Label(self.Home, text="Verba", font=("Rubik Bubbles",45),bg=data["bgc"],fg=data["bgt"] )
        self.home_title_part_2.place(relx=0.5, rely=0.05)

        #Code for the star button and the hover effect and stuff
        #Code for the button in the home page that leads the user to the difficulty selection page - and also make
        # it so that it doesn't have any brick effect and when you hover over the button it makes a pointer effect to indicate it's a button
        self.star_button = tk.Label(self.Home, image=self.star, bd=0, cursor="hand2",bg=data["bgc"], text="PLAY")
        self.star_button.place(relx=0.425, rely=0.5, relwidth=0.15, relheight=0.2)
        def hover_in(event):self.star_button.config(image=self.hovering_over_star_button)
        def hover_out(event):self.star_button.config(image=self.star)
        self.star_button.bind("<Enter>", hover_in)
        self.star_button.bind("<Leave>", hover_out)
        self.star_button.bind("<ButtonRelease-1>", lambda e: self.home_page_to_difficulty_page())

        #Code for the sun and moon buttons which is the buttons for the light and dark mode
        #releif makes it so that there is no more button brick effect and cursor 2 makes the cursor point when it hovers over the button
        self.lightbutton = tk.Button(self.Home, image=self.sun,command=lambda: self.load_button("light_mode"), bd=0, highlightthickness=0, relief="flat", cursor="hand2",bg=data["bgc"],activebackground=data["bgc"])
        self.lightbutton.place(relx=0.25, rely=0.05)
        #code so that there is an image that would be played for a hover effect before the user click on the button to make it more aesthetic


        self.darkbutton = tk.Button(self.Home, image=self.moon,command=lambda: self.load_button("dark_mode"),bd=0, highlightthickness=0, relief="flat", cursor="hand2",bg=data["bgc"],activebackground=data["bgc"])
        self.darkbutton.place(relx=0.69, rely=0.07)

        #Design for Difficulty Selection Page
        self.difficulty_background = tk.Label(self.Difficulty, image=self.Home_background, bd=0)
        self.difficulty_background.place(x=0, y=0, relwidth=1, relheight=1)
        self.difficulty_selection_page_title = tk.Label(self.Difficulty, text="DIFFICULTY SELECTION", font=("Rubik Bubbles",50),bg=data["bgc"],fg=data["bgt"]  )
        self.difficulty_selection_page_title.pack()

        #button for the hard mode difficulty in the difficulty page
        self.Hard_button = tk.Button(self.Difficulty, text="Hard", width = 25,command=lambda:self.difficulty_page_to_game_page("hard"),bg="#C7141F", font=("Inter",20,"bold"))
        self.Hard_button.place(relx=0.2,rely=0.6,relwidth=0.1,relheight=0.1)
        #Code for the info of each difficulty
        self.Hard_Mode_Word_description = tk.Label(self.Difficulty,font=("Inter",12,"bold"),justify="left",bg=data["description_box_bg"],fg=data["description_box_font"],text = "6 letter combination with more objectively harder terms\nHardest difficulty out of the three modes")
        self.Hard_Mode_Word_description.place(relx=0.35, rely=0.6, relwidth=0.4, relheight=0.1)
        #added overlay effect on the button when the user hovers over the button
        self.Hard_button.bind("<Enter>", lambda e: self.Hard_button.config(bg="#D81212"))
        self.Hard_button.bind("<Leave>", lambda e: self.Hard_button.config(bg="#C7141F"))
        #code for the medium button
        self.Medium_button = tk.Button(self.Difficulty, text="Medium", width = 25,command=lambda:self.difficulty_page_to_game_page("medium"),bg="#C27E01", font=("Inter",20,"bold"))
        self.Medium_button.place(relx=0.2, rely=0.4, relwidth=0.1, relheight=0.1)
        self.Medium_Mode_Word_description = tk.Label(self.Difficulty, font=("Inter", 12, "bold"), justify="left", bg=data["description_box_bg"],fg=data["description_box_font"],text = "5 letter combination with more objectively moderate terms\nMedium difficulty out of the three modes")
        self.Medium_Mode_Word_description.place(relx=0.35, rely=0.4, relwidth=0.4, relheight=0.1)
        self.Medium_button.bind("<Enter>", lambda e: self.Medium_button.config(bg="#D98F06"))
        self.Medium_button.bind("<Leave>", lambda e: self.Medium_button.config(bg="#C27E01"))
        #code for the easy button
        self.Easy_button = tk.Button(self.Difficulty, text="Easy", width = 25,command=lambda:self.difficulty_page_to_game_page("easy"),bg="#558B36", font=("Inter",20,"bold"))
        self.Easy_Mode_Word_description = tk.Label(self.Difficulty, font=("Inter", 12, "bold"), justify="left", bg=data["description_box_bg"],fg=data["description_box_font"],text = "4 letter combination with more objectively simpler terms\nEasiest difficulty out of the three modes")
        self.Easy_Mode_Word_description.place(relx=0.35, rely=0.2, relwidth=0.4, relheight=0.1)
        self.Easy_button.place(relx=0.2, rely=0.2, relwidth=0.1, relheight=0.1)
        self.Easy_button.bind("<Enter>", lambda e: self.Easy_button.config(bg="#68AF3E"))
        self.Easy_button.bind("<Leave>", lambda e: self.Easy_button.config(bg="#558B36"))
        self.Go_back_to_home_page=tk.Button(self.Difficulty,text="<-- Back", font = ("Inter", 14,"bold"), command = self.Go_back, bg = "#84817f", fg = "white", bd = 0, cursor = "hand2")
        self.Go_back_to_home_page.place(x=20, y=20)
        self.Home.pack(fill="both", expand=True)

    #the code that allows the home page to appear
    def home_page(self):
        self.Home.pack(fill="both", expand=True)
    #def code that allows the difficulty page to appear
    def home_page_to_difficulty_page(self):
        self.Home.pack_forget()
        self.Difficulty.pack(fill="both", expand=True)

        #change this so that it connects to the code of the wordle page
    def difficulty_page_to_game_page(self,difficulty):
        self.Difficulty.pack_forget()
        if hasattr(self,"frame_of_game_page") and self.frame_of_game_page.winfo_exists():
            self.frame_of_game_page.destroy()
        self.frame_of_game_page=tk.Frame(self.root,bg="white")
        self.frame_of_game_page.pack(fill="both",expand=True)
        StellaVerbaGamePage(self.frame_of_game_page,difficulty,self)
    #code that displays the result page itself
    def displaying_the_results_page(self,won,word,guesses):
        if hasattr(self,"result_frame") and self.result_frame.winfo_exists():
            self.result_frame.destroy()
        if hasattr(self,"frame_of_game_page") and self.frame_of_game_page.winfo_exists():
            self.frame_of_game_page.destroy()
        self.Difficulty.pack(fill="both",expand=True)

    #code that displays the popup of the result page
    def show_result_page(self, won, word, guesses):
        if hasattr(self, "frame_of_game_page") and self.frame_of_game_page.winfo_exists():
            self.frame_of_game_page.destroy()
        self.result_frame = tk.Frame(self.root, bg="white")
        self.result_frame.pack(fill="both", expand=True)
        StellaVerbaResultPage(self.result_frame, won, word, guesses, self)

    #Things to do - connect the wordle page, add single line box that shows answers,
    def load_button(self,mode):
        self.mode=mode
        data=self.assets[mode]
        self.Home_background = PhotoImage(file=str(self.img / data["background"])) #The bg for home and diff
        self.star = PhotoImage(file=str(self.img / data["star"])) #star img of button
        self.sun = PhotoImage(file=str(self.img / data["sun"])) #sun img of button
        self.moon = PhotoImage(file=str(self.img / data["moon"])) #moon img button
        self.hovering_over_star_button = PhotoImage(file=str(self.img / "hstar.png")) #the hover image that it switches to
        #The actual pages
        self.Home.config(bg=data["bgc"])
        self.Difficulty.config(bg=data["bgc"])
        self.difficulty_background.config(image=self.Home_background,bg=data["bgc"],fg=data["bgt"] )
        #all the labels and text
        self.home_background.config(image=self.Home_background, bg=data["bgc"])
        self.home_title_part_2.config(bg=data["bgc"], fg=data["bgt"])
        self.home_title_part_1.config(bg=data["bgc2"], fg=data["bgt2"])
        self.difficulty_selection_page_title.config(bg=data["bgc"], fg=data["bgt"])
        #The buttons for the home page eg: the sun the star and the moon
        self.star_button.config(image=self.star,bg=data["bgc"])
        self.lightbutton.config(image=self.sun,bg=data["bgc"],activebackground=data["bgc"])
        self.darkbutton.config(image=self.moon,bg=data["bgc"],activebackground=data["bgc"])

    def Go_back(self):
        self.Difficulty.pack_forget()
        self.Home.pack(fill="both", expand=True)

    def go_back_to_difficulty_page(self):
        go_back_pop_up = tk.Toplevel(self.root)
        go_back_pop_up.geometry("400x250")
        go_back_pop_up.resizable(False, False)
        go_back_pop_up.configure(bg="#2E2E2E")
        go_back_pop_up.transient(self.root)
        go_back_pop_up.grab_set()
        tk.Label(go_back_pop_up, text="Leave Game Page?", font=("Rubik Bubbles", 20), bg="#2E2E2E", fg="white").pack(pady=(20, 10))
        tk.Label(go_back_pop_up,text="Leave current game page and return\nto difficulty selection?\n\n(Leaving will lose your current progress)",font=("Inter", 11), bg="#2E2E2E", fg="#AAAAAA").pack()
    #if the user had pressed yes it would destroy the game page and then lead back to the difficulty page
        def yes():
            go_back_pop_up.destroy()
            if hasattr(self, "frame_of_game_page"):
                self.frame_of_game_page.destroy()
            self.Difficulty.pack(fill="both", expand=True)
            #when the user presses no in the message box it would just destroy the frame
        def no():
            go_back_pop_up.destroy()
        button_frame = tk.Frame(go_back_pop_up, bg="#2E2E2E")
        button_frame.pack(pady=20)
        tk.Button(button_frame, text="Leave", bg="#C7141F", fg="white", font=("Inter", 12, "bold"), bd=0,command=yes).pack(side="left", padx=10)
        tk.Button(button_frame, text="Stay", bg="#558B36", fg="white", font=("Inter", 12, "bold"), bd=0,command=no).pack(side="left", padx=10)

root=tk.Tk()
app=Verba(root)
root.mainloop()
