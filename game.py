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
        "idea": "Thought/suggestion - That's a great idea, lets go to the beach\nA purpose/goal - The idea is to win by having the most points",
        "view": "Something you can see - The mountain view is amazing\nAn opinion - That's my view on ice cream flavours",
        "fact": "Something that is true -Humans die and that's a fact\nInformation that can be proven - Check the facts, smoking causes lung cancer",
        "goal": "Something you want to achieve - My goal is to pass the internal with excellence\nA point scored in sport - She scored a goal by herself",
        "role": "A person's job or purpose - Everyone has a role in this world\nA character in a play or film - He played the lead role as the prince",
        "plan": "An idea for what to do - We made a plan on how to reach antarctica\nTo organise ahead - Let's plan the trip to the Bahamas",
        "term": "A word with a special meaning - Aqueous is a chemistry term\nA school period - Next term is going to start in 3 days.",
        "item": "A single object - Pick up that ball behind the fence \nOne thing on a list - First item to buy is butter",
        "base": "The bottom of something - The base of the house is strong\nA main place - Our base is near the beach",
        "gain": "To get something - She gained confidence to speak to the crowd\nAn increase - A small gain in knowledge",
        "loss": ":Lost something - The loss of her puppy was upsetting\nMoney lost - The business made a loss of 20 million dollars",
        "rule": "Something you must follow - Follow the rules in the kitchen\nTo control - The queen ruled the country for 30 years",
        "mean": "To have a meaning - What does this book mean?\nUnkind - Don't be mean to your sister",
        "rank": "A position in order - First rank in swimming",
        "feel": "To have an emotion - I feel happy because I got a new book \nTo touch - Feel the fabric of the dress I am wearing",
        "theme": "The main idea - The theme of this book is about how friendship prevails all\nA style or topic - The movie we are watching is a pirate themed one",
        "issue": "A problem - There's an issue, the pipes are broken\n Publish or release: We need to issue you a new debit card",
        "valid": "Reasonable or correct - Breaking your hand is a valid reason to not sit the exam\nStill usable - The gift card is valid until the december of next year",
        "logic": "Clear reasoning - Use logic to solve this mathematics equation\nA sensible way of thinking - Good logic on bringing scarfs in this weather",
        "claim": "To say something is true - He claimed that he can run the fastest\nA statement - That's a big claim to say everyone except you sucks",
        "value": "How important something is - I value love over money \nHow much something is worth - The value of gold has increased exponentially",
        "adapt": "To change for a new situation - Adapt quickly to this weather\nTo change into another form - The book was adapted into a movie",
        "focus": "Main attention - Stay focused on your task\nTo concentrate - Our main focus is to write this book",
        "trend": "A common change - A growing trend has been seen of children’s reading capability increasing \nSomething popular - Jeans are the latest trend",
        "civil": "Polite - Can we keep it civil and not argue\nRelated to society - It is a civil right to vote whether your a man or a woman",
        "shift": "To move -  could you shift your chair a little more to the right\nA change - A big shift in the pH scale",
        "cause": "The reason - The cause of our books being wet was the rain\nTo make happen - The heavy rain caused there to be a flood in the neighbourhood",
        "proof": "Evidence - Show me proof that you didn’t cheat",
         "image": "A picture - Nice image of the ocean\nHow others see you - You have to maintain your public image as a model",
        "grant": "Money given to help - A research grant was given to the high school student\nTo allow - Permission granted to enter the laboratory",
        "impact": "A strong effect - The war had a big impact in the economy\nA collision - The impact of the car crash was loud",
        "theory": "An explanation - A scientific theory\nA set of ideas - Music theory",
        "review": "To check again - Review your work to make sure there is no grammar issues\nAn opinion - my review on the movie is that it was horrible",
        "debate": "A discussion with different opinions - The group debated on how to win the game\nTo argue different sides - They debated on who deserves the inheritance",
        "select": "To choose - Select an prize out of these three options\nChosen carefully - A select group to go with you",
        "create": "To make something - He created a poster for the parade\nTo cause - The change in school system created problems",
        "survey": "A set of questions - please complete the survey so that we may know your opinion\nTo look over - Could you survey the area to make sure it’s safe",
        "assess": "To judge - The teacher next door is going to assess our work\nTo work out value - He is going to the damage done to their house",
        "expand": "To grow bigger - Expand the business to worldwide\nTo add more detail - Could you expand your answer a bit more",
        "symbol": "Something that represents something - The heart is a symbol for their undying love\nA special character - The % is a symbol for percentages",
        "motive": "A reason for doing something - His motive is to win the game\nWhat drives actions - Find the motive that caused the character to go mad",
        "policy": "A set of rules - it is school policy to wear black socks",
          "crisis": "A serious problem - After the trip we were in a financial crisis",
        "effort": "Trying hard - Great effort was placed into creating the project\nThe energy needed - It takes effort to pass this exam",
        "enable": "To make possible - Enable notifications so that you will be notified\nTo help someone do something - The donation enabled them to get into university",
        "factor": "Something that affects a result - A key factor in ocean acidification is carbon dioxide\nA number that divides another - 5 is a factor of 20",
        "status": "Current situation - Her status is currently in critical condition \nA person's position - Aristocrats had high status compared to the farmers",
        "inform": "To tell someone - Inform your teacher that you got to leave the class\nTo help someone decide - The facts informed us that we should look both ways before crossing the road", }


