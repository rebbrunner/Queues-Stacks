#dequeue-test-cases
#Rebecca Brunner
#29 August 2018
#Test dequeue class structure and methods

from random import *
from dequeue import Dequeue

#Create deqeueue
d1 = Dequeue()
for i in range(5):
	d1.pushBack(randint(1, 5))
print("Dequeue 1 is: ", d1.items)
d2 = Dequeue()
for i in range(5):
	d2.pushBack(randint(1, 5))
print("Dequeue 2 is: ", d2.items)

d1.insertion_sort()
print("Dequeue 1, sorted with an insertion sort: ", d1.items)
d2.merge_sort()
print("Dequeue 2, sorted with a merge sort:", d2.items)

if(d1.binary_search(4)) != None:
	print("Searching for 4 in d1 with a binary search, 4 is in position ", d1.binary_search(4))
else:
	print("Searching for 4 in d1 with a binary search, 4 was not found.")

if(d2.binary_search(4)) != None:
	print("Searching for 4 in d2 with a binary search, 4 is in position ", d2.binary_search(4))
else:
	print("Searching for 4 in d2 with a binary search, 4 was not found.")