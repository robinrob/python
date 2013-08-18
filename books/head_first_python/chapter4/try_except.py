try:
    data=open("file that does not exist!")
except IOError as err:
    print("An error occurred: " + str(err))
finally:
    if 'data' in locals():
        data.close()
