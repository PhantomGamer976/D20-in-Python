import random
import pyttsx3
import keyboard 
import pygame




random.seed()

D20 = None



def roll_d20():
    global D20 
    D20 = random.randint(1,20)
    pyttsx3.speak(f"You rolled a {D20}")
    return

def nat_20():
    pygame.init()
    pygame.mixer.music.load("Nat_20.mp3")
    pygame.mixer.music.play()

def nat_1():
    pygame.init()
    pygame.mixer.music.load("SadDice.mp3")
    pygame.mixer.music.play()


while True:
    if keyboard.is_pressed("r"):
        roll_d20()
        if D20 == 20:
            nat_20()
        if D20 == 1:
            nat_1()