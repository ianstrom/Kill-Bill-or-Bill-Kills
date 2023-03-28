from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

from path_instances import paths
from destination_instances import destinations
from location_instances import locations
from person_instances import people

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///billkills.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for path in paths:
        session.add(path)

    for destination in destinations:
        session.add(destination)
        
    for person in people:
        session.add(person)

    for location in locations:
        session.add(location)
    
    session.commit()