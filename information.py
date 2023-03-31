from os import name
from subprocess import call
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Person

def get_info(character, murderer):
    # Clear Terminal
    _ = call('clear'if name == 'posix' else 'cls')

    # Example variables for testing (Comment out or delete before use)

    shirt_color = murderer.shirt_color
    hair_length = murderer.hair_length
    hair_color = murderer.hair_color

    # Example Completed Array for Testing (Comment out or delete before use)

    clue_array = character.clues

    # clue_array = [
    #     'Edith Key', 
    #     'Stairs Key', 
    #     'Stained Cloth', 
    #     'Blood/Hair',
    #     f"* I think I saw someone wearing a {shirt_color} colored shirt walking away from the body before. Could it be them? *",
    #     f"* I'm pretty sure I saw someone with {hair_length} length hair hanging out around the body before. Maybe it's them? *",
    #     f"* I couldn't see too well, but I think I saw someone suspicious around the body with {hair_color} colored hair. Was that actually the killer? *"
    #     ]

    # Physical Clue Logic

    thing_dict = {}

    for thing in clue_array:
        if thing == 'Knife':
            thing_dict['Knife'] = 'A bloody knife'
        if thing == 'Edith Key':
            thing_dict['Edith Key'] = 'A good way to lock someone up'
        if thing == 'Stairwell Key':
            thing_dict['Stairwell Key'] = 'a key to the stairwell when you want to make your escape'
        if thing == 'Bloody Cloth':
            thing_dict['Bloody Cloth'] = f'A cloth covered in blood. Its color is {shirt_color}'
        if thing == 'Hair':
            thing_dict['Hair'] = f'A bit of {hair_length} hair covered in blood'

    if thing_dict:
        print()
        print("Here's a things I've picked up along the way:")

    print()
    for thing, description in thing_dict.items():
        print(f'{thing:20} -        {description:20}')
    print()

    # Verbal Clue Logic

    verbal_dict = {}

    for phrase in clue_array:
        if "shirt" in phrase:
            verbal_dict['Shirt Clue'] = f"Someone saw the a flash of a {shirt_color}-colored shirt. Could it be the killer?"
        if "length" in phrase:
            verbal_dict['Hair-length Clue'] = f"There was a suspicious person with {hair_length}-length hair hanging around the body..."
        if "sus" in phrase:
            verbal_dict['Hair-color Clue'] = f"An eyewitness said the killer's hair might be {hair_color}."


    if verbal_dict:
        print()
        print("I've learned a few facts that could be helpful...")

    print()
    for clue, phrase in verbal_dict.items():
        print(f'{clue:20} -        {phrase:20}')
    print()

    # In case nothing has been learned or picked up yet:
    if not clue_array:
        print()
        print("You haven't discovered anything yet. Best get to investigating!")

def get_suspect_info():
    engine = create_engine('sqlite:///billkills.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all remaining suspects
    suspects = session.query(Person)
    print()
    for suspect in suspects:
        print('------------------------------------------------------------------------------------------------------')
        print(suspect.details)

get_suspect_info()