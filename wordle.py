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
                self.show_text(int(self["width"]) / 2 - x + LetterButtonSize / 2, y, text="ENTER",font=("Arial", 9, "bold"), tag=("enter", "label_enter"))

                self.letter_rectangle_create(int(self["width"]) / 2 + x - LetterButtonSize, y - height * size / 2,int(self["width"]) / 2 + x, y + height * size / 2,width=0, fill=LetterButtonColour, tag=("back", "key_back"))
                self.show_text(int(self["width"]) / 2 + x - LetterButtonSize / 2, y, text="BACK",font=("Arial", 9, "bold"), tag=("back", "label_back"))

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

















