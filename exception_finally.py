import sqlite3

conn = None

try:
    conn = sqlite3.connect('animals/wombat.db')
except sqlite3.DatabaseError as err:
    print(err)
    exit()
else:
    cursor = conn.cursor()
    # make queries ....
finally:  # clean up and disconnect as needed
    if conn is not None:
        conn.close()
