#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extracting arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)
    cursor = db.cursor()

    # Execute SQL query to select cities of the given state
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))

    # Fetch all rows and display results
    rows = cursor.fetchall()
    cities = ", ".join([row[0] for row in rows])
    print(cities)

    # Close cursor and database connection
    cursor.close()
    db.close()
