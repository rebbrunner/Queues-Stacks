#Heap
#Rebecca Brunner
#4 September 2018
#Implement Heap Data Structure

class Heap():
    def __init__(self):
        self.list = [0]
        self.size = 0

    def percUp(self, index):
        while index // 2 > 0:
            if self.list[index] < self.list[index // 2]:
                temp = self.list[index//2]
                self.list[index//2] = self.list[index]
                self.list[index] = temp
            i = i // 2

    def insert(self, item):
        self.list.append(item)
        self.size = self.size + 1
        self.percUp(self.size)

    def percDown(self, index):
        while (index * 2) <= self.size:
            minimum = self.smallest(index)
            if self.list[index] > self.list[minimum]:
                temp = self.list[index]
                self.list[index] = self.list[minimum]
                self.list[minimum] = temp
            i = minimum

    def smallest(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.list[index * 2] < self.list[index*2+1]:
                return index * 2
            else:
                return index * 2 + 1

    def deleteSmallest(self):
        val = self.list[1]
        self.list[1] = self.list[self.size]
        self.size = self.size - 1
        self.list.pop()
        self.percDown(1)
        return val

    def checkEmpty(self):
        return self.list == [0]

    def size(self):
        return self.size

    def buildFromList(self, list):
        index = len(list)//2
        self.size = len(list)
        self.list = [0] + list[:]
        while (index > 0):
            self.percDown(index)
            index = index - 1