#Queue Class
#Rebecca Brunner
#27 August 2018
#Implement Queue class with creation, searching, sorting, insertion, and deleting.

class queue:
    #Subclasses
    class iterator:
        def __init__(self, queue):
        def __next__(self):

    class node:
        def __init__(self, item, prev = None, next = None):
            self.item = item;
            self.prev = prev;
            self.next = next;

    #Data Structures

    #Functions
    def push_front(self, item):
    def push_back(self, item):

    def pop_front(self,item):
    def pop_back(self, item):

    def sort(self):
    def search(self, item):

    def __iter__(self):