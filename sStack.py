import sLink
class SStack:
    def __init__(self):
        self.head=None

    def push(self,value):
        node=Node()
        node.data=value
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
            
    def pop(self):
        if self.head!=None:
            self.head=self.head.next
