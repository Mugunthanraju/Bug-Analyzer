import sqlite3 as sql

#! Connect to database
con = sql.connect('sample.db')

#! Create a cursor
c = con.cursor()

#! Create a Table
# c.execute("""CREATE TABLE categories (
# 		category text,
# 		count integer
# 		)""")

#! list of data
# list_data = [
#     ("Student", 500),
#     ("Professor", 100),
#     ("HOD", 50),
#     ("Dean", 10)
# ]
#! Inserting the multiple row values into table
# c.executemany("INSERT INTO categories VALUES (?, ?)", list_data)
#! Inserting the single row values into table
# c.execute("INSERT INTO categories VALUES ('Management', 5)")

#! Selecting from the TABLE.
# c.execute("SELECT rowid, * FROM categories")
#! This fetch only one row.
# c.fetchone()
#! This fetches number of rows which have given as parameter.
# c.fetchmany(2)
#! This fetches all the rows from the table.
# data_fetched = c.fetchall()

#! WHERE Clause
# c.execute("SELECT * FROM categories WHERE count > 49")

#! UPDATE the table the value
# c.execute("UPDATE categories SET category = 'Learner' WHERE count > 400")

#! Delete row
# c.execute("DELETE FROM categories WHERE rowid = 5")

#! ORDER BY - by default ASC so, if we want descending order add DESC at last.
# c.execute("SELECT rowid, * FROM categories ORDER BY rowid DESC")
# con.commit()

# c.execute("SELECT rowid, * FROM categories")
data_fetched = c.fetchall()
for data in data_fetched:
    print(f"{data[0]} | {data[1]} | {data[2]}")

print("Query executed successfully...")
# Commit our command
con.commit()
# Close our connection
con.close()
