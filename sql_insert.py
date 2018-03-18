import sqlite3
from random import randint

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	try:
		c.execute("""CREATE TABLE numbers(ints INT)""")
	except:
		print ("oops exception")


	

	for i in range(0,100):
		randinteger = randint(0,10000)
		print (randinteger)
		c.execute("INSERT INTO numbers VALUES({})".format(randinteger))






	



