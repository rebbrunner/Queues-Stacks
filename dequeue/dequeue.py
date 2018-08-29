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

    def insertion_sort(self):
        a = self.items
        i, j = 1, 1
        while (i < self.size()):
            j = i
            while (j > 0 and a[j-1] > a[j]):
                a[j-1], a[j] = a[j], a[j-1]
                j -= 1
            i += 1