#Create a SQLite3 database and table

#import the SQLite3 library
import sqlite3

# create the connection object

conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands

cursor = conn.cursor()

try:

	#insert data
	cursor.execute("""INSERT INTO populations VALUES('New York City', 'NY', 8400000)""")
	cursor.execute("""INSERT INTO populations VALUES('San Francisco', 'CA', 8000000)""")


	#commit the changes

	conn.commit()
except sqlite3.Error as er:

	print ("Ooops!, something went wrong. Try again... ", er)


#close the database connection

conn.close()
