def linearSearch(x, lst):
	for i in range(len(lst)):
		if lst[i] == x:
			return i
	return False

def binarySearch(x, lst):
    if x < lst[:(len(lst)//2):
        return lst[:(len(lst)//2)]
    else:
        return lst[(len(lst)//2):]

lst = list(range(100))
binarySearch(4, lst)
