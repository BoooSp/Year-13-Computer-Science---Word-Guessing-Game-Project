from tkinter import *
import urllib.request
import threading
import random
import tkinter as tk
from pathlib import Path
from PIL.ImageTk import PhotoImage

import pyglet



# list of words for each mode (making it 4/5/6 letter for each mode)
Wordsforthegame = {"easy":["idea","view","fact","goal","role","plan","term","item","base","gain","loss","rule","mean","rank","feel"],
                   "medium":["theme","issue","valid","logic","claim","value","adapt","focus","trend","civil","shift","phase","cause","proof","image","grant"],
                   "hard":["impact","theory","review","debate","select","create","survey","assess","expand","symbol","motive","policy","crisis","effort","enable","factor","status","inform"],}

#the definitons of the words
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
    "phase": "A stage in something - The project is in its testing phase\nA period someone goes through - It's just a phase, he'll grow out of it",
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
wordlength_eachdifficulty = {"easy": 4, "medium": 5, "hard": 6}
guessinglimits = {"easy": 6, "medium": 6, "hard": 6}

#Colours i left here for now
Green  = "#375B37"
Yellow = "#AAA228"
Grey   = "#2B2B2B"

def checkifrealword(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}" #uses the url and the website to confirm the word
    try:
        req = urllib.request.Request(url,headers={"User-Agent": "StellaVerba"})
        urllib.request.urlopen(req, timeout=4)#sends the thing to confirm the code and it is done in 4 seconds
        return True
    except:
        return False
# the class for the keyboard function of my game page
class Physical_DigitalKeyboard(Canvas):
    def __init__(self,master,bgimage):
        Canvas.__init__(self,master,highlightthickness=0,width=600,height=737) #canvas for the keyboard design that i created to palce in my design
        self.master = master
        self.place(x=0, y=0)
        self.create_image(0, 0, image=bgimage, anchor="nw")


#The letters that will be in the keyboard function
        self.Keyboard_letter_boxes = ["ABCDEF","GHIJKL","MNOPQR","STUVWX","YZ"]
        size = 60
        height=1
        gap=10
        LetterButtonColour = "#545454"
        self.layoutkeys={}
        self.boxes_coord={}
        #sizes of the boxes
        totalboxwidth = 6*(size+gap)-gap
        leftside=300-totalboxwidth/2
        rightside=300+totalboxwidth/2
        startingatyaxis=300
        #only the tag bind being placed above works for the keyboard
        self.tag_bind("letter", "<Button-1>",self.push_button)
        self.tag_bind("enter", "<Button-1>", lambda e:self.master.subitanswerchoice())
        self.tag_bind("back", "<Button-1>", lambda e:self.master.deletetheletter())
        #The extra functions that allow the letters to work and the delete and enter button

#the sizing of the keyboard letters boxes to easily be reffered to
        for i in range(4):
            boxes = self.Keyboard_letter_boxes[i]
            for char in boxes:
               col=boxes.find(char)
               x = 300 + (size + gap) * (col- (len(boxes) - 1) / 2)
               y = startingatyaxis + i * (size * height + gap)
               self.create_rectangle(x -size/2,y-size*height/2,x+size/2,y+size*height/2,width=0,fill=LetterButtonColour, tags=("key_" + char, "letter"))
               self.create_text(x, y, text=char, font=("Inter", 18, "bold"), fill="white",tags=("letter", "label_" + char))
               self.boxes_coord["key_" + char]=(x-size/2,y-size*height/2,x+size/2,y+size*height/2)

#last row has different shapes so the sizing has to be different
        lastrowofkeyboard = startingatyaxis + 4 * (size * height + gap)
        yonaxis = 300-(size+gap)/2
        zonaxis=300+(size+gap)/2
        deletebuttonleftside  = leftside
        deletebuttonrightside = yonaxis- size/2 - gap
        deletebuttonmiddle= (deletebuttonleftside + deletebuttonrightside) / 2

#the ends of the last line so that it fits inside the box shape of my plan of the keyboard shape
        enterbuttonleftside  = zonaxis+size/2+gap
        enterbuttonrightside = rightside
        enterbuttonmiddleside= (enterbuttonleftside + enterbuttonrightside) / 2

