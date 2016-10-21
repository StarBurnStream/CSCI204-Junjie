import sLink
class Node:
    def __init__(self):
        self.next = None
        self.data = []


class SStack:
    def __init__(self):
        self.head=None
        self.size=0

    def push(self,item):
        if self.size==0:
            self.head=item
        else:
            item.next=self.head
            self.head=item
        self.size+=1
            
    def pop(self):
        if self.size!=0:
            a=self.head
            self.head=self.head.next
            a.next=None
            self.size-=1
        return a
