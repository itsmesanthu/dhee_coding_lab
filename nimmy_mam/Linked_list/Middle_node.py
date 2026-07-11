class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def middle_node(self,head):
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        return s
    
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n6=Node(70)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
l=Node(n1)
res=l.middle_node(n1)
print(res.data)