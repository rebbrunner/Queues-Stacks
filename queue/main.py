from queue import Queue

myQueue = Queue()
myQueue.enqueue(5)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(1)
print(myQueue.items)
myQueue.insertion_sort()
print(myQueue.items)
print(myQueue.binary_search(6))