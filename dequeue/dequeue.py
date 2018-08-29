#Dequeue Class
#Rebecca Brunner
#29 August 2018
#Implement Dequeue class

class Dequeue():
    def __init__(self):
        self.items = []

    def pushFront(self, item):
        self.items.append(item)

    def pushBack(self, item):
        self.items.insert(0, item)

    def popFront(self):
        return self.items.pop()

    def popBack(self):
        return self.items.pop(0)

    def checkEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)