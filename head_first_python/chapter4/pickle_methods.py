try:
	import cPickle as pickle
	print('cPickle imported')
except:
	import pickle
	print('pickle imported')

def print_error(err):
	print("An error occured: " + err)

def dump_data(data, filename):
	try:
		with open(filename, 'wb') as file:
			pickle.dump(data, file)
	except IOError as err:
		print_error(err)
		
def load_data(filename):
	try:
		with open(filename, 'rb') as file:
			data = pickle.load(file)
	except IOError as err:
		print_error(err)
	return data
