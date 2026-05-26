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

guessedletter=pygame.font.Font("Fonts/")


