from pynput import keyboard
import subprocess
from character import Character
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Path, Person
from moving import move_left, move_right, move_down, move_up

engine = create_engine('sqlite:///billkills.db')
Session = sessionmaker(bind=engine)
session = Session()

# char = Character('fucked')

print("Choose a character: \n(1): Anson\n(2): Bill\n(3): Finn\n(4): Jack\n(5): Bobby\n(6): Brett\n(7): Chris C.\n(8): Chris W.\n(9): Eshwar\n(10): Jacob\n(11): Ian\n(12): Kyushik\n(13): Min\n(14): Michelle\n(15): Sally\n(16): Nick")
x = input()
character = session.query(Person).filter(Person.id == x).all()[0]
char = Character(character.name)
char.curr = session.query(Path).filter(Path.id == 1).all()[0]

subprocess.run("./videos/loading-vid.sh")
print(f'Reception: (a), Stairs: (d)')

def on_press(key):
    if key.char == 'a':
        move_left(char)

    if key.char == 'd':
        move_right(char)

    if key.char == 'w':
        move_up(char)

    if key.char == 's':
        move_down(char)

    print(char.curr.name)
    

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

