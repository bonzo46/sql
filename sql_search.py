import sqlite3

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





def sqlAverage:
	return "SELECT avg(ints) FROM numbers"





if user_input == "1":
	#run average function
	print ("You chose 1")
elif user_input == "2":
	print ("You chose 2")
	#run max function
elif user_input == "3":
	print ("You chose 3")
	#run min function
elif user_input == "4":
	#run sum function
	print ("You chose 4")
elif user_input == "5":	
	#run exit functio
	print ("You chose 5")
else:
	print ("Ooops we got to the else line")






