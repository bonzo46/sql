#Select statement , remove unicoe characters

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# use a for loop to interate through the database, priniting the results line by line

	c.execute("SELECT firstname, lastname from employees")
	
	rows = c.fetchall()

	#output the rows to the screen, row by row

	for r in rows:

		print(r[0], r[1])





		