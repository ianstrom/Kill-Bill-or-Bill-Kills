from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Path(Base):
    __tablename__ = 'paths'

    all = []

    id = Column(Integer(), primary_key=True)
    name = Column("name", String())
    up = Column("up", Integer())
    down = Column("down", Integer())
    left = Column("left", Integer())
    right = Column("right", Integer())
    person = Column("person", Integer())
    thing = Column("thing", String())

    def __init__(self, name, up, down, left, right, person, thing):
        self.name = name
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.person = person
        self.thing = thing
        Path.all.append(self)
    
    def __repr__(self):
        return (f"{self.name}-  Up: {self.up}, Down: {self.down}, Left: {self.left}, Right: {self.right}")


class Destination(Base):
    __tablename__ = 'destinations'

    all = []

    id = Column(Integer(), primary_key=True)
    destination_id = Column(Integer())
    bash_path = Column(String())

    def __init__(self, destination_id, bash_path):
        self.destination_id = destination_id
        self.bash_path = bash_path
        Destination.all.append(self)

    def __repr__(self):
        return f"Unique Pathway {self.id}:  Goes to: {self.destination_id}, Bash File: {self.bash_path}"


class Person(Base):
    __tablename__ = 'people'

    all = []

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    hair_length = Column(String())
    hair_color = Column(String())
    shirt_color = Column(String())
    murderer = Column(Boolean())
    speech = Column(String())

    def __init__(self, name, hair_length, hair_color, shirt_color, murderer, speech):
        self.name = name
        self.hair_length = hair_length
        self.hair_color = hair_color
        self.shirt_color = shirt_color
        self.murderer = murderer
        # self.location = None
        self.speech = speech
        Person.all.append(self)

    @property
    def details(self):
        return f'Name: {self.name:15}  Hair Length: {self.hair_length:15} Hair Color: {self.hair_color:15} Shirt Color: {self.shirt_color}'

    
    def __repr__(self):
        return f'Name: {self.name}, Murderer: {self.murderer}'

    
class Location(Base):
    __tablename__ = 'locations'

    all = []

    id = Column(Integer(), primary_key=True)
    up = Column(String())
    down = Column(String())
    left = Column(String())
    right = Column(String())

    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        Location.all.append(self)
    
    def __repr__(self):
        return f"Room: {self.id}{chr(10)}Up: {self.up}, Down: {self.down}, Left: {self.left}, Right: {self.right}"


# Persisting the Data
if __name__ == '__main__':
    engine = create_engine('sqlite:///billkills.db')
    Base.metadata.create_all(engine)
