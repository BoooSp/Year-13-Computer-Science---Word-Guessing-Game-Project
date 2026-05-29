from tkinter import *
import tkinter.ttk as ttk
import random, time


# the class for the keyboard function of my game page
class Physical_DigitalKeyboard(Canvas):
    def __init__(self,master):
        Canvas.__init__(self,master,bg="black",highlightthickness=0,width=420,height=170)
        self.master = master
        self.grid(row=3,column=1,sticky=N)

        self.Keyboard_letter_boxes = ["ABCDEF","GHIJKL","MNOPQR","STUVWX","YZ"]
        size = 35
        height=1.3
        buffer=size/6
        self.layoutkeys={}

        LetterButtonColour = "#545454"
        UsedLetterButtonColour = "#545454"

        for i in range(3):
            boxes = self.Keyboard_letter_boxes[i]
            for char in boxes:
                x,y=int(self["width"])/2+(size+buffer)*(boxes.find(char)-(len(boxes)-1)/2),height*size/2+i*(height*size+buffer)+buffer
                self.box_rectangle_shapes(x-size/2, y-height*size/2, x+size/2, y+height*size/2, width=0,fill=LetterButtonColour, tags=("key_"+char, "letter"))
                self.show_text(x, y, text=char.upper(), font=("Inter", 13, "bold"),tag=("letter", "label_" + char.upper()))
                self.boxes_cord["key_" + char] = (x - size / 2, y - height * size / 2, x + size / 2,y + height * size / 2)

                LetterButtonSize = (3*size+buffer)/2
                x,y = (10*size+9*buffer)/2, height*size/2+2*(height*size+buffer)+buffer

                self.letter_rectangle_create(int(self["width"]) / 2 - x, y - height * size / 2,int(self["width"]) / 2 - x + LetterButtonSize, y + height * size / 2,width=0, fill=LetterButtonColour, tag=("enter", "key_enter"))
                self.show_text(int(self["width"]) / 2 - x + LetterButtonSize / 2, y, text="ENTER",font=("Inter", 9, "bold"), tag=("enter", "label_enter"))

                self.letter_rectangle_create(int(self["width"]) / 2 + x - LetterButtonSize, y - height * size / 2,int(self["width"]) / 2 + x, y + height * size / 2,width=0, fill=LetterButtonColour, tag=("back", "key_back"))
                self.show_text(int(self["width"]) / 2 + x - LetterButtonSize / 2, y, text="BACK",font=("Inter", 9, "bold"), tag=("back", "label_back"))

                self.tag_bind("letter","<Button>",self.push_button)
                self.tag_bind("enter","<Button>",self.master.submit)
                self.tag_bind("back","<Button>",self.master.back)

                def push_button(self, key=None):
                    for tag in self.boxes_cord:
                        if self.boxes_cord[tag][0] <= key.x <= self.boxes_cord[tag][2] and \
                                self.boxes_cord[tag][1] <= key.y <= self.boxes_cord[tag][3]:
                            self.master.type_letter(tag[-1])
                            return

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


































