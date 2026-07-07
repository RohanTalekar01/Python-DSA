class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular_linkedlist:
    def __init__(self):
        self.last=None

    def addToEmpty(self, data):

        if self.last is not None:
            return self.last

        new_node = Node(data)

        self.last = new_node
        self.last.next = self.last

        return self.last

    def add_Front(self,data):
        if self.last==None:
            return self.addToEmpty(data)

        new_node=Node(data)

        new_node.next=self.last.next

        self.last.next=new_node

        return self.last

    def add_end(self,data):
        if self.last==None:
            return self.addToEmpty(data)

        new_node=Node(data)

        new_node.next=self.last.next

        self.last.next=new_node

        self.last=new_node

        return self.last

    def after(self,data,item):

        if self.last is None:
            return None

        p = self.last.next

        while True:

            if p.data == item:

                new_node = Node(data)

                new_node.next = p.next
                p.next = new_node

                if p == self.last:
                    self.last = new_node

                return self.last

            p = p.next

            if p == self.last.next:
                print(item, "The given node is not present in the list")
                break

    def printlist(self):

        if self.last is None:
            print("The list is empty")
            return

        temp = self.last.next

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.last.next:
                break
            

if __name__=="__main__":

    cll = Circular_linkedlist()

    last = cll.addToEmpty(10)
    last = cll.add_end(80)
    last = cll.add_Front(5)
    last = cll.after(15, 10)

    cll.printlist()


                
                
        
