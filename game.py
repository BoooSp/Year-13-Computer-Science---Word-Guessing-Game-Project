from tkinter import *
import urllib.request
import threading
import random
import tkinter as tk
from pathlib import Path
from PIL.ImageTk import PhotoImage

import pyglet

#emergency change all capital letter of functions and naming conventions

# list of words for each mode (making it 4/5/6 letter for each mode)
Words_for_the_game = {"easy":["idea","view","fact","goal","role","plan","term","item","base","gain","loss","rule","mean","rank","feel"],
                   "medium":["theme","issue","valid","logic","claim","value","adapt","focus","trend","civil","shift","cause","proof","image","grant"],
                   "hard":["impact","theory","review","debate","select","create","survey","assess","expand","symbol","motive","policy","crisis","effort","enable","factor","status","inform"],}

#the definitions of the words
Definitions = {
    "idea": "A thought or suggestion - That's a great idea, let's go to the beach\nUnderstanding or knowledge - I have no idea what you mean\nPurpose or aim - The idea of the game is to get the highest score\nBelief or opinion - They have unusual ideas about politics",
    "view": "What can be seen from a certain location - The apartment has a beautiful view of the ocean\nOpinion or belief - In my view, going left is the best solution\nTo look or watch - Millions of people watched the broadcast\nTo consider or regard - They viewed the delay as a minor inconvenience",
    "fact": "A thing that is true - It's a fact that the sun rises in the east\nSomething you can check or prove - The article was full of facts and figures",
    "goal": "Something you're trying to achieve - My goal is to finish this project by Friday\nA point scored in a sport - She scored the winning goal in the last minute",
    "role": "The job someone does in a group - Everyone has a role to play in the team\nA character in a movie or play - He got the lead role in the school play",
    "plan": "An idea for how to do something - We came up with a plan for the weekend\nWhat you intend to do in future - My plan is to study engineering next year\nTo work out details ahead of time - We need to plan the trip before we leave",
    "term": "A word with a specific meaning - Photosynthesis is a science term\nA block of time at school - The next term starts in two weeks",
    "item": "A single thing - Can you grab that item off the shelf for me\nA point on a list - The first item on the agenda is the budget",
    "base": "The bottom part of something - The lamp has a heavy metal base\nA main place to work or live from - The team set up their base near the river\nTo build something on top of - The movie is based on a true story",
    "gain": "To get something - She gained a lot of confidence from the trip\nTo increase - Prices have gained over the past month\nAn increase or benefit - There was a small gain in his test scores",
    "loss": "Losing something - The loss of his phone really stressed him out\nMoney lost in business - The company reported a loss this year",
    "rule": "Something you have to follow - One rule is no phones in class\nA general pattern - As a rule, the shops close early on Sundays\nTo be in charge of something - The king ruled the country for forty years",
    "mean": "What something means - What does this symbol mean\nTo intend something - I didn't mean to be rude\nUnkind - It's mean to leave someone out on purpose",
    "rank": "A position in an order - She came first in the rankings\nTo put things in order - The app ranks songs by how often you play them",
    "feel": "An emotion - I feel really tired today\nTo touch something - Feel how soft this jumper is\nTo think or believe - I feel like we should leave early",
    "theme": "The main idea of something - The theme of the book is friendship\nA topic for an event - The party had a beach theme",
    "issue": "A problem - There's an issue with the wifi again\nAn edition of a magazine - I bought the latest issue of the magazine",
    "valid": "Makes sense, reasonable - That's a valid point\nStill allowed or usable - My bus pass is valid until next month",
    "logic": "A way of thinking something through - Using basic logic, that can't be true\nThe reasoning behind something - There's a logic to how the files are organised",
    "claim": "To say something is true - He claimed he'd never seen it before\nTo ask for something you're owed - She made a claim on her insurance\nA statement that might be true or false - The ad makes some big claims",
    "value": "How important something is - Education has a lot of value\nThe price or worth of something - The value of the car dropped quickly\nTo care about something - I really value honesty",
    "adapt": "To change to fit a new situation - We had to adapt to the new schedule\nTo turn something into a different form - The book was adapted into a film",
    "focus": "The main thing you're paying attention to - The focus of the lesson is fractions\nTo concentrate on something - Try to focus on one task at a time",
    "trend": "The direction things are heading - There's a trend towards working from home\nSomething popular right now - Big sneakers are a trend at the moment",
    "civil": "Polite, even when disagreeing - They kept the conversation civil\nTo do with citizens or society - She studied civil rights at uni",
    "shift": "To move - He shifted his chair closer to the desk\nA change - There's been a shift in how people shop\nA work period - She works the night shift on weekends",
    "cause": "The reason something happens - The cause of the delay was traffic\nTo make something happen - The storm caused a power cut",
    "proof": "Evidence - Do you have proof that you paid for it\nA draft checked before printing - She read through the proof before sending it off",
    "image": "A picture - The image took ages to load\nHow people see someone - He's trying to fix his public image",
    "grant": "Money given for a purpose - She got a grant to fund her research\nTo allow something - The teacher granted us an extra day for the assignment",
    "impact": "A strong effect - The new policy had a big impact on prices\nThe force of a collision - The impact damaged the front of the car",
    "theory": "An idea that explains something - Scientists came up with a new theory\nA set of ideas about a subject - We learned some music theory in class",
    "review": "A look back to check something - The teacher did a review before the test\nAn opinion on something - He left a five-star review for the restaurant\nTo check something again - Can you review my essay before I submit it",
    "debate": "A discussion with different opinions - The class had a debate about homework\nAn ongoing disagreement - There's a lot of debate about the new rule\nTo argue different sides - They debated which movie to watch",
    "select": "To choose - Select your answer from the dropdown\nCarefully chosen - Only a select few were invited",
    "create": "To make something new - She created a poster for the event\nTo cause something to happen - The changes created a few problems",
    "survey": "A set of questions to collect info - We did a survey to find out what people think\nA general look at something - The report gave a survey of last year's results\nTo look over something - The drone surveyed the area from above",
    "assess": "To judge how good or bad something is - The teacher will assess our projects\nTo work out the value of something - They assessed the damage after the storm",
    "expand": "To become bigger - The company expanded into new countries\nTo add more detail - Could you expand on that idea a bit more",
    "symbol": "Something that represents something else - A heart is a symbol of love\nA character used in writing or maths - The percent sign is a symbol",
    "motive": "The reason behind doing something - His motive for helping was kindness\nWhat's driving someone's actions - Police are trying to find a motive",
    "policy": "A set of rules a group follows - The school has a no-phone policy\nAn official plan of action - The government announced a new policy",
    "crisis": "A serious problem - The country is going through an economic crisis\nA turning point - The story builds up to a crisis moment",
    "effort": "Trying hard - She put a lot of effort into the project\nThe energy something takes - Climbing the hill took a lot of effort",
    "enable": "To make something possible - The new app enables faster messaging\nTo give someone the means to do something - The donation enabled her to study overseas",
    "factor": "Something that affects a result - Weather was a big factor in the delay\nA number that divides evenly into another - 5 is a factor of 20",
    "status": "Someone's position or situation - He has a high status at work\nThe current state of something - What's the status of the order",
    "inform": "To tell someone something - Please inform us if your plans change\nTo shape understanding - The data informed their decision", }

