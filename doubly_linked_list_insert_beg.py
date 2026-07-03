import gc

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class doublylinkedlist:
    def __init__(self):
        self.head=None

    def insertatbeg(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return

        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end= " ")
            temp=temp.next

d_linledlist=doublylinkedlist()

d_linledlist.insertatbeg(5)
d_linledlist.insertatbeg(2)
d_linledlist.insertatbeg(1)

d_linledlist.printlist()