# how many letters and guesses per difficulty
Word_length_for_each_difficulty = {"easy": 4, "medium": 5, "hard": 6} # the word lengths for each of the difficulty
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
    def __init__(self,master,background_images):
        Canvas.__init__(self,master,highlightthickness=0,width=600,height=737) #canvas for the keyboard design that I created to place in my design
        self.master = master
        self.place(x=0, y=0)
        self.create_image(0, 0, image=background_images, anchor="nw")


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
        at_y_on_axis=300
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
               y = at_y_on_axis + i * (size * height + gap)
               self.create_rectangle(x -size/2,y-size*height/2,x+size/2,y+size*height/2,width=0,fill=letter_button_colour, tags=("key_" + char, "letter"))
               self.create_text(x, y, text=char, font=("Inter", 18, "bold"), fill="white",tags=("letter", "label_" + char))
               self.boxes_coord["key_" + char]=(x-size/2,y-size*height/2,x+size/2,y+size*height/2)

#last row has different shapes so the sizing has to be different
        last_row_of_keyboard = at_y_on_axis + 4 * (size * height + gap)
        y_on_axis = 300-(size+gap)/2
        z_on_axis=300+(size+gap)/2
        left_side_of_delete_button  = left_side
        right_side_of_delete_button = y_on_axis- size/2 - gap
        middle_of_delete_button= (left_side_of_delete_button + right_side_of_delete_button) / 2

#the ends of the last line so that it fits inside the box shape of my plan of the keyboard shape
        left_side_of_enter_button  = z_on_axis+size/2+gap
        right_side_of_enter_button = right_side
        middle_of_enter_button= (left_side_of_enter_button + right_side_of_enter_button) / 2

#The last line of buttons on the keyboard has to be done separately because they are not same shaped
        self.create_rectangle(left_side_of_delete_button, last_row_of_keyboard - size*height/2,right_side_of_delete_button, last_row_of_keyboard + size*height/2,width=0, fill=letter_button_colour, tags=("back", "key_back"))
        self.create_text(middle_of_delete_button, last_row_of_keyboard,text="DELETE", font=("Inter", 12, "bold"),fill="white", tags=("delete", "delete_button","back"))
        self.boxes_coord["Delete key"] = (left_side_of_delete_button, last_row_of_keyboard -size*height/2,right_side_of_delete_button, last_row_of_keyboard + size*height/2)
        self.create_rectangle(y_on_axis - size / 2, last_row_of_keyboard - size * height / 2,y_on_axis + size / 2, last_row_of_keyboard + size * height / 2,width=0, fill=letter_button_colour, tags=("key_Y", "letter"))
        self.create_text(y_on_axis, last_row_of_keyboard,text="Y", font=("Inter", 18, "bold"),fill="white", tags=("letter", "label Y Button"))
        self.boxes_coord["Y"] = (y_on_axis - size / 2, last_row_of_keyboard - size * height / 2, y_on_axis + size / 2,last_row_of_keyboard + size * height / 2)
        self.create_rectangle(z_on_axis - size / 2, last_row_of_keyboard - size * height / 2, z_on_axis + size / 2,last_row_of_keyboard + size * height / 2, width=0, fill=letter_button_colour,tags=("key_Z", "letter"))
        self.create_text(z_on_axis, last_row_of_keyboard, text="Z", font=("Inter", 18, "bold"), fill="white",tags=("letter", "Z Button"))
        self.boxes_coord["Z"] = (z_on_axis - size / 2,last_row_of_keyboard - size * height / 2, z_on_axis + size / 2,last_row_of_keyboard + size * height / 2)
        self.create_rectangle(left_side_of_enter_button, last_row_of_keyboard - size * height / 2, right_side_of_enter_button,last_row_of_keyboard + size * height / 2, width=0, fill=letter_button_colour,tags=("enter", "enter button"))
        self.create_text(middle_of_enter_button, last_row_of_keyboard, text="ENTER", font=("Inter", 12, "bold"),fill="white", tags=("enter", "enter_button"))
        self.boxes_coord["Enter key"] = (left_side_of_enter_button, last_row_of_keyboard - size * height / 2,right_side_of_enter_button, last_row_of_keyboard + size * height / 2)

