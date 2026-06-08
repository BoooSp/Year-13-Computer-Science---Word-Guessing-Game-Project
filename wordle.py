from tkinter import *
import tkinter.ttk as ttk
import urllib.request
import threading
import random

# list of words for each mode (making it 4/5/6 letter for each mode)
Wordsforthegame = {"easy":["easy"],"medium":["stare"],"hard":["failed"],}

# how many letters and guesses per difficulty
wordlength_eachdifficulty = {"easy": 4, "medium": 5, "hard": 6}
guessinglimits = {"easy": 6, "medium": 6, "hard": 6}

#Colours i left here for now
Green  = "#6aaa64"
Yellow = "#c9b458"
Grey   = "#787c7e"

def checkifrealword(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}"
    try:
        req = urllib.request.Request(url,headers={"User-Agent": "StellaVerba"})
        urllib.request.urlopen(req, timeout=4)
        return True
    except:
        return False
# the class for the keyboard function of my game page
class Physical_DigitalKeyboard(Canvas):
    def __init__(self,master):
        Canvas.__init__(self,master,bg="black",highlightthickness=0,width=600,height=737)
        self.master = master
        self.place(x=0, y=0)

        self.Keyboard_letter_boxes = ["ABCDEF","GHIJKL","MNOPQR","STUVWX","YZ"]
        size = 60
        height=1
        gap=10
        LetterButtonColour = "#545454"
        self.layoutkeys={}
        self.boxes_coord={}
        totalboxwidth = 6*size*5+gap
        leftside=300-totalboxwidth/2
        rightside=300+totalboxwidth/2
        startingatyaxis=150

        for i in range(4):
            boxes = self.Keyboard_letter_boxes[i]
            for char in boxes:
               col=boxes.find(char)
               x = 300 + (size + gap) * (col- (len(boxes) - 1) / 2)
               y = startingatyaxis + i * (size * height + gap)
               self.create_rectangle(x -size/2,y-size*height/2,x+size/2,y+size*height/2,width=0,fill=LetterButtonColour, tags=("key_" + char, "letter"))
               self.create_text(x, y, text=char, font=("Inter", 18, "bold"), fill="white",tags=("letter", "label_" + char))
               self.boxes_coord["key_" + char]=(x-size/2,y-size*height/2,x+size/2,y+size*height/2)

        lastrowofkeyboard = startingatyaxis + 4 * (size * height + gap)
        yonaxis = 300-(size+gap)/2
        zonaxis=300+(size+gap)/2
        deletebuttonleftside  = leftside
        deletebuttonrightside = yonaxis- size/2 - gap
        deletebuttonmiddle= (deletebuttonleftside + deletebuttonrightside) / 2


        enterbuttonleftside  = zonaxis+size/2+gap
        enterbuttonrightside = rightside
        enterbuttonmiddleside= (enterbuttonleftside + enterbuttonrightside) / 2

#The last line of buttons on the keyboard has to be done seperately because they are not same shaped (its huering my head ;-;)
        self.create_rectangle(deletebuttonleftside, lastrowofkeyboard - size*height/2,deletebuttonrightside, lastrowofkeyboard + size*height/2,width=0, fill=LetterButtonColour, tags=("back", "key_back"))
        self.create_text(deletebuttonmiddle, lastrowofkeyboard,text="DELETE", font=("Inter", 12, "bold"),fill="white", tags=("delete", "deletebutton"))
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

    def push_button(self, key=None):
        for tag in self.boxes_coord:
            if tag in ("Delete key", "Enter key"):
                    continue
            x1,y1,x2,y2 = self.boxes_coord[tag]
            if x1<=key.x<=x2 and y1 <=key.y <= y2:
                self.master.allow_letter_type(tag[-1])
            return

        self.tag_bind("letter", "<Button>",self.push_button)
        self.tag_bind("enter", "<Button>", lambda e:self.master.subitanswerchoice())
        self.tag_bind("back", "<Button>", lambda e:self.master.deletetheletter())

class StellaVerbaGamePage(Frame):
    def __init__(self,master,difficulty,app):
        Frame.__init__(self,master,bg="white")
        self.master=master
        self.app=app
        self.pack(fill="both", expand=True)

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

        self.keyboard=Physical_DigitalKeyboard(self)
        cell=68
        gap=6
        padding=40
        answerletterboxwitdth= self.wordlength*cell+(self.wordlength-1)*gap
        answerletterboxheight=self.maxguesses*cell+(self.maxguesses-1)*gap
        ansboxsx=600+(600-answerletterboxwitdth)//2
        ansboxsy=(737-answerletterboxheight)//2
        self.ansboxbg=Canvas(self ,bg="#E8E8E8",highlightthickness=0,width=answerletterboxwitdth+padding*2, height=answerletterboxheight+padding*2)
        self.ansboxbg.place(x=ansboxsx-padding,y=ansboxsy-padding)
        self.canvas=Canvas(self ,bg="white",width=answerletterboxwitdth,height=answerletterboxheight,highlightthickness=0)
        self.canvas.place(x=ansboxsx,y=ansboxsy)

        for x in range(self.wordlength):
            for y in range(self.maxguesses):
                xx = x * (cell + gap)
                yy = y * (cell + gap)
                self.canvas.create_rectangle(xx,yy,xx+cell,yy+cell,outline="black",width=2,tag=f"cell{x}{y}")
                self.canvas.create_text(xx+cell//2,yy+cell//2, text="", font=("Inter", 30, "bold"),tag=f"text{x}{y}")



        self.WordChoice=random.choice(self.answers).upper()
        self.word=self.WordChoice
        self.Gray=Grey
        self.Green=Green
        self.Yellow=Yellow
        self.bind_all("<Key-BackSpace>", self.deletetheletter)
        self.bind_all("<Key-Return>", self.subitanswerchoice)
        self.bind_all("<Key>", self.master.allow_letter_type)



#Function that allows the letter to be deleted from the answering box thing
    def deletetheletter(self,event=None):
        if self.frozen or self.checking or len(self.textField)==0:
            return
        self.textField=self.textField[:-1]
        self.canvas.itemconfigure(f"text{len(self.textField)}{self.entered}",text="")

    def subitanswerchoice(self,event=None):
        if self.frozen or self.checking:
            return
        if len(self.textField) <self.wordlength or self.entered>=self.maxguesses:
            return
            self.checking = True
            threading.Thread(target=self.checkingboforethescoring, daemon=True).start()

    def checkingboforethescoring(self):
        #fix this
        valid = checkifrealword(self.textField)
        self.after(0,lambda: self.afterthechecking(valid))

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
        won = colored.count(self.Green) ==self.wordlength
        self.entered+= 1
        self.textField=""
        if won or self.entered >=self.maxguesses:
            self.frozen =True
            self.goingtotheresultpage(won)

    def goingtotheresultpage(self, won):
        self.unbind_all("<Key-BackSpace>")
        self.unbind_all("<Key-Return>")
        self.unbind_all("<Key>")
        self.app.displayingtheresults(won=won,word=self.word,guesses=self.entered)



class trasnitioning:
    def displayingtheresults(self, won, word, guesses):
        print(f"won={won}, word={word}, guesses={guesses}")




















