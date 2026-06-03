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
        totalboxwidth = 6*size*5*gap
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

        lastrowofkeyboard = startingatyaxis + 4 * (size * height * gap)
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
        self.boxes_coord["Delete key"] = (deletebuttonleftside, lastrowofkeyboard - size*height/2,deletebuttonrightside, lastrowofkeyboard + size*height/2)
        self.create_rectangle(yonaxis - size / 2, lastrowofkeyboard - size * height / 2,yonaxis + size / 2, lastrowofkeyboard + size * height / 2,width=0, fill=LetterButtonColour, tags=("key_Y", "letter"))
        self.create_text(yonaxis, lastrowofkeyboard,text="Y", font=("Inter", 18, "bold"),fill="white", tags=("letter", "label Y BUtton"))
        self.boxes_coord["Y key"] = (yonaxis - size / 2, lastrowofkeyboard - size * height / 2, yonaxis + size / 2,lastrowofkeyboard + size * height / 2)
        self.create_rectangle(zonaxis - size / 2, lastrowofkeyboard - size * height / 2, zonaxis + size / 2,lastrowofkeyboard + size * height / 2, width=0, fill=LetterButtonColour,tags=("key Z", "letter"))
        self.create_text(zonaxis, lastrowofkeyboard, text="Z", font=("Inter", 18, "bold"), fill="white",tags=("letter", "Z Button"))
        self.boxes_coord["Z key"] = (zonaxis - size / 2, lastrowofkeyboard - size * height / 2, zonaxis + size / 2,lastrowofkeyboard + size * height / 2)
        self.create_rectangle(enterbuttonleftside, lastrowofkeyboard - size * height / 2, enterbuttonrightside,lastrowofkeyboard + size * height / 2, width=0, fill=LetterButtonColour,tags=("enter", "enter button"))
        self.create_text(enterbuttonmiddleside, lastrowofkeyboard, text="ENTER", font=("Inter", 12, "bold"),fill="white", tags=("enter", "enterbutton"))
        self.boxes_coord["Enter key"] = (enterbuttonleftside, lastrowofkeyboard - size * height / 2,enterbuttonrightside, lastrowofkeyboard + size * height / 2)

        self.tag_bind("letter", "<Button>",self.push_button)
        self.tag_bind("enter", "<Button>", lambda e:self.master.submit)
        self.tag_bind("back", "<Button>", lambda e:self.master.back)

        def push_button(self, key=None):
            for tag in self.boxes_coord:
                if tag in ("Delete key", "Enter key"):
                    continue
                x1, y1, x2, y2 = self.boxes_coord[tag]
                if x1 <= key.x <= x2 and y1 <= key.y <= y2: self.master.allow_letter_type(tag[-1])
                return

        int(self["width"]) / 2 - x, y - height * size / 2,int(self["width"]) / 2 - x + LetterButtonSize, y + height * size / 2,width=0, fill=LetterButtonColour, tag=("enter", "key_enter"))
        self.show_text(int(self["width"]) / 2 - x + LetterButtonSize / 2, y, text="ENTER",font=("Inter", 9, "bold"), tag=("enter", "label_enter"))

        self.letter_rectangle_create(int(self["width"]) / 2 + x - LetterButtonSize, y - height * size / 2,int(self["width"]) / 2 + x, y + height * size / 2,width=0, fill=LetterButtonColour, tag=("back", "key_back"))
        self.show_text(int(self["width"]) / 2 + x - LetterButtonSize / 2, y, text="BACK",font=("Inter", 9, "bold"), tag=("back", "label_back"))



class StellaVerbaGamePage:
    def __int__(self,master):
        Frame.__init__(self,master,bg="black")
        self.master=master
        self.grid()

        top=60
        self.canvas=Canvas(self,bg="black",width=370,height=415+top,highlightthickness=0)
        self.canvas.grid(row=2,column=1)

        self.canvas.create_text(370/2,top/2-10,text="Wordle",font=("Inter",30,"bold"))
        self.keyboard = Physical_DigitalKeyboard(self)

        self.spacer1 = Canvas(self,bg="black",width=50,height=10,highlightthickness=0)
        self.spacer2 = Canvas(self,bg="black",width=50,height=10,highlightthickness=0)
        self.spacer1.grid(row=1,column=0)
        self.spacer2.grid(row=1,column=2)
        self.sep=ttk.Separator(self,orient=HORIZONTAL)
        self.sep.grid(row=0,column=0,columnspan=3,sticky=E+W)

        answers = open("easy.txt")
        self.answers = answers.read().split()
        answers.close()
        words = open("easy.txt")
        self.words = words.read().split()
        words.close()

        self.textField = ""
        self.entered = 0
        self.frozen = False

        for x in range(5):
            for y in range(6):
                self.canvas.letter_rectangle_create(x*68+20,y*68,x*68+80,y*68+60+top,outline="black",tag=f"cell{x}{y}")
                self.canvas.show_text(x * 68 + 50, y * 68 + 30 + top, text="", font=("Inter", 30, "bold"),tag=f"text{x}{y}")

        self.WordChoice=random.choice(self.answers)
        self.word=self.WordChoice
        self.Gray=""
        self.Green=""
        self.Yellow=""
        self.bind_all("<Key-BackSpace>", self.back)
        self.bind_all("<Key-Return>", self.submit)
        self.bind_all("<Key>", self.type_letter)
