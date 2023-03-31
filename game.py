from pynput import keyboard
import subprocess
from character import Character
import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Path, Person
from moving import move_left, move_right, move_down, move_up
from information import get_info, get_suspect_info
import os

engine = create_engine('sqlite:///billkills.db')
Session = sessionmaker(bind=engine)
session = Session()

ids_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
banned_locations = [1,7,8]
# char = Character('fucked')

print("Choose a character: \n(1): Anson\n(2): Bill\n(3): Finn\n(4): Jack\n(5): Bobby\n(6): Brett\n(7): Chris C.\n(8): Chris W.\n(9): Eshwar\n(10): Jacob\n(11): Ian\n(12): Kyushik\n(13): Min\n(14): Michelle\n(15): Sally\n(16): Nick")
x = int(input())
del ids_array[x - 1]
print(x)
character = session.query(Person).filter(Person.id == x).first()
randombitch = random.randint(0,14)
murderer_id = ids_array[randombitch]
murderer = session.query(Person).filter(Person.id == murderer_id).first()
murderer.murderer = True
del ids_array[randombitch]

random2 = random.randint(0,13)
dead_person_id = ids_array[random2]
dead_person = session.query(Person).filter(Person.id == dead_person_id).first()
del ids_array[random2]

char = Character(character.name)
session.delete(character)
session.delete(dead_person)
session.commit()
char.curr = session.query(Path).filter(Path.id == 1).first()

from attribute_setters import *
from user_prompts import *
set_attr()

subprocess.run("./videos/loading-vid.sh")
print(f'Reception: (a), Stairs: (d)')
print(f" You walk out of the Elevator and find {dead_person.name}'s body.")

def on_press(key):
    if key.char == 'a':
        move_left(char)

    if key.char == 'd':
        move_right(char)

    if key.char == 'w':
        move_up(char)

    if key.char == 's':
        move_down(char)

    if key.char == 'f':
        if char.curr.id != 1:
            search_prompt(char)
        else:
            print("\nNothing to search")
    
    if key.char == 't':
        if char.curr.person != 0 and char.curr.id != 7:
            speak_prompt(char)
        else:
            print("\nThere is no one here... Eerie")
    
    if key.char == 'e':
        escape_promt(char)
        pass

    if key.char == 'q':
        if char.curr.person != 0 and char.curr.id != 7:
            accuse_prompt(char)
        else:
            print("\nThere is no one to accuse!")
        pass

    if key.char == 'z':
        get_info(char, murderer)
        pass
    
    if key.char == 'x':
        get_suspect_info()
        pass
    

def on_release(key):
    if key == keyboard.Key.esc:
        subprocess.run('rm billkills.db')
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


