#Queue Class
#Rebecca Brunner
#27 August 2018
#Implement Queue class with creation, searching, sorting, insertion, and deleting.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        if self.size() == 0:
            return True
        else:
            return False