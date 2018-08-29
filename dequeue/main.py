#dequeue-test-cases
#Rebecca Brunner
#29 August 2018
#Test dequeue class structure and methods

from dequeue import Dequeue

#Create deqeueue
myDequeue = Dequeue()

#Check if dequeue is empty or not
print(myDequeue.checkEmpty())

#Push 4 to back of dequeue
myDequeue.pushBack(4)
print(myDequeue.items)

#Push 'dog' to back of dequeue
myDequeue.pushBack('dog')
print(myDequeue.items)

#Push 'cat' to front of dequeue
myDequeue.pushFront('cat')
print(myDequeue.items)

#Push True to front of dequeue
myDequeue.pushFront(True)
print(myDequeue.items)

#Check size of dequeue
print(myDequeue.size())

#Check if dequeue is empty or not
print(myDequeue.checkEmpty())

#Push 8.4 to back of dequeue
myDequeue.pushBack(8.4)
print(myDequeue.items)

#Pop item off the back
myDequeue.popBack()
print(myDequeue.items)

#Pop item off the front
myDequeue.popFront()
print(myDequeue.items)