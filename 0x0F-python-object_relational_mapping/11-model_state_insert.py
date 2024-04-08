#!/usr/bin/python3
"""Add the State object "Louisiana" to the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and bind to MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Create new State object
    new_state = State(name='Louisiana')

    # Add new_state to the session
    session.add(new_state)

    # Commit the session to save changes to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)
