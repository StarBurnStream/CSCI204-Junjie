from sStack import *

class Node:
    def __init__(self):
        self.next = None
        self.data = []

class SLink:
    def __init__(self):
        self.head=None
        self.size=0
        aStack=SStack()
        for i in range(100):
            node=Node()
            aStack.push(node)
        self.stack=aStack

    def __len__(self):
        return self.size


    def add(self, data):
        if self.stack.size==0:
            newNode = Node()

        else:
            newNode=self.stack.pop()

        newNode.data.append(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1


            
    def remove(self, data):
        #Removes a node from the list
        prunner = None
        runner = self.head
        while runner != None and runner.data[0] != data:
            prunner = runner
            runner = runner.next

        if runner == None:
            #It was not found, so no work to do
            return -1

        #Remove node
        if runner == self.head:
            #head case
            self.head = runner.next
        else:
            #nonhead case
            prunner.next = runner.next
        runner.data=[]
        runner.next=None
        self.stack.push(runner)

    def __iter__(self):
        return SLinkIterator(self.head)


class SLinkIterator:

    def __init__(self, head):
        self.runner = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.runner == None:
            raise StopIteration
        else:
            item = self.runner.data
            self.runner = self.runner.next
            return item


def main():
    a=SLink()
    a.add('a')
    print(a.head.data)
    a.add('b')
    
    print(a.head.data)
    print(a.head.next.data)
#main()
