from attribute_setters import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#Debugging tools
import ipdb

engine = create_engine('sqlite:///billkills.db')
Session = sessionmaker(bind=engine)
session = Session()

def speak_prompt(char):
    if char.curr.person:
        person = session.query(Person).filter(Person.id == char.curr.person).first()
        print(f'{person.name}: {person.speech}')
        if "*" == person.speech[0]:
            char.clues.append(person.speech)
    

def search_prompt(char):
    print(f'{char.curr.thing}')
    if "cloth" in char.curr.thing:
        char.clues.append("Bloody cloth")
    elif "knife" in char.curr.thing:
        char.clues.append("Knife")
    elif "Stairwell" in char.curr.thing:
        char.clues.append("Stairwell key")
    elif "Edith" in char.curr.thing:
        char.clues.append("Edith key")
    elif "sink" in char.curr.thing:
        char.clues.append("Hair")

def accuse_prompt(char):
    person = session.query(Person).filter(Person.id == char.curr.person).first()
    if "Edith key" not in char.clues:
        print(f"We have no way of trapping {person.name} yet!")
    else:
        edith = session.query(Path).filter(Path.id == 7).first()
        edith.person = char.curr.person
        char.curr.person = None
        char.curr = 7
        session.commit()

def escape_promt(char):
    if char.curr != 2:
        print("You need to go to the stairs to escape")
    else:
        edith = session.query(Path).filter(Path.id == 7).first()
        person = session.query(Person).filter(Person.id == edith.person).first()
        if "Stairwell key" not in char.clues:
            print("You need to find the stairwell key")
        elif "Stairwell key" in char.clues and edith.person == 0:
            print("You need to trap the killer in Edith")
        elif "Stairwell key" in char.clues and len(char.clues) < 8:
            print("You havent found all the clues")
        elif "Stairwell key" in char.clues and person.murderer != True:
            print("You trapped the wrong person")
        elif person.murderer == True and len(char.clues) == 8:
            print("You have escaped")
    



# ipdb.set_trace()