# how many letters and guesses per difficulty
Word_length_for_each_difficulty = {"easy": 4, "medium": 5, "hard": 6} # the word lengths for each of the diffuclty
Letter_limit_for_each_mode = {"easy": 6, "medium": 6, "hard": 6} #the limits I have placed for each mode so the system doesn't allow more letters

#Colours I left here for now
Green  = "#375B37"
Yellow = "#AAA228"
Grey   = "#2B2B2B"

def check_if_real_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}" #uses the url and the website to confirm the word
    try:
        req = urllib.request.Request(url,headers={"User-Agent": "StellaVerba"})
        urllib.request.urlopen(req, timeout=4)#sends the thing to confirm the code, and it is done in 4 seconds
        return True
    except:
        return False
# the class for the keyboard function of my game page
class physical_and_digital_keyboard(Canvas):
    def __init__(self,master,Background_Image):
        Canvas.__init__(self,master,highlightthickness=0,width=600,height=737) #canvas for the keyboard design that I created to place in my design
        self.master = master
        self.place(x=0, y=0)
        self.create_image(0, 0, image=Background_Image, anchor="nw")


#The letters that will be in the keyboard function
        self.Keyboard_letter_boxes = ["ABCDEF","GHIJKL","MNOPQR","STUVWX","YZ"] #the letters that would appear in the keyboard function
        size = 60
        height=1
        gap=10
        letter_button_colour = "#545454"
        self.layout_keys={}
        self.boxes_coord={}
        #sizes of the boxes
        box_width = 6*(size+gap)-gap
        left_side=300-box_width/2
        right_side=300+box_width/2
        at_y_axis=300
        #only the tag bind being placed above works for the keyboard
        self.tag_bind("letter", "<Button-1>",self.push_button)
        self.tag_bind("enter", "<Button-1>", lambda e:self.master.submit_the_answer())
        self.tag_bind("back", "<Button-1>", lambda e:self.master.delete_the_letter())
        #The extra functions that allow the letters to work and the delete and enter button

