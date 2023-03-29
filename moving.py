import subprocess
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Person, Path, Destination, Location

engine = create_engine('sqlite:///billkills.db')

Session = sessionmaker(bind=engine)

session = Session()


def query_direction(char, direction):
    destination_id = getattr(char.curr, direction)
    return session.query(Destination).filter(Destination.id == destination_id).all()[0]

def query_new_path(new_path):
    return session.query(Path).filter(Path.id == new_path.destination_id).all()[0]

def print_directions(destination):
    location = session.query(Location).filter(Location.id == destination.id).all()[0]
    message = ""
    paths = [str(value) for key, value in location.__dict__.items() if key in ["up", "down", "left", "right"] and value is not None] + ["Search: (f) Speak: (t) Escape: (e) Accuse: (q)"]
    message += " ".join(paths)
    print(message)

def move_left(char):
    if char.curr.left > 0:
        new_path = query_direction(char, 'left')
        destination = query_new_path(new_path)
        if not new_path.bash_path == "": 
            subprocess.run(new_path.bash_path)
        print_directions(destination)
        char.move(destination)
    else:
        print("You cannot go to the left")

def move_right(char):
    if char.curr.right > 0:
        new_path = query_direction(char, 'right')
        destination = query_new_path(new_path)
        if not new_path.bash_path == "": 
            subprocess.run(new_path.bash_path)
        print_directions(destination)
        char.move(destination)
    else:
        print("You cannot go to the right")

def move_up(char):
    if char.curr.up > 0:
        new_path = query_direction(char, 'up')
        destination = query_new_path(new_path)
        if not new_path.bash_path == "": 
            subprocess.run(new_path.bash_path)
        print_directions(destination)
        char.move(destination)
    else:
        print("You cannot go forward")

def move_down(char):
    if char.curr.down > 0:
        new_path = query_direction(char, 'down')
        destination = query_new_path(new_path)
        if not new_path.bash_path == "": 
            subprocess.run(new_path.bash_path)
        print_directions(destination)
        char.move(destination)
    else:
        print("You cannot go backwards")

        