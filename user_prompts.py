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
        print(f'\n{person.name}: {person.speech}')
        if "*" in person.speech:
            char.clues.append(person.speech)
    

def search_prompt(char):
    print(f'\n{char.curr.thing}')
    if "cloth" in char.curr.thing:
        char.clues.append("Bloody Cloth")
    elif "knife" in char.curr.thing:
        char.clues.append("Knife")
    elif "Stairwell" in char.curr.thing:
        char.clues.append("Stairwell Key")
    elif "Edith" in char.curr.thing:
        char.clues.append("Edith Key")
    elif "sink" in char.curr.thing:
        char.clues.append("Hair")

def accuse_prompt(char):
    person = session.query(Person).filter(Person.id == char.curr.person).first()
    if "Edith Key" not in char.clues:
        print(f"\nWe have no way of trapping {person.name} yet!")
    else:
        edith = session.query(Path).filter(Path.id == 7).first()

        if edith.person:
            print("\nYou already have someone locked away in Edith. You should try and escape first!")
        else:
            print(f"\nYou accuse {person.name} of being the killer. You bring them to Edith and lock them up.")
            char.curr.person = None
            char.curr = edith
            session.commit()

def escape_promt(char):
    if char.curr.id != 2:
        print("\nYou need to go to the stairs to escape")
    else:
        edith = session.query(Path).filter(Path.id == 7).first()
        person = session.query(Person).filter(Person.id == edith.person).first()
        # print(person, char.clues, len(char.clues), edith.person)
        if "Stairwell Key" not in char.clues:
            return print("\nYou need to find the stairwell key")
        elif "Stairwell Key" in char.clues and edith.person == 0:
            return print("\nYou need to trap the killer in Edith")
        elif "Stairwell Key" in char.clues and len(char.clues) < 8:
            return print("\nYou havent found all the clues")
        elif person:
            if "Stairwell Key" in char.clues and not test:
                # return print("\nYou trapped the wrong person. You find their body")
                return print("\nYou trapped the wrong person and unknowingly doomed them to a life of imprisonment while the actual killer gets away. Game over!")
            elif person.murderer == 1 and len(char.clues) == 8:
                return print("\nYou manage to escape through the locked doors and step out onto the stairwell landing. As you descend the stairs, you begin to piece together the events of that night, following the trail of evidence. Eventually, you figure out what happened and who the killer is. After a few moments of hesitation, you approach the police and present your evidence. The murderer is arrested, and justice is served. You take a deep breath, relieved that the mystery has been solved. As you walk away from the scene, you know that youll never forget the lessons you learned during this experience.")
    



# ipdb.set_trace()