#!/usr/bin/python3
"""Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Database connection information
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connection to MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for State objects containing the letter 'a'
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(
        State.id).all()

    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
