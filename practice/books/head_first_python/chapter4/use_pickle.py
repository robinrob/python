import pickle_methods

list1 = ['Robin', 'Smith', 'is', 25, 'years', 'old']
pickle_methods.dump_data(list1, 'robin.pickle')
list2 = pickle_methods.load_data('robin.pickle')
print(list2)
