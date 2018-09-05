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
            print(index // 2, " is greater than ", 0)
            if self.list[index] < self.list[index // 2]:
                print(self.list[index], " is less than ", self.list[index//2], " swapping.")
                temp = self.list[index//2]
                self.list[index//2] = self.list[index]
                self.list[index] = temp
            else:
                print(self.list[index], " is greater than or equal to, ", self.list[index//2])
            index = index // 2
            print(self.list)

    def insert(self, item):
        self.list.append(item)
        self.size = self.size + 1
        print("Moving Up")
        self.percUp(self.size)

    def percDown(self, index):
        while (index * 2) <= self.size:
            print("Moving Down")
            minimum = self.smallest(index)
            if self.list[index] > self.list[minimum]:
                print("Swapping", self.list[index], " with ", self.list[minimum])
                temp = self.list[index]
                self.list[index] = self.list[minimum]
                self.list[minimum] = temp
            index = minimum
            print(self.list)

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