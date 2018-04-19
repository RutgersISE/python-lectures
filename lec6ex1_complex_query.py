import sqlite3 

con = sqlite3.connect("chinook.db")
c = con.cursor()

c.execute("""
    SELECT FirstName, Lastname, sum(Total)
    FROM invoices i
    INNER JOIN customers c on i.CustomerID = c.CustomerID
    GROUP BY c.CustomerID
    ORDER BY sum(Total) DESC
    LIMIT 5;""")

print("Our best customers are: ")
for i, (fname, lname, tot) in enumerate(c.fetchall()):
    print("%d. %s %s who spent %d dollars." % (i + 1, fname, lname, tot))
