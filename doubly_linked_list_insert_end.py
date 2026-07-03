import gc

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class doubly_linked_list():
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return

        temp=self.head

        while temp.next:
            temp=temp.next

        temp.next=new_node

        new_node.prev=temp

        return
        

    def printlist(self):
        temp=self.head

        while temp:
            print(temp.data,end= " ")
            temp=temp.next

d1=doubly_linked_list()

d1.insert_at_end(5)
d1.insert_at_end(4)
d1.insert_at_end(2)

d1.printlist()
