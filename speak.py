from person_instances import people
import random

# people[0].murderer = True
# del people[-2:]

hair_length = [person.hair_length for person in people if person.murderer == True][0]
hair_color = [person.hair_color for person in people if person.murderer == True][0]
shirt_color = [person.shirt_color for person in people if person.murderer == True][0]

s1 = f"* I think I saw someone wearing a {shirt_color} colored shirt walking away from the body before. Could it be them? *"
s2 = f"* I'm pretty sure I saw someone with {hair_length} length hair hanging out around the body before. Maybe it's them? *"
s3 = f"* I couldn't see too well, but I think I saw someone suspicious around the body with {hair_color} colored hair. Was that actually the killer? *"
s4 = "I haven't seen much, I just want to get out of here."
s5 = "Is your phone working? I can't seem to get a signal anywhere."
s6 = "I'm scared, what are we going to do?"
s7 = "Did you see that the stairs were locked?"
s8 = "Aww man, I just really wanted to code today. How am I going to be a full stack developer at this rate."
s9 = "So does that mean no pong on Friday?"
s10 = "Is it too late to transfer to remote studies?"
s11 = "It couldn't have been one of us right?"
s12 = "I didn't see much, but there definitely has to be clues around since we're all trapped in here together."
s13 = "Kind of weird that it's only our cohort here today, right?"
s14 = "Well at least we won't have to present our projects today."

speech_array = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]

for person in people:
    if person.murderer == True:
        i = random.randint(3, 13)
        person.speech = speech_array[i]
        del speech_array[i]

random.shuffle(speech_array)

for person in people:
    if person.murderer == False:
        person.speech = speech_array[0]
        del speech_array[0]