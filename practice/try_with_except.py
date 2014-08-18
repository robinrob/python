try:
	with open("file that does not exist!") as data:
		pass
except IOError as err:
    print("An error occurred: " + str(err))