#Function that allows the letter to be deleted from the answering box thing
    def delete_letter(self,event=None):
        if len(self.textField)==0 and self.entered>=6:
            return
        self.textField=self.textField[:-1]

        self.canvas.itemconfigure(f"text{len(self.textField)}{self.entered}",text="")

    def subitanswerchoice(self,event=None):
        if self.textField.lower() not in self.words:
            self.invalid_word_show()
            return
        if len(self.textField) <5 or self.entered>=6:
            return
        colored=[False for i in range(5)]
        letterCount = {}
        for char in self.textField:
            letterCount[char]=0

        for i in range(5):
            letter = self.textField[i]
            if letter == self.word[i]:
                self.canvas.itemconfigure(f"cell{i}{self.entered}", fill=self.Green)
                self.keyboard.itemconfigure("key_" + letter, fill=self.Green)
                letterCount[letter] += 1
                colored[i] = True

                # color cells and keyboard yellow
        for i in range(5):
            letter = self.textField[i]
            if letter != self.word[i] and letter in self.word and \
                letterCount[letter] < self.word.count(letter):
                self.keyboard.itemconfigure("key_"+letter, fill=self.YELLOW)
                self.canvas.itemconfigure(f"cell{i}{self.entered}", fill=self.YELLOW)
                letterCount[letter] += 1
                colored[i] = True
            elif letterCount[letter] >= self.word.count(letter) and not colored[i]:
                self.canvas.itemconfigure(f"cell{i}{self.entered}", fill=self.GRAY)
                self.keyboard.itemconfigure("key_"+letter, fill=self.GRAY)

        if self.word.upper() ==self.textField.upper():
            self.frozen=True
            self.result_display()

        elif self.entered==5:
            self.result_display()
            self.entered+=1
            self.textField=""
    def allow_letter_type(self,event):
        if len(self.textField)>=5 or self.frozen:
            return
        if isinstance(event,str):
            letter=event
        else:
            letter=event.char.lower()
        if not letter.isalpha():
            return
        self.canvas.itemconfigure(f"text{len(self.textField)}{self.entered}", text=letter.upper())
        self.textField += letter

    def not_available_word_showing(self):

        self.canvas.create_rectangle(185 - 80, 35 - 18, 185 + 80, 35 + 18, fill="#a00", tag="invalid", width=0)
        self.canvas.create_text(185, 35, text="Invalid word.", font=("Inter", 12), fill="white", tag="invalid")
        self.after(1500, self.invalid_word_hide)

    def not_available_word_hiding(self):
        self.canvas.delete("Invalid")

    def win_display(self):
        if self.entered == 0:
            tries = "try"
        else:
            tries = "tries"
        x, y = 185, 260
        self.canvas.create_rectangle(x - 150, y - 50, x + 150, y + 50, fill="#white")
        self.canvas.create_text(x - 140, y - 20, text="Congratulation! You guessed '" + self.word.upper() + "'\nin " + \
        str(self.entered + 1) + " " + tries + ".", font=("Inter", 12),anchor=W)
        self.button = Button(text="New Wordle", relief="flat", font=("Inter", 10, "bold"), command=self.restart_game,bg=self.Green, fg="white")
        self.canvas.create_window(x, y + 23, window=self.button)

    def lose_display(self):
        x, y = 185, 260
        self.canvas.create_rectangle(x - 150, y - 50, x + 150, y + 50, fill="#fff")
        self.canvas.create_text(x - 140, y - 20,text="Sorry, you ran out of tries. The word was\n'" + self.word.upper() + "'.",font=("Arial", 12), anchor=W)\

        self.button = Button(text="Play Again",relief="flat",font=("Inter",25,"bold"),command=self.restart_game,bg="red",fg="white")

    def play_again_function (self):
        self.grid_remove()
        self.__init__(self.master)
root=Tk()
root.configure(bg="white")
root.title("Wordle")
StellaVerbaGamePage(root)


































