import gc

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class doubly_linked_list:
    def __init__(self):
        self.head=None

    def del_node(self,dele):
        if self.head is None or dele is None:
            return

        if self.head==dele:
            self.head=dele.next

        if dele.next is not None:
            dele.next.prev=dele.prev

        if dele.prev is not None:
            dele.prev.next=dele.next

        gc.collect()

    def printlist(self):
        temp=self.head

        while temp:
            print(temp.data,end=" ")
            temp=temp.next

d1=doubly_linked_list()

first=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)
fifth=Node(50)
sixth=Node(60)



d1.head=first
first.next=second
second.prev = first

second.next = third
third.prev = second

third.next = fourth
fourth.prev = third

fourth.next = fifth
fifth.prev = fourth

fifth.next=sixth
sixth.prev=fifth

d1.del_node(third)
d1.printlist()
    
