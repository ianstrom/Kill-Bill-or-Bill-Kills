from models import Path
import random

#Both of these lists will be put onto attributes respectively

#Random List of indexes for where PEOPLE go
person_location_list = list(range(1, 18))
person_location_list = [id for id in person_location_list if id != 7 and id != 8]
random.shuffle(person_location_list)

#Random List of indexes for where THINGS go
thing_location_list = range(1, 18)
thing_location_list = [id for id in thing_location_list if id!= 7 and id != 8 and id != 1]
random.sample(thing_location_list, 4)
random.shuffle(thing_location_list)




p1 = Path("Elevator", 0, 0, 1, 2)
p3 = Path("Stairs", 0, 0, 3, 4)
p4 = Path("Data Hall Corner", 5, 0, 6, 7)
p5 = Path("Johnson- Lower", 8, 9, 10, 0)
p6 = Path("Johnson- Couches", 11, 0, 0, 0)
p8 = Path("Johnson- Kitchen", 12, 13, 0, 0)
p9 = Path("Edith", 0, 14, 0, 0)
p10 = Path("Men's Bathroom", 0, 15, 0, 0)
p14 = Path("Reception", 0, 0, 16, 17)
p15 = Path("Large Room Viewpoint", 18, 19, 20, 21)
p16 = Path("Turing", 22, 0, 0, 0)
p17 = Path("Large Room- Couches", 23, 24, 0, 25)
p19 = Path("Collins", 0, 26, 0, 0)
p20 = Path("Large Room- Kitchen", 27, 28, 29, 0)
p22 = Path("Small Lecture Hall", 30, 31, 0, 0)
p23 = Path("Phone Booths", 32, 33, 0, 0)
p25 = Path("Phase 5- Room", 0, 0, 0, 34)

# Composing Array

paths = [
p1,
p3,
p4,
p5,
p6,
p8,
p9,
p10,
p14,
p15,
p16,
p17,
p19,
p20,
p22,
p23,
p25
]

# Code to double-check paths

# for path in Path.all:
#     print (path.__repr__())
#     print()