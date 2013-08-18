def print_list(list):
	for item in list:
		print(item)

list1 = ["Ro.bin", "S.mith", "is", "fu.ll", "o.f.", "d.o.t.s!"]
list2 = [word.replace(".", "") for word in list1]
print_list(list2)
