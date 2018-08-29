#dequeue-test-cases
#Rebecca Brunner
#29 August 2018
#Test dequeue class structure and methods

from random import *
from dequeue import Dequeue

#Create deqeueue
myDequeue = Dequeue()

#Add items to dequeue
for i in range(5):
    myDequeue.pushFront(randint(1, 6))
print(myDequeue.items)

#Sort items in dequeue
myDequeue.insertion_sort()
print(myDequeue.items)