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

    def insertion_sort(self):
        i, j = 1, 1
        while (i < len(self.items)):
            j = i
            while (j > 0 and self.items[j-1] > self.items[j]):
                self.items[j], self.items[j-1] = self.items[j-1], self.items[j]
                j -= 1
            i += 1

    def binary_search(self, item):
        l, r = 0, 0
        while (l < r):
            mid = (l + r) / 2
            if (self.items[mid] < item):
                l = mid + 1
            else if (self.items[mid] > item):
                r = mid - 1
            else if (self.items[mid] = item):
                return mid
        return 0