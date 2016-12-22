
#a = 10
def name(*a):
	""" thin function """
	for n in a:
		print n
	#print name.__doc__


name(1,2,3,4)