#the sizing of the keyboard letters boxes to easily be referred to
        for i in range(4):
            boxes = self.Keyboard_letter_boxes[i]
            for col, char in enumerate(boxes):
               x = 300 + (size + gap) * (col- (len(boxes) - 1) / 2)
               y = at_y_axis + i * (size * height + gap)
               self.create_rectangle(x -size/2,y-size*height/2,x+size/2,y+size*height/2,width=0,fill=letter_button_colour, tags=("key_" + char, "letter"))
               self.create_text(x, y, text=char, font=("Inter", 18, "bold"), fill="white",tags=("letter", "label_" + char))
               self.boxes_coord["key_" + char]=(x-size/2,y-size*height/2,x+size/2,y+size*height/2)

#last row has different shapes so the sizing has to be different
        Last_row_of_keyboard = at_y_axis + 4 * (size * height + gap)
        Y_axis = 300-(size+gap)/2
        zonaxis=300+(size+gap)/2
        Left_side_of_delete_button  = left_side
        Right_side_of_delete_button = Y_axis- size/2 - gap
        Middle_of_delete_button= (Left_side_of_delete_button + Right_side_of_delete_button) / 2

#the ends of the last line so that it fits inside the box shape of my plan of the keyboard shape
        Left_side_of_enter_button  = zonaxis+size/2+gap
        Right_side_of_enter_button = right_side
        Middle_of_enter_button= (Left_side_of_enter_button + Right_side_of_enter_button) / 2

#The last line of buttons on the keyboard has to be done seperately because they are not same shaped (its huering my head ;-;)
        self.create_rectangle(Left_side_of_delete_button, Last_row_of_keyboard - size*height/2,Right_side_of_delete_button, Last_row_of_keyboard + size*height/2,width=0, fill=letter_button_colour, tags=("back", "key_back"))
        self.create_text(Middle_of_delete_button, Last_row_of_keyboard,text="DELETE", font=("Inter", 12, "bold"),fill="white", tags=("delete", "deletebutton","back"))
        self.boxes_coord["Delete key"] = (Left_side_of_delete_button, Last_row_of_keyboard -size*height/2,Right_side_of_delete_button, Last_row_of_keyboard + size*height/2)
        self.create_rectangle(Y_axis - size / 2, Last_row_of_keyboard - size * height / 2,Y_axis + size / 2, Last_row_of_keyboard + size * height / 2,width=0, fill=letter_button_colour, tags=("key_Y", "letter"))
        self.create_text(Y_axis, Last_row_of_keyboard,text="Y", font=("Inter", 18, "bold"),fill="white", tags=("letter", "label Y BUtton"))
        self.boxes_coord["Y"] = (Y_axis - size / 2, Last_row_of_keyboard - size * height / 2, Y_axis + size / 2,Last_row_of_keyboard + size * height / 2)
        self.create_rectangle(zonaxis - size / 2, Last_row_of_keyboard - size * height / 2, zonaxis + size / 2,Last_row_of_keyboard + size * height / 2, width=0, fill=letter_button_colour,tags=("key_Z", "letter"))
        self.create_text(zonaxis, Last_row_of_keyboard, text="Z", font=("Inter", 18, "bold"), fill="white",tags=("letter", "Z Button"))
        self.boxes_coord["Z"] = (zonaxis - size / 2,Last_row_of_keyboard - size * height / 2, zonaxis + size / 2,Last_row_of_keyboard + size * height / 2)
        self.create_rectangle(Left_side_of_enter_button, Last_row_of_keyboard - size * height / 2, Right_side_of_enter_button,Last_row_of_keyboard + size * height / 2, width=0, fill=letter_button_colour,tags=("enter", "enter button"))
        self.create_text(Middle_of_enter_button, Last_row_of_keyboard, text="ENTER", font=("Inter", 12, "bold"),fill="white", tags=("enter", "enterbutton"))
        self.boxes_coord["Enter key"] = (Left_side_of_enter_button, Last_row_of_keyboard - size * height / 2,Right_side_of_enter_button, Last_row_of_keyboard + size * height / 2)

