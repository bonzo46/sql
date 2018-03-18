import sqlite3
import sys

user_input ="blah"

while user_input not in ["1","2","3","4","5"]:

	user_input = input(""" Select 1 - 5 from the following list: 
	1: Average 
	2: Maximum 
	3: Minimum
	4: Sum
	5: Exit
	""")
	if user_input not in ["1", "2","3","4","5"]:
		print ("""Sorry you did not choose a correct option.
			Please Try again.

			""")



def sqlAverage():
	return "SELECT avg(ints) FROM numbers"

def sqlMax():
	return "SELECT max(ints) FROM numbers"

def sqlMin():
	return "SELECT min(ints) FROM numbers"

def sqlSum():
	return "SELECT sum(ints) FROM numbers"





with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()








	if user_input == "1":

		#run average function
		print ("You chose 1 - Average")
		result = sqlAverage()

		print ("SQL Executed was", result)

		outputnum = c.execute(result)

		#for r in outputnum:
		print("The Average is:", outputnum.fetchone()[0])





	elif user_input == "2":
		print ("You chose 2 - Maximum")
		#run max function
		result = sqlMax()

		print ("SQL Executed was", result)

		outputnum = c.execute(result)

		#for r in outputnum:
		print("The Maximum is:", outputnum.fetchone()[0])



	elif user_input == "3":
		print ("You chose 3 - Minimum")
		#run min function

		result = sqlMin()

		print ("SQL Executed was", result)

		outputnum = c.execute(result)

		#for r in outputnum:
		print("The Minimum is:", outputnum.fetchone()[0])

	elif user_input == "4":
		#run sum function
		print ("You chose 4 - Sum")

		result = sqlSum()

		print ("SQL Executed was", result)

		outputnum = c.execute(result)

		#for r in outputnum:
		print("The Sum is:", outputnum.fetchone()[0])



	elif user_input == "5":	
		#run exit functio
		print ("You chose 5 - Exit")
		print ("Goodbye, quitting now")
		sys.exit(0)



	else:
		print ("Ooops we got to the else line")






