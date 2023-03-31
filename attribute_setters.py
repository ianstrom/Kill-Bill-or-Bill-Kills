# from path_instances import thing_location_list, person_location_list, paths
# from person_instances import people
from models import Path, Person
import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///billkills.db')
Session = sessionmaker(bind=engine)
session = Session()

#Debugging tools
# import ipdb
# people[0].murderer = True
# del people[-2:]

people_list = session.query(Person).all()
random.shuffle(people_list)
#SEARCH ITEMS
murderer = [person for person in people_list if person.murderer == True][0]

hair_length, hair_color, shirt_color = murderer.hair_length, murderer.hair_color, murderer.shirt_color

path_ids = [2,3,4,5,6,9,10,11,12,13,14,15,16,17]
# path_ids2 = [2,3,4,5,6,9,10,11,12,13,14,15,16,17]

se0 = " You've already searched this area!"

se1 = "\nYou search the area and find nothing"
se2 = "\nYou search the area and find bolts for chair arm rests. Is this where they've all been?"
se3 = "\nYou search the area and find $20. Sickkkkkkkk."
se4 = "\nYou search the area and find an empty Pret a Manger bag. Sally was definitely here before."
se5 = "\nYou search the area and find Michelle's bright ass green bottle. Why does she leave this everywhere?"
se6 = "\nYou search the area and find some glass on the floor. Did this fall out of Jack's finger?"
se7 = "\nYou search the area and find a laptop heavily smeared with fingerprints."
se8 = "\nYou search the area and find an open laptop with only manga open and not a single line of code to be seen at all."
se9 = "\nYou search the area and find an LIRR ticket. Guess Min isn't going home."
se10 = "\nYou search the area and find a bag of rolling tobacco. Classic Ian."
se11 = f"\n* You search the area and find a {shirt_color} colored cloth stained with blood. The killer must have used this to clean the murder weapon.*"
se12 = "\nYou search the area and find the area and find a bloodied knife!"
se13 = "\nYou search the area and find a key labeled with 'Stairwell'. Do we finally have a way out?!"
se14 = "\nYou search the area and find a key labeled with 'Edith'. This could come in handy later!"

se15 = f"\nYou see the sink stained with blood with some {hair_color} colored hair. Does this hair belong to the killer?"
se16 = "\nYou look around and see nobody here at all. This might be the perfect place to trap the killer!"

search_list = [se1, se2, se3, se4, se5, se6, se7, se8, se9, se10, se11, se12, se13, se14]

#DIALOGUE PROMPTS

s1 = f"\n* I think I saw someone wearing a {shirt_color} colored shirt walking away from the body before. Could it be them? *"
s2 = f"\n* I'm pretty sure I saw someone with {hair_length} length hair hanging out around the body before. Maybe it's them? *"
s3 = f"\n* I couldn't see too well, but I think I saw someone suspicious around the body with {hair_color} colored hair. Was that actually the killer? *"
s4 = "\nI haven't seen much, I just want to get out of here."
s5 = "\nIs your phone working? I can't seem to get a signal anywhere."
s6 = "\nI'm scared, what are we going to do?"
s7 = "\nDid you see that the stairs were locked?"
s8 = "\nAww man, I just really wanted to code today. How am I going to be a full stack developer at this rate."
s9 = "\nSo does that mean no pong on Friday?"
s10 = "\nIs it too late to transfer to remote studies?"
s11 = "\nIt couldn't have been one of us right?"
s12 = "\nI didn't see much, but there definitely has to be clues around since we're all trapped in here together."
s13 = "\nKind of weird that it's only our cohort here today, right?"
s14 = "\nWell at least we won't have to present our projects today."

speech_array = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]

def set_attr():
    #Setting items
    edith = session.query(Path).filter(Path.id == 7).first()
    mens = session.query(Path).filter(Path.id == 8).first()
    edith.thing = se16
    mens.thing = se15
    
    random.shuffle(search_list)


    # for i in range(1,18):
    #   session.query(Paths).filter(Path.id == i).update('thing' search_list[0])

    for i in path_ids:
        random.shuffle(search_list)
        path = session.query(Path).filter(Path.id == i).first()
        path.thing = search_list[0]
        del search_list[0]

    #Setting dialogue prompts
    for person in people_list:
        if person.murderer == True:
            i = random.randint(3, 13)
            person.speech = speech_array[i]
            del speech_array[i]

    random.shuffle(speech_array)

    for person in people_list:
        if person.murderer == False:
            person.speech = speech_array[0]
            del speech_array[0]
    
    #Setting person location
    for i in path_ids:
        path = session.query(Path).filter(Path.id == i).first()
        path.person = people_list[0].id
        del people_list[0]
        # paths[person_location_list[0]].person = person
        # person.location = person_location_list[0]

    session.commit()
# ipdb.set_trace()