from path_instances import thing_location_list, paths
from person_instances import people
from character import Character
import ipdb

chris = Character("chris", 5)

people[0].murderer = True

hair_color = [person.hair_color for person in people if person.murderer == True][0]
shirt_color = [person.shirt_color for person in people if person.murderer == True][0]

se0 = "You've already searched this area!"

se1 = "You search the area and find nothing"
se2 = "You search the area and find bolts for chair arm rests. Is this where they've all been?"
se3 = "You search the area and find $20. Sickkkkkkkk."
se4 = "You search the area and find an empty Pret a Manger bag. Sally was definitely here before."
se5 = "You search the area and find Michelle's bright ass green bottle. Why does she leave this everywhere?"
se6 = "You search the area and find some flass on the floor. Did this fall out of Jack's finger?"
se7 = "You search the area and find a laptop heavily smeared with fingerprints."
se8 = "You search the area and find an open laptop with only manga open and not a single line of code to be seen at all."
se9 = "You search the area and find an LIRR ticket. Guess Min isn't going home."
se10 = "You search the area and find a bag of rolling tobacco. Classic Ian."
se11 = f"You search the area and find and find a {shirt_color} colored cloth stained with blood. The killer must have used this to clean the murder weapon."
se12 = "You search the area and find the area and find a bloodied knife!"
se13 = "You search the area and find a key labeled with 'Stairwell'. Do we finally have a way out?!"
se14 = "You search the area and find a key labeled with 'Edith'. This could come in handy later!" 

se15 = f"You see the sink stained with blood with some {hair_color} colored hair. Does this hair belong to the killer?"
se16 = "You look around and see nobody here at all. This might be the perfect place to trap the killer!"

search_list = [se1, se2, se3, se4, se5, se6, se7, se8, se9, se10, se11, se12, se13, se14]

def set_items():
    paths[6].thing = se16
    paths[7].thing = se15

    for i in thing_location_list:
        paths[i].thing = search_list[0]
        del search_list[0]

def search(char):
    print(f'{paths[char.curr].thing}')

ipdb.set_trace()