#allows the buttons to be pushed and pressed as well as the delete and the enter button
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
        self.background_images = PhotoImage(file=str(self.img / ("dbg1.png" if app.mode == "dark_mode" else "lbg1.png")))
        self.bg_label = Label(self, image=self.background_images, bd=0)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        #the go back function that appears in the top left corner of the game page
        self.Go_back_to_home_page_button = tk.Button(self, text="<-- Back", font=("Inter", 14, "bold"), command=self.app.go_back_to_difficulty_page,bg="#545454", fg="white", bd=0, cursor="hand2")
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


        self.keyboard=physical_and_digital_keyboard(self,self.background_images)
        self.Go_back_to_home_page_button.lift()
        cell=68
        gap=6
        padding=40
        answer_box_width= self.Word_length*cell+(self.Word_length-1)*gap
        answer_box_height=self.Max_guesses*cell+(self.Max_guesses-1)*gap
        answer_box_x_axis=600+(600-answer_box_width)//2
        answer_box_y_axis=(737-answer_box_height)//2

        #Code for the line function including help button, hint_button and the line of the final answer box

        centre_of_keyboard = 300
        single_line_function = 115
        single_line_function_x_axis = centre_of_keyboard - answer_box_width // 2
        #The line that separates from the keyboard and the single line function
        self.separation_line_of_keyboard_and_answer_box = Canvas(self, bg="#555555", highlightthickness=0, height=2, width=560)
        self.separation_line_of_keyboard_and_answer_box.place(x=20, y=single_line_function + cell + 15)

        self.Single_line_of_boxes = Canvas(self, bg="#3D3D3D", width=answer_box_width, height=cell, highlightthickness=0)
        self.Single_line_of_boxes.place(x=single_line_function_x_axis, y=single_line_function)
        for i in range(self.Word_length):
            xx = i * (cell + gap)
            self.Single_line_of_boxes.create_rectangle(xx, 0, xx + cell, cell, outline="#6E6E6E", width=2,tags=(f"hint{i}",))
            self.Single_line_of_boxes.create_text(xx + cell // 2, cell // 2, text="", font=("Inter", 30, "bold"), fill="white",tags=(f"give_hint_letter{i}",))


        #hint button image and stuffs
        self.hint_button_image = PhotoImage(file=str(self.img / "lightbulb.png"))
        self.hint_button = Label(self, image=self.hint_button_image, bd=0, cursor="hand2")
        self.hint_button.place(x=single_line_function_x_axis - 80, y=single_line_function, width=cell, height=cell)
        self.hint_button.bind("<ButtonRelease-1>", self.give_hint)

#the help and documentation page button and the image that appears when it is pressed
        self.Help_button = tk.Button(self, text="?", font=("Inter", 20, "bold"), cursor="hand2",bd=0, relief="flat", bg="#545454", fg="white",activebackground="#6a6a6a", activeforeground="white",command=self.show_help_page)
        self.Help_button.place(x=single_line_function_x_axis + answer_box_width + 20, y=single_line_function, width=cell,height=cell)

        self.Help_image = PhotoImage(file=str(self.img / "helpimg.png"))
        self.Help_image_box = Label(self, image=self.Help_image, bd=0)
        self.Help_image_close = Label(self, text="✕", font=("Inter", 14, "bold"), cursor="hand2", bg="#C7141F", fg="white")
        self.Help_image_close.bind("<ButtonRelease-1>", self.close_help_page)

#the box that the user enters the letters in like how it would be in wordle
        self.Answer_box_background=Canvas(self ,bg="#2A2A2A",highlightthickness=0,width=answer_box_width+padding*2, height=answer_box_height+padding*2)
        self.Answer_box_background.place(x=answer_box_x_axis-padding,y=answer_box_y_axis-padding)
        self.canvas=Canvas(self ,bg="#3D3D3D",width=answer_box_width,height=answer_box_height,highlightthickness=0)
        self.canvas.place(x=answer_box_x_axis,y=answer_box_y_axis)
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
            self.show_error_pop_up(f"Not enough letters")
            return
        if self.entered>=self.Max_guesses:
            return
        self.checking = True
        threading.Thread(target=self.checking_before_the_scoring, daemon=True).start()
#the code that allows the user to enter the letters from the keyboard
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
#the code checks the answer the user enters before confirming anything
    def checking_before_the_scoring(self):
        #fix this
        valid = check_if_real_word(self.textField)
        self.after(0,lambda: self.after_the_checking(valid))
#after it has checked the thing it would determine if it does not meet the criteria to be considered as a proper guess then one of the errors would pop up
    def after_the_checking(self, valid):
        self.checking = False
        if not valid:
            self.show_error_pop_up("Word doesn't exist")
            return
        if self.textField in self.word_already_used:
            self.show_error_pop_up("Word has already been used")
            return
        self.word_already_used.append(self.textField)
        self.scoring_the_guess()


    def show_error_pop_up(self, message):
        self.popup.config(text=message)
        self.popup.lift()
        self.popup.place(relx=0.5,y=20,anchor="n")
        self.after(1500, self.popup.place_forget) #The amount of time the error thing stays up for
#it would change the colour of the letter of the words the user enter to indicate whether if the letter position is correct/if the letter is in the word but not in correct location or it doest appear at all
    def scoring_the_guess(self):
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
            self.going_to_the_result_page(won)
#the hint button that gives hint by telling the user what letter appears in what location in the Single_line_of_boxes function
    def give_hint(self, event=None):
        for i in range(self.Word_length):
            current = self.Single_line_of_boxes.itemcget(f"give_hint_letter{i}", "text")
            if current == "":
                self.Single_line_of_boxes.itemconfigure(f"give_hint_letter{i}", text=self.word[i])
                self.Single_line_of_boxes.itemconfigure(f"hint{i}", fill=self.Green, outline=self.Green)
                self.Single_line_of_boxes.itemconfigure(f"hint{i}", tags=("temporary_hint", f"hint{i}"))
                self.after(2000, lambda i=i: self.clear_hint(i))
                return
#this is more of a personal choice where the hint goes away after a bit, so that the hint is like a mini clue they can get, but then it fades so they still "get" feeling of doing it
    def clear_hint(self, i):
        current = self.Single_line_of_boxes.itemcget(f"give_hint_letter{i}", "text")
        if current == self.word[i]:
            self.Single_line_of_boxes.itemconfigure(f"give_hint_letter{i}", text="")
            self.Single_line_of_boxes.itemconfigure(f"hint{i}", fill="#3D3D3D", outline="#6E6E6E")
            #function that allows the help page to open and be shown
    def show_help_page(self):
            self.Help_image_box.place(relx=0.5, rely=0.5, anchor="center")
            self.Help_image_box.lift() #brings the help page to appear in front
            self.Help_image_close.place(relx=0.715, rely=0.12, anchor="center")
            self.Help_image_close.lift()#allows the help page close button to appear in front of the help page
#closes the help image page
    def close_help_page(self, event=None): #the function that closes both the belp page and the help page button
        self.Help_image_box.place_forget()
        self.Help_image_close.place_forget()

    def going_to_the_result_page(self, won):
        self.unbind_all("<Key-BackSpace>")
        self.unbind_all("<Key-Return>")
        self.unbind_all("<Key>")
        self.after(1000, lambda:self.app.show_result_page(won=won,word=self.word,guesses=self.entered))



class StellaVerbaResultPage(Frame):
    def __init__(self, master,won,word,guesses,app):
        Frame.__init__(self, master, bg="white")
        self.master = master
        self.app = app
        self.pack(fill="both", expand=True)
        self.shortcut = Path(__file__).parent
        self.img = self.shortcut / "images"
        #the background image of the result page and the labels of the page as well as the big box that is placed in the middle of the page
        self.background_images = PhotoImage(file=str(self.img / ("dbg2.png" if app.mode == "dark_mode" else "lbg2.png")))
        self.Background_Label = Label(self, image=self.background_images, bd=0)
        self.Background_Label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Result_page_box = tk.Frame(self, bg="#2E2E2E", bd=0)
        self.Result_page_box.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.78)
        #depending on whether the user had won one of these two texts appears
        if won:
            message = "Congratulations"
            colour_of_the_final_text = "#6AAA64"
        else:
            message = "Better Luck Next Time"
            colour_of_the_final_text = "#C7141F"

        self.Result_page_text = tk.Label(self.Result_page_box, text=message, font=("Rubik Bubbles", 30),bg="#2E2E2E", fg=colour_of_the_final_text)
        self.Result_page_text.pack(pady=(40, 10))
        #the line that separates the congratulatory line with the definition and the word reveal text
        self.divider = tk.Frame(self.Result_page_box, bg="#555555", height=2)
        self.divider.pack(fill="x", padx=30, pady=(0, 15))
        #the code for the "the word is:_____" text that appears in the result page
        self.The_word_is_text = tk.Label(self.Result_page_box, text="The word is:", font=("Inter", 16),bg="#2E2E2E", fg="#AAAAAA")
        self.The_word_is_text.pack(pady=(0, 5))
        #the code for the word reveal function for example "The word is: VALID"
        self.Word_Revealed = tk.Label(self.Result_page_box, text=word.upper(), font=("Inter", 40, "bold"), bg="#2E2E2E", fg="white")
        self.Word_Revealed.pack(pady=(0, 5))
        #shows the user the amount of trials they did and if they won
        if won:
            self.Amount_of_guesses_showed = tk.Label(self.Result_page_box, text=f"You got it in {guesses} guess{'es' if guesses != 1 else ''}!", font=("Inter", 14), bg="#2E2E2E", fg="#AAAAAA")
            self.Amount_of_guesses_showed.pack(pady=(0, 20))
        #this is more of a testing type of code to make sure that each of the word has definition
        definition = Definitions.get(word.lower(), "No definition available.") #just to test if there is no definitons for the word
        self.Definition_of_the_word = tk.Frame(self.Result_page_box, bg="#545454", bd=0)
        self.Definition_of_the_word.pack(padx=30, pady=(0, 30), fill="x")
        #the font of the definition inside the box
        self.Font_of_the_definition = tk.Label(self.Definition_of_the_word, text=definition, font=("Inter", 9),bg="#545454", fg="white", wraplength=480, justify="center")
        self.Font_of_the_definition.pack(padx=20, pady=20)
        #the frame of the play again and the exit button
        self.play_again_And_Exit_Button = tk.Frame(self.Result_page_box, bg="#2E2E2E")
        self.play_again_And_Exit_Button.pack(pady=(0, 40))
        #The play again button for the result page
        self.play_again_Button = tk.Button(self.play_again_And_Exit_Button, text="Play Again", font=("Inter", 16, "bold"), bg="#548a38", fg="white", bd=0, relief="flat", cursor="hand2", activebackground="#5d993d", activeforeground="white", command=self.play_again)
        self.play_again_Button.pack(side="left", padx=20, ipadx=20, ipady=10)
        #the exit button for the result page
        self.Exit_button = tk.Button(self.play_again_And_Exit_Button, text="Exit", font=("Inter", 16, "bold"),bg="#ab1b27", fg="white", bd=0, relief="flat", cursor="hand2",activebackground="#bf1d2a", activeforeground="white",command=self.master.winfo_toplevel().destroy)
        self.Exit_button.pack(side="left", padx=20, ipadx=20, ipady=10)
    #the play again function where it would destroy the page and would lead back to the game page
    def play_again(self):
        self.destroy()
        self.app.displaying_the_results_page(won=None, word=None, guesses=None)