#allows the buttons to be pushed and pressed aswell as the delete and the enter button
    def push_button(self, event):
        for tag,(x1,y1,x2,y2) in self.boxes_coord.items():
            if tag in ("Delete key", "Enter key"):
                    continue
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                self.master.allow_letter_type(tag[-1])
                return


class StellaVerbaGamePage(Frame):
    def __init__(self,master,difficulty,app):
        Frame.__init__(self,master,bg="white") # frame for the whole page of my wordle
        self.master=master
        self.app=app
        self.pack(fill="both", expand=True)

        self.shortcut = Path(__file__).parent #code taken from main page
        self.img = self.shortcut / "images"
        self.Background_Image = PhotoImage(file=str(self.img / ("dbg1.png" if app.mode == "darkmode" else "lbg1.png")))
        self.bg_label = Label(self, image=self.Background_Image, bd=0)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.Go_back_to_home_page_button = tk.Button(self, text="<-- Back", font=("Inter", 14, "bold"), command=self.app.Go_back_to_difficulty_page,bg="#545454", fg="white", bd=0, cursor="hand2")
        self.Go_back_to_home_page_button.place(x=20, y=20)
        self.Go_back_to_home_page_button.lift()
        self.font = self.shortcut / "Fonts"
        # all the font files dir connected with the sef font thingy to make my life easier
        for font_file in self.font.glob("*.ttf"):
            pyglet.font.add_file((str(font_file)))


        self.Word_length = Word_length_for_each_difficulty[difficulty]
        self.Max_guesses = Letter_limit_for_each_mode[difficulty]
        self.answers = Words_for_the_game[difficulty]
        self.words = Words_for_the_game[difficulty]

        self.textField = ""
        self.entered = 0
        self.frozen = False
        self.checking= False
        self.word_already_used = []
        self.popup =Label(self,text="",font=("Inter",15,"bold"), bg="#91000c",fg="#E8E8E8")


        self.keyboard=physical_and_digital_keyboard(self,self.Background_Image)
        self.Go_back_to_home_page_button.lift()
        cell=68
        gap=6
        padding=40
        Answer_box_width= self.Word_length*cell+(self.Word_length-1)*gap
        Answer_box_height=self.Max_guesses*cell+(self.Max_guesses-1)*gap
        Answer_box_x_axis=600+(600-Answer_box_width)//2
        Answer_box_y_axis=(737-Answer_box_height)//2

        #Code for the line function including help button, Hint_button and the line of the final answer box

        Centre_of_keyboard = 300
        Single_Line_Functions_y_axis = 115
        Single_Line_functions_x_axis = Centre_of_keyboard - Answer_box_width // 2
        #The line that seperates from the keyboard and the single line funciton
        self.Seperation_line_of_keyboard_and_answer_box = Canvas(self, bg="#555555", highlightthickness=0, height=2, width=560)
        self.Seperation_line_of_keyboard_and_answer_box.place(x=20, y=Single_Line_Functions_y_axis + cell + 15)

        self.Single_line_of_boxes = Canvas(self, bg="#3D3D3D", width=Answer_box_width, height=cell, highlightthickness=0)
        self.Single_line_of_boxes.place(x=Single_Line_functions_x_axis, y=Single_Line_Functions_y_axis)
        for i in range(self.Word_length):
            xx = i * (cell + gap)
            self.Single_line_of_boxes.create_rectangle(xx, 0, xx + cell, cell, outline="#6E6E6E", width=2,tags=(f"hint{i}",))
            self.Single_line_of_boxes.create_text(xx + cell // 2, cell // 2, text="", font=("Inter", 30, "bold"), fill="white",tags=(f"give_hint_letter{i}",))


        #hint button image and stuffs
        self.Hint_button_image = PhotoImage(file=str(self.img / "lightbulb.png"))
        self.Hint_button = Label(self, image=self.Hint_button_image, bd=0, cursor="hand2")
        self.Hint_button.place(x=Single_Line_functions_x_axis - 80, y=Single_Line_Functions_y_axis, width=cell, height=cell)
        self.Hint_button.bind("<ButtonRelease-1>", self.give_hint)

#the help and documentation page button and the image that appears wehn it is pressed
        self.Help_button = tk.Button(self, text="?", font=("Inter", 20, "bold"), cursor="hand2",bd=0, relief="flat", bg="#545454", fg="white",activebackground="#6a6a6a", activeforeground="white",command=self.Show_help_page)
        self.Help_button.place(x=Single_Line_functions_x_axis + Answer_box_width + 20, y=Single_Line_Functions_y_axis, width=cell,height=cell)

        self.Help_image = PhotoImage(file=str(self.img / "helpimg.png"))
        self.Help_image_box = Label(self, image=self.Help_image, bd=0)
        self.Help_image_close = Label(self, text="✕", font=("Inter", 14, "bold"), cursor="hand2", bg="#C7141F", fg="white")
        self.Help_image_close.bind("<ButtonRelease-1>", self.Close_help_page)

#the box that the user enters the letters in like how it would be in wordle
        self.Answer_box_background=Canvas(self ,bg="#2A2A2A",highlightthickness=0,width=Answer_box_width+padding*2, height=Answer_box_height+padding*2)
        self.Answer_box_background.place(x=Answer_box_x_axis-padding,y=Answer_box_y_axis-padding)
        self.canvas=Canvas(self ,bg="#3D3D3D",width=Answer_box_width,height=Answer_box_height,highlightthickness=0)
        self.canvas.place(x=Answer_box_x_axis,y=Answer_box_y_axis)
        for x in range(self.Word_length):
            for y in range(self.Max_guesses):
                xx = x * (cell + gap)
                yy = y * (cell + gap)
                self.canvas.create_rectangle(xx,yy,xx+cell,yy+cell,outline="#6E6E6E",width=2,tag=f"cell{x}{y}",fill="#3D3D3D")
                self.canvas.create_text(xx+cell//2,yy+cell//2, text="", font=("Inter", 30, "bold"),tag=f"text{x}{y}",fill="white")



        self.WordChoice=random.choice(self.answers).upper()
        self.word=self.WordChoice
        self.Gray=Grey # the colours that I previously created (above)
        self.Green=Green
        self.Yellow=Yellow
        self.bind_all("<Key-BackSpace>", self.delete_the_letter)
        self.bind_all("<Key-Return>", self.submit_the_answer)
        self.bind_all("<Key>", self.allow_letter_type)


#Function that allows the letter to be deleted from the answering box thing
    def delete_the_letter(self,event=None):
        if self.frozen or self.checking or len(self.textField)==0:
            return
        self.textField=self.textField[:-1]
        self.canvas.itemconfigure(f"text{len(self.textField)}{self.entered}",text="")
#the code that determines of the user is entering a proper answer
    def submit_the_answer(self,event=None):
        if self.frozen or self.checking:
            return
        if len(self.textField) <self.Word_length:
            self.Show_error_pop_up(f"Not enough letters")
            return
        if self.entered>=self.Max_guesses:
            return
        self.checking = True
        threading.Thread(target=self.Checking_before_scoring_the_guess, daemon=True).start()
#the code that allows the user to enter the letters from the keybaord
    def allow_letter_type(self, event):
        if len(self.textField) >= self.Word_length or self.frozen or self.checking:
            return
        if isinstance(event, str):
            letter = event.upper()
        else:
            if not event.char:
                return
            letter = event.char.upper()
        if not letter.isalpha():
            return
        self.canvas.itemconfigure(f"text{len(self.textField)}{self.entered}", text=letter)
        self.textField += letter
#the code checks the ansewr the user enters before confirming anything
    def Checking_before_scoring_the_guess(self):
        #fix this
        valid = check_if_real_word(self.textField)
        self.after(0,lambda: self.After_the_checking(valid))
#after it has checked the thign it would determine if it does not meet the criteria to be considered as a proper guess then one of the errosrs would pop up
    def After_the_checking(self, valid):
        self.checking = False
        if not valid:
            self.Show_error_pop_up("Word doesn't exist")
            return
        if self.textField in self.word_already_used:
            self.Show_error_pop_up("Word has already been used")
            return
        self.word_already_used.append(self.textField)
        self.Scoring_the_guess()


    def Show_error_pop_up(self, message):
        self.popup.config(text=message)
        self.popup.lift()
        self.popup.place(relx=0.5,y=20,anchor="n")
        self.after(1500, self.popup.place_forget) #The amount of time the error thing stays up for
#it would change the colour of the letter of the words the user enter to indicate wether if the letter position is correct/if the letter is in the word but not in correct location or it doenst appear at all
    def Scoring_the_guess(self):
        guess =self.textField
        secret= self.word
        colored = [self.Gray]*self.Word_length
        letter_count ={}
        for char in secret:
            if char in letter_count:
                letter_count[char]+=1
            else:
                letter_count[char]=1
        for i in range(self.Word_length):
            if guess[i]== secret[i]:
                colored[i] =self.Green
                letter_count[guess[i]]-=1
        for i in range(self.Word_length):
            if colored[i] ==self.Green:
                continue
            if guess[i] in letter_count and letter_count[guess[i]]>0:
                colored[i]=self.Yellow
                letter_count[guess[i]]-=1




        for i in range(self.Word_length):
            self.canvas.itemconfigure(f"cell{i}{self.entered}",fill=colored[i],outline=colored[i])
            self.canvas.itemconfigure(f"text{i}{self.entered}",fill="white")
            if colored[i] == self.Green:
                self.Single_line_of_boxes.itemconfigure(f"give_hint_letter{i}", text=self.word[i])
                self.Single_line_of_boxes.itemconfigure(f"hint{i}", fill=self.Green, outline=self.Green)
            cur = self.keyboard.itemcget("key_"+guess[i],"fill")
            if cur == self.Green:
                continue
            if colored[i] == self.Green:
                self.keyboard.itemconfigure("key_" + guess[i], fill=self.Green)
            elif colored[i] == self.Yellow and cur != self.Green:
                self.keyboard.itemconfigure("key_"+guess[i],fill=self.Yellow)
            elif colored[i]== self.Gray and cur =="#545454":
                self.keyboard.itemconfigure("key_"+guess[i], fill=self.Gray)
            if colored[i] == self.Green:
                self.Single_line_of_boxes.itemconfigure(f"give_hint_letter{i}", text=guess[i])
                self.Single_line_of_boxes.itemconfigure(f"hint{i}", fill=self.Green, outline=self.Green)
        won = colored.count(self.Green) ==self.Word_length
        self.entered+= 1
        self.textField=""
        if won or self.entered >=self.Max_guesses:
            self.frozen =True
            self.Going_to_the_result_page(won)
#the hint button that gives hint by telling the user what lettter appears in what locaiton in the Single_line_of_boxes function
    def give_hint(self, event=None):
        for i in range(self.Word_length):
            current = self.Single_line_of_boxes.itemcget(f"give_hint_letter{i}", "text")
            if current == "":
                self.Single_line_of_boxes.itemconfigure(f"give_hint_letter{i}", text=self.word[i])
                self.Single_line_of_boxes.itemconfigure(f"hint{i}", fill=self.Green, outline=self.Green)
                self.Single_line_of_boxes.itemconfigure(f"hint{i}", tags=("temporaryhint", f"hint{i}"))
                self.after(2000, lambda i=i: self.Clear_hint(i))
                return
#this is more of a personal choice where the hint goes away after a bit, so that the hint is like a mini clue they can get but then it fades so they still "get" feeling of doing it idk
    def Clear_hint(self, i):
        current = self.Single_line_of_boxes.itemcget(f"give_hint_letter{i}", "text")
        if current == self.word[i]:
            self.Single_line_of_boxes.itemconfigure(f"give_hint_letter{i}", text="")
            self.Single_line_of_boxes.itemconfigure(f"hint{i}", fill="#3D3D3D", outline="#6E6E6E")
            #function that allows the help page to open and be shown
    def Show_help_page(self):
            self.Help_image_box.place(relx=0.5, rely=0.5, anchor="center")
            self.Help_image_box.lift() #brings the help page to appear in front
            self.Help_image_close.place(relx=0.715, rely=0.12, anchor="center")
            self.Help_image_close.lift()#allows the help page close button to appear in frong of the help page

    def Close_help_page(self, event=None): #the function that closes both the belp page and the help page button
        self.Help_image_box.place_forget()
        self.Help_image_close.place_forget()
    def Going_to_the_result_page(self, won):
        self.unbind_all("<Key-BackSpace>")
        self.unbind_all("<Key-Return>")
        self.unbind_all("<Key>")
        self.after(1000, lambda:self.app.Show_result_page(won=won,word=self.word,guesses=self.entered))



class StellaVerbaResultPage(Frame):
    def __init__(self, master,won,word,guesses,app):
        Frame.__init__(self, master, bg="white")
        self.master = master
        self.app = app
        self.pack(fill="both", expand=True)
        self.shortcut = Path(__file__).parent
        self.img = self.shortcut / "images"

        self.Background_Image = PhotoImage(file=str(self.img / ("dbg2.png" if app.mode == "darkmode" else "lbg2.png")))
        self.Background_Label = Label(self, image=self.Background_Image, bd=0)
        self.Background_Label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Result_page_box = tk.Frame(self, bg="#2E2E2E", bd=0)
        self.Result_page_box.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.78)
        #depending on wether the user had won one of these two texts appears
        if won:
            message = "Congratulations"
            Colour_of_the_final_text = "#6AAA64"
        else:
            message = "Better Luck Next Time"
            Colour_of_the_final_text = "#C7141F"

        self.Result_page_text = tk.Label(self.Result_page_box, text=message, font=("Rubik Bubbles", 30),bg="#2E2E2E", fg=Colour_of_the_final_text)
        self.Result_page_text.pack(pady=(40, 10))
        #the line that seperates the congradulatory line with the definition and the word reveal text
        self.divider = tk.Frame(self.Result_page_box, bg="#555555", height=2)
        self.divider.pack(fill="x", padx=30, pady=(0, 15))

        self.The_word_is_text = tk.Label(self.Result_page_box, text="The word is:", font=("Inter", 16),bg="#2E2E2E", fg="#AAAAAA")
        self.The_word_is_text.pack(pady=(0, 5))

        self.Word_Revealed = tk.Label(self.Result_page_box, text=word.upper(), font=("Inter", 40, "bold"), bg="#2E2E2E", fg="white")
        self.Word_Revealed.pack(pady=(0, 5))
        #shows the user the amount of trials they did and if they won
        if won:
            self.Amount_of_guesses_showed = tk.Label(self.Result_page_box, text=f"You got it in {guesses} guess{'es' if guesses != 1 else ''}!", font=("Inter", 14), bg="#2E2E2E", fg="#AAAAAA")
            self.Amount_of_guesses_showed.pack(pady=(0, 20))
        #this is more of a testing type of code to make sure that each of the word has definition
        definition = Definitions.get(word.lower(), "No definition available.")
        self.Definition_of_the_word = tk.Frame(self.Result_page_box, bg="#545454", bd=0)
        self.Definition_of_the_word.pack(padx=30, pady=(0, 30), fill="x")
        #the font of the definition inside the box
        self.Font_of_the_definition = tk.Label(self.Definition_of_the_word, text=definition, font=("Inter", 9),bg="#545454", fg="white", wraplength=480, justify="center")
        self.Font_of_the_definition.pack(padx=20, pady=20)
        #the frame of the play again and the exit button
        self.Play_Again_And_Exit_Button = tk.Frame(self.Result_page_box, bg="#2E2E2E")
        self.Play_Again_And_Exit_Button.pack(pady=(0, 40))
        #The play again button for the result page
        self.Play_Again_Button = tk.Button(self.Play_Again_And_Exit_Button, text="Play Again", font=("Inter", 16, "bold"), bg="#548a38", fg="white", bd=0, relief="flat", cursor="hand2", activebackground="#5d993d", activeforeground="white", command=self.Play_Again)
        self.Play_Again_Button.pack(side="left", padx=20, ipadx=20, ipady=10)
        #the exit button for the result page
        self.Exit_button = tk.Button(self.Play_Again_And_Exit_Button, text="Exit", font=("Inter", 16, "bold"),bg="#ab1b27", fg="white", bd=0, relief="flat", cursor="hand2",activebackground="#bf1d2a", activeforeground="white",command=self.master.winfo_toplevel().destroy)
        self.Exit_button.pack(side="left", padx=20, ipadx=20, ipady=10)
    #the play again function where it would destroy the page and would lead back to the game page
    def Play_Again(self):
        self.destroy()
        self.app.Displaying_the_results_page(won=None, word=None, guesses=None)