#The last line of buttons on the keyboard has to be done seperately because they are not same shaped (its huering my head ;-;)
        self.create_rectangle(deletebuttonleftside, lastrowofkeyboard - size*height/2,deletebuttonrightside, lastrowofkeyboard + size*height/2,width=0, fill=LetterButtonColour, tags=("back", "key_back"))
        self.create_text(deletebuttonmiddle, lastrowofkeyboard,text="DELETE", font=("Inter", 12, "bold"),fill="white", tags=("delete", "deletebutton","back"))
        self.boxes_coord["Delete key"] = (deletebuttonleftside, lastrowofkeyboard -size*height/2,deletebuttonrightside, lastrowofkeyboard + size*height/2)
        self.create_rectangle(yonaxis - size / 2, lastrowofkeyboard - size * height / 2,yonaxis + size / 2, lastrowofkeyboard + size * height / 2,width=0, fill=LetterButtonColour, tags=("key_Y", "letter"))
        self.create_text(yonaxis, lastrowofkeyboard,text="Y", font=("Inter", 18, "bold"),fill="white", tags=("letter", "label Y BUtton"))
        self.boxes_coord["Y key"] = (yonaxis - size / 2, lastrowofkeyboard - size * height / 2, yonaxis + size / 2,lastrowofkeyboard + size * height / 2)
        self.create_rectangle(zonaxis - size / 2, lastrowofkeyboard - size * height / 2, zonaxis + size / 2,lastrowofkeyboard + size * height / 2, width=0, fill=LetterButtonColour,tags=("key Z", "letter"))
        self.create_text(zonaxis, lastrowofkeyboard, text="Z", font=("Inter", 18, "bold"), fill="white",tags=("letter", "Z Button"))
        self.boxes_coord["Z key"] = (zonaxis - size / 2,lastrowofkeyboard - size * height / 2, zonaxis + size / 2,lastrowofkeyboard + size * height / 2)
        self.create_rectangle(enterbuttonleftside, lastrowofkeyboard - size * height / 2, enterbuttonrightside,lastrowofkeyboard + size * height / 2, width=0, fill=LetterButtonColour,tags=("enter", "enter button"))
        self.create_text(enterbuttonmiddleside, lastrowofkeyboard, text="ENTER", font=("Inter", 12, "bold"),fill="white", tags=("enter", "enterbutton"))
        self.boxes_coord["Enter key"] = (enterbuttonleftside, lastrowofkeyboard - size * height / 2,enterbuttonrightside, lastrowofkeyboard + size * height / 2)

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
        self.bgimage = PhotoImage(file=str(self.img / ("dbg1.png" if app.mode == "darkmode" else "lbg1.png")))
        self.bg_label = Label(self, image=self.bgimage, bd=0)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.font = self.shortcut / "Fonts"
        # all the font files dir connected with the sef font thingy to make my life easier
        pyglet.font.add_file(str(self.font / "Inter-Italic-VariableFont_opsz,wght.ttf"))
        pyglet.font.add_file(str(self.font / "Italianno-Regular.ttf"))
        pyglet.font.add_file(str(self.font / "RubikBubbles-Regular.ttf"))
        pyglet.font.add_file(str(self.font / "RubikPuddles-Regular.ttf"))


        self.wordlength = wordlength_eachdifficulty[difficulty]
        self.maxguesses = guessinglimits[difficulty]
        self.answers = Wordsforthegame[difficulty]
        self.words = Wordsforthegame[difficulty]

        self.textField = ""
        self.entered = 0
        self.frozen = False
        self.checking= False
        self.alreadywordused = []
        self.popup =Label(self,text="",font=("Inter",12,"bold"), bg="#C30010",fg="#E8E8E8")


        self.keyboard=Physical_DigitalKeyboard(self,self.bgimage)
        cell=68
        gap=6
        padding=40
        answerletterboxwitdth= self.wordlength*cell+(self.wordlength-1)*gap
        answerletterboxheight=self.maxguesses*cell+(self.maxguesses-1)*gap
        ansboxsx=600+(600-answerletterboxwitdth)//2
        ansboxsy=(737-answerletterboxheight)//2

        #Code for the line function including help button, hintbutton and the line of the final answer box

        centreofkeyboardthing = 300
        functionlinething_y = 115
        functionlinething_x = centreofkeyboardthing - answerletterboxwitdth // 2
        #The line that seperates from the keyboard and the single line funciton
        self.middleline_inwordlepage = Canvas(self, bg="#555555", highlightthickness=0, height=2, width=560)
        self.middleline_inwordlepage.place(x=20, y=functionlinething_y + cell + 15)

        self.singlelinebox = Canvas(self, bg="#3D3D3D", width=answerletterboxwitdth, height=cell, highlightthickness=0)
        self.singlelinebox.place(x=functionlinething_x, y=functionlinething_y)
        for x in range(self.wordlength):
            xx = x * (cell + gap)
            self.singlelinebox.create_rectangle(xx, 0, xx + cell, cell, outline="#6E6E6E", width=2, tag=f"hint{x}", fill="#3D3D3D")
            self.singlelinebox.create_text(xx + cell // 2, cell // 2, text="", font=("Inter", 30, "bold"), fill="white",tag=f"givehintletter{x}")

#hint button image and stuffs
        self.hintbuttonimage = PhotoImage(file=str(self.img / "lightbulb.png"))
        self.hintbutton = Label(self, image=self.hintbuttonimage, bd=0, cursor="hand2")
        self.hintbutton.place(x=functionlinething_x - 80, y=functionlinething_y, width=cell, height=cell)
        self.hintbutton.bind("<ButtonRelease-1>", self.givehint)

#the help and documentation page button and the image that appears wehn it is pressed
        self.helpbutton = tk.Button(self, text="?", font=("Inter", 20, "bold"), cursor="hand2",bd=0, relief="flat", bg="#545454", fg="white",activebackground="#6a6a6a", activeforeground="white",command=self.showhelppage)
        self.helpbutton.place(x=functionlinething_x + answerletterboxwitdth + 20, y=functionlinething_y, width=cell,height=cell)

        self.helpimg = PhotoImage(file=str(self.img / "helpimg.png"))
        self.helppagebox = Label(self, image=self.helpimg, bd=0)
        self.helppageclose = Label(self, text="✕", font=("Inter", 14, "bold"), cursor="hand2", bg="#C7141F", fg="white")
        self.helppageclose.bind("<ButtonRelease-1>", self.closehelppage)

#the box that the user enters the letters in like how it would be in wordle
        self.ansboxbg=Canvas(self ,bg="#2A2A2A",highlightthickness=0,width=answerletterboxwitdth+padding*2, height=answerletterboxheight+padding*2)
        self.ansboxbg.place(x=ansboxsx-padding,y=ansboxsy-padding)
        self.canvas=Canvas(self ,bg="#3D3D3D",width=answerletterboxwitdth,height=answerletterboxheight,highlightthickness=0)
        self.canvas.place(x=ansboxsx,y=ansboxsy)
        for x in range(self.wordlength):
            for y in range(self.maxguesses):
                xx = x * (cell + gap)
                yy = y * (cell + gap)
                self.canvas.create_rectangle(xx,yy,xx+cell,yy+cell,outline="#6E6E6E",width=2,tag=f"cell{x}{y}",fill="#3D3D3D")
                self.canvas.create_text(xx+cell//2,yy+cell//2, text="", font=("Inter", 30, "bold"),tag=f"text{x}{y}",fill="white")



        self.WordChoice=random.choice(self.answers).upper()
        self.word=self.WordChoice
        self.Gray=Grey
        self.Green=Green
        self.Yellow=Yellow
        self.bind_all("<Key-BackSpace>", self.deletetheletter)
        self.bind_all("<Key-Return>", self.subitanswerchoice)
        self.bind_all("<Key>", self.allow_letter_type)



#Function that allows the letter to be deleted from the answering box thing
    def deletetheletter(self,event=None):
        if self.frozen or self.checking or len(self.textField)==0:
            return
        self.textField=self.textField[:-1]
        self.canvas.itemconfigure(f"text{len(self.textField)}{self.entered}",text="")
#the code that determines of the user is entering a proper answer
    def subitanswerchoice(self,event=None):
        if self.frozen or self.checking:
            return
        if len(self.textField) <self.wordlength:
            self.showerrorpopup(f"Not enough letters")
            return
        if self.entered>+self.maxguesses:
            return
        self.checking = True
        threading.Thread(target=self.checkingboforethescoring, daemon=True).start()
#the code that allows the user to enter the letters from the keybaord
    def allow_letter_type(self, event):
        if len(self.textField) >= self.wordlength or self.frozen or self.checking:
            return
        if isinstance(event, str):
            letter = event
        else:
            letter = event.char.upper()
        if not letter.isalpha():
            return
        self.canvas.itemconfigure(f"text{len(self.textField)}{self.entered}", text=letter)
        self.textField += letter
#the code checks the ansewr the user enters before confirming anything
    def checkingboforethescoring(self):
        #fix this
        valid = checkifrealword(self.textField)
        self.after(0,lambda: self.afterthechecking(valid))
#after it has checked the thign it would determine if it does not meet the criteria to be considered as a proper guess then one of the errosrs would pop up
    def afterthechecking(self, valid):
        self.checking = False
        if not valid:
            self.showerrorpopup("Word doesn't exist")
            return
        if self.textField in self.alreadywordused:
            self.showerrorpopup("Word has already been used")
            return
        self.alreadywordused.append(self.textField)
        self.checkingtheguessandscoring()

    def showerrorpopup(self, message):
        self.popup.config(text=message)
        self.popup.lift()
        self.popup.place(relx=0.5,y=20,anchor="n")
        self.after(4000, self.popup.place_forget)
#it would change the colour of the letter of the words the user enter to indicate wether if the letter position is correct/if the letter is in the word but not in correct location or it doenst appear at all
    def checkingtheguessandscoring(self):
        guess =self.textField
        secret= self.word
        colored = [self.Gray]*self.wordlength
        letterCount ={}
        for char in secret:
            if char in letterCount:
                letterCount[char]+=1
            else:
                letterCount[char]=1
        for i in range(self.wordlength):
            if guess[i]== secret[i]:
                colored[i] =self.Green
                letterCount[guess[i]]-=1
        for i in range(self.wordlength):
            if colored[i] ==self.Green:
                continue
            if guess[i] in letterCount and letterCount[guess[i]]>0:
                colored[i]=self.Yellow
                letterCount[guess[i]]-=1
        for i in range(self.wordlength):
            self.canvas.itemconfigure(f"cell{i}{self.entered}",fill=colored[i],outline=colored[i])
            self.canvas.itemconfigure(f"text{i}{self.entered}",fill="white")
            cur = self.keyboard.itemcget("key_"+guess[i],"fill")
            if cur == self.Green:
                continue
            if colored[i] ==self.Green:
                self.keyboard.itemconfigure("key_"+guess[i],fill=self.Green)
            elif colored[i]== self.Yellow and cur != self.Green:
                self.keyboard.itemconfigure("key_"+guess[i],fill=self.Yellow)
            elif colored[i]== self.Gray and cur =="#545454":
                self.keyboard.itemconfigure("key_"+guess[i], fill=self.Gray)
            if colored[i] == self.Green:
                self.singlelinebox.itemconfigure(f"givehintletter{i}", text=guess[i])
                self.singlelinebox.itemconfigure(f"hint{i}", fill=self.Green, outline=self.Green)
        won = colored.count(self.Green) ==self.wordlength
        self.entered+= 1
        self.textField=""
        if won or self.entered >=self.maxguesses:
            self.frozen =True
            self.goingtotheresultpage(won)
#the hint button that gives hint by telling the user what lettter appears in what locaiton in the singlelinebox function
    def givehint(self, event=None):
        for i in range(self.wordlength):
            current = self.singlelinebox.itemcget(f"givehintletter{i}", "text")
            if current == "":
                self.singlelinebox.itemconfigure(f"givehintletter{i}", text=self.word[i])
                self.singlelinebox.itemconfigure(f"hint{i}", fill=self.Green, outline=self.Green)
                self.after(2000, lambda i=i: self.clearhint(i))
                return
#this is more of a personal choice where the hint goes away after a bit, so that the hint is like a mini clue they can get but then it fades so they still "get" feeling of doing it idk
    def clearhint(self, i):
        fill = self.singlelinebox.itemcget(f"hint{i}", "fill")
        if fill == self.Green:
            self.singlelinebox.itemconfigure(f"givehintletter{i}", text="")
            self.singlelinebox.itemconfigure(f"hint{i}", fill="#3D3D3D", outline="#6E6E6E")

    def showhelppage(self):
        self.helppagebox.place(relx=0.5, rely=0.5, anchor="center")
        self.helppagebox.lift()
        self.helppageclose.place(relx=0.715, rely=0.12, anchor="center")
        self.helppageclose.lift()

    def goingtotheresultpage(self, won):
        self.unbind_all("<Key-BackSpace>")
        self.unbind_all("<Key-Return>")
        self.unbind_all("<Key>")
        self.after(1000, lambda:self.app.showresultpage(won=won,word=self.word,guesses=self.entered))

    def closehelppage(self, event=None):
        self.helppagebox.place_forget()
        self.helppageclose.place_forget()

class StellaVerbaResultPage(Frame):
    def __init__(self, master,won,word,guesses,app):
        Frame.__init__(self, master, bg="white")
        self.master = master
        self.app = app
        self.pack(fill="both", expand=True)
        self.shortcut = Path(__file__).parent
        self.img = self.shortcut / "images"

        self.bgimage = PhotoImage(file=str(self.img / ("dbg2.png" if app.mode == "darkmode" else "lbg2.png")))
        self.bglabel = Label(self, image=self.bgimage, bd=0)
        self.bglabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.resultpagebox = tk.Frame(self, bg="#2E2E2E", bd=0)
        self.resultpagebox.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.78)
        if won:
            message = "Congratulations"
            colourofendingmessage = "#6AAA64"
        else:
            message = "Better Luck Next Time"
            colourofendingmessage = "#C7141F"

        self.resulttext = tk.Label(self.resultpagebox, text=message, font=("Rubik Bubbles", 30),bg="#2E2E2E", fg=colourofendingmessage)
        self.resulttext.pack(pady=(40, 10))
        self.divider = tk.Frame(self.resultpagebox, bg="#555555", height=2)
        self.divider.pack(fill="x", padx=30, pady=(0, 15))

        self.thewordistext = tk.Label(self.resultpagebox, text="The word is:", font=("Inter", 16),bg="#2E2E2E", fg="#AAAAAA")
        self.thewordistext.pack(pady=(0, 5))

        self.revealwordtext = tk.Label(self.resultpagebox, text=word.upper(), font=("Inter", 40, "bold"), bg="#2E2E2E", fg="white")
        self.revealwordtext.pack(pady=(0, 5))
        #shows the user the amount of trials they did and if they won
        if won:
            self.amountofguessestext = tk.Label(self.resultpagebox, text=f"You got it in {guesses} guess{'es' if guesses != 1 else ''}!", font=("Inter", 14), bg="#2E2E2E", fg="#AAAAAA")
            self.amountofguessestext.pack(pady=(0, 20))
        definition = Definitions.get(word.lower(), "No definition available.")
        self.definitionbox = tk.Frame(self.resultpagebox, bg="#545454", bd=0)
        self.definitionbox.pack(padx=30, pady=(0, 30), fill="x")
        self.fontofthedefiniton = tk.Label(self.definitionbox, text=definition, font=("Inter", 9),bg="#545454", fg="white", wraplength=480, justify="center")
        self.fontofthedefiniton.pack(padx=20, pady=20)
        self.delandenterbutton = tk.Frame(self.resultpagebox, bg="#2E2E2E")
        self.delandenterbutton.pack(pady=(0, 40))
        self.playagainbutton = tk.Button(self.delandenterbutton, text="Play Again", font=("Inter", 16, "bold"), bg="#CCC751", fg="white", bd=0, relief="flat", cursor="hand2", activebackground="#7BBB75", activeforeground="white", command=self.playagain)
        self.playagainbutton.pack(side="left", padx=20, ipadx=20, ipady=10)
        self.exitbutton = tk.Button(self.delandenterbutton, text="Exit", font=("Inter", 16, "bold"),bg="#CCC751", fg="white", bd=0, relief="flat", cursor="hand2",activebackground="#D81212", activeforeground="white",command=self.master.winfo_toplevel().destroy)
        self.exitbutton.pack(side="left", padx=20, ipadx=20, ipady=10)

    def playagain(self):
        self.app.displayingtheresults(won=None, word=None, guesses=None)

def displayingtheresults(self, won, word, guesses):
    if hasattr(self, "gameframeofwordle"):
        self.gameframeofwordle.destroy()
    self.Home.pack(fill="both", expand=True)