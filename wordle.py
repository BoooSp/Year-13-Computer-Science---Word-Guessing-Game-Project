import sys
import pygame
import random
from words import *
from pathlib import Path

pygame.innit()
width,height=633,900


shortcut = Path(__file__).parent
word = shortcut / "images"
font = shortcut / "Fonts"

page=pygame.display.set_code((width,height))
bg=pygame.image.load("images/dbg.png")
bgg=bg.get_react(center=(317,300))
icon=pygame.image.load("images/dbg.png")

pygame.display.set_caption("Wordle")
pygame.display.set_icon(icon)

Green = "#264226"
Yellow = "#AAA228"
Grey = "#545454"
DarkGrey="#2B2B2B"

Alphabet=["ABCDEF","GHIJKL","MNOPQR","STUVWX","YZ"]

guessedletter=pygame.font.Font("Fonts/Italianno-Regular.ttf",25)
notguessedletter=pygame.font.Font("Fonts/Italianno-Regular.ttf",40)

page.fill("white")
page.blit(bg,bgg)
pygame.display.update()

letter_x_spacing=85
letter_y_spacing=12
lettersize=75

guesses_count=0

guesses=[[]]*6
correctguess=[]
correctguesstring=""
correctletterbgx=110

indicators=[]
game_result=""

class letter:
    def __init__(self,text,bg_position):
        pass
    def draw(self):
        pass
    def delete(self):
        pass



