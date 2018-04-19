import sqlite3 

con = sqlite3.connect("chinook.db")
c = con.cursor()

c.execute("""
    SELECT Name, Milliseconds
    FROM tracks 
    ORDER BY Milliseconds DESC
    LIMIT 10;""")

# note the extra comma - c.fetchall() returns
# a list of tuples "[(name, ), (name, ), ...]"

print("The 10 longest songs in the database are:")
for name, ms in c.fetchall():
    print('"%s" at %d minutes' % (name, ms//60000))

