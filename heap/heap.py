#Heap
#Rebecca Brunner
#4 September 2018
#Implement Heap Data Structure

class Heap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while (i // 2) > 0:
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i /= 2

    def insert(self, item):
        self.heapList.append(item)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            child = self.minChild(i)
            if self.heapList[i] > self.heapList[child]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[child]
                self.heapList[child] = temp
            i = child

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delChild(self):
        val = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return val

    def buildFromList(self, myList):
        i = len(myList) // 2
        self.currentSize = len(myList)
        self.heapList = [0] + myList[:]
        while (i > 0):
            self.percDown(i)
            i -= 1
