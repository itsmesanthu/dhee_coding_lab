class Node:
    def __init__(self,val):
        self.data=val
        self.prev=None
        self.next=None
    
    def forword(self,head):
        current=head
        while current:
            print(current.data,end="<->")
            current=current.next
        print()
    def backword(self,head):
        current=head
        while current.next:
            current=current.next
        while current:
            print(current.data,end="<->")
            current=current.prev
        print()
n1=Node(20)
n2=Node(30)
n3=Node(40)
n1.next=n2
n2.next=n3
n3.prev=n2
n2.prev=n1
n1.forword(n1)
n1.backword(n1)