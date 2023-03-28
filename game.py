from pynput import keyboard
import subprocess
from character import Character
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Path
import random
from moving import move_left, move_right, move_down, move_up

engine = create_engine('sqlite:///billkills.db')

Session = sessionmaker(bind=engine)

session = Session()

char = Character('fucked')
muderer = random.randint(0,14)

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

