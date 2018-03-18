#Select statement

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# use a for loop to interate through the database, priniting the results line by line

	for row in c.execute("SELECT firstname, lastname from employees"):
		print (row)

		