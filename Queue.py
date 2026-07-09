class Queue():
    def __init__(self,k):
        self.k=k
        self.queue=[None]*k
        self.head  = -1
        self.tail = -1

    def isEmpty(self):
        return self.head == -1


    def enqueue(self,data):
        if self.tail == self.k - 1:
            print("The Queue is full\n")

        elif self.head == -1:
            self.head=0
            self.tail=0
            self.queue[self.tail]= data

        else:
            self.tail = self.tail + 1
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print("this queue is an empty\n")

        elif self.head == self.tail:
            temp= self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp

        else:
            temp=self.queue[self.head]
            self.head=self.head + 1
            return temp

    def peek(self):
        if self.isEmpty():
            print("The Queue is empty")
            return None
        return self.queue[self.head]

    def printqueue(self):
        if self.head == -1:
            print("No element in the queue")
        else:
            for i in range(self.head,self.tail+1):
                print(self.queue[i],end=" ")
            print()


q = Queue(5)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print("Initial Queue : ")
q.printqueue()

print("Is Queue Empty?", q.isEmpty())

print("Front Element (Peek):", q.peek())

print("Dequeued Element:", q.dequeue())

print("After removing an element from the queue")
q.printqueue()

print("Front Element (Peek):", q.peek())
