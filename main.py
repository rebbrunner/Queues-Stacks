from queue import Queue

myQueue = Queue()
myQueue.enqueue(4)
print myQueue.items
myQueue.enqueue('dog')
print myQueue.items
myQueue.enqueue(True)
print myQueue.items
print myQueue.size()
print myQueue.empty()
myQueue.enqueue(8.4)
print myQueue.items
myQueue.dequeue()
print myQueue.items
myQueue.dequeue()
print myQueue.items
print myQueue.size()
print myQueue.empty()
myQueue.dequeue()
print myQueue.items
myQueue.dequeue()
print myQueue.items
print myQueue.size()
print myQueue.empty()