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

    def binary_search(self, item):
        left = 0
        right = len(self.items)
        right -= 1
        while (left <= right):
            middle = int((left + right) / 2)
            if (self.items[middle] < item):
                left = middle + 1
            elif (self.items[middle] > item):
                right = middle - 1
            elif (self.items[middle] == item):
                return middle
        return None

    def merge_sort(self):
        self.merge_sort_main(self.items)

    def merge_sort_main(self, A):
        if len(A) > 1:
            mid = len(A)//2
            l = A[:mid]
            r = A[mid:]

            self.merge_sort_main(l)
            self.merge_sort_main(r)

            i, j, k = 0, 0, 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    A[k] = l[i]
                    i += 1
                else:
                    A[k] = r[j]
                    j += 1
                k += 1

            while i < len(l):
                A[k] = l[i]
                i += 1
                k += 1

            while j < len(r):
                A[k] = r[j]
                j += 1
                k += 1