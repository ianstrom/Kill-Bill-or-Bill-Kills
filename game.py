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

subprocess.run("./videos/loading-vid.sh")

print(f'Reception: (a), Stairs: (d)')





def on_press(key):
    if key.char == 'a':
        if char.curr.left > 0:
            new_path = session.query(Destination).filter(Destination.id == char.curr.left).all()[0]
            if not new_path.bash_path == "": 
                subprocess.run(new_path.bash_path)
            destination = session.query(Path).filter(Path.id == new_path.destination_id).all()[0]
            char.move(destination)
        else:
            print("You cannot go to the left")

    if key.char == 'd':
        if char.curr.right > 0:
            new_path = session.query(Destination).filter(Destination.id == char.curr.right).all()[0]
            if not new_path.bash_path == "": 
                subprocess.run(new_path.bash_path)
            destination = session.query(Path).filter(Path.id == new_path.destination_id).all()[0]
            char.move(destination)
        else:
            print("You cannot go to the right")

    if key.char == 'w':
        if char.curr.up > 0:
            new_path = session.query(Destination).filter(Destination.id == char.curr.up).all()[0]
            if not new_path.bash_path == "": 
                subprocess.run(new_path.bash_path)
            destination = session.query(Path).filter(Path.id == new_path.destination_id).all()[0]
            char.move(destination)
        else:
            print("You cannot go forward")

    if key.char == 's':
        if char.curr.down > 0:
            new_path = session.query(Destination).filter(Destination.id == char.curr.down).all()[0]
            if not new_path.bash_path == "": 
                subprocess.run(new_path.bash_path)
            destination = session.query(Path).filter(Path.id == new_path.destination_id).all()[0]
            char.move(destination)
        else:
            print("You cannot go backwards")

    print(char.curr.name)
    

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

