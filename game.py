from pynput import keyboard
import subprocess
from character import Character
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Person, Path, Destination
import random

engine = create_engine('sqlite:///billkills.db')

Session = sessionmaker(bind=engine)

session = Session()

char = Character('fucked')
muderer = random.randint(0,15)

char.curr = session.query(Path).filter(Path.id == 1).all()[0]
subprocess.run("./videos/black+white.sh")
print(char.curr.left)

# print(f'{char.left}: (a), {char.right}: (d), {char.down}: (s), {char.up}: (w)')


def on_press(key):
    if key.char == 'a':
        subprocess.run("./videos/black+white.sh")
    

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

