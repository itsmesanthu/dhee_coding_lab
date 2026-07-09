class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def print_list(self, head):
        if head is None:
            print("Linked List is Empty")
            return

        c = head
        while c:
            print(c.data, end=" -> ")
            c = c.next
        print("None")

    def count(self, head):
        count = 0
        c = head
        while c:
            count += 1
            c = c.next
        return count

    def insert_begin(self, head, data):
        new = Node(data)
        new.next = head
        return new

    def insert_end(self, head, data):
        new = Node(data)

        if head is None:
            return new

        c = head
        while c.next:
            c = c.next

        c.next = new
        return head

    def insert_position(self, head, data, pos):
        new = Node(data)

        if pos == 1:
            new.next = head
            return new

        c = head
        count = 1

        while c is not None and count < pos - 1:
            c = c.next
            count += 1

        if c is None:
            print("Invalid Position")
            return head

        new.next = c.next
        c.next = new

        return head

    def delete_begin(self, head):
        if head is None:
            return None
        return head.next

    def delete_end(self, head):
        if head is None:
            return None

        if head.next is None:
            return None

        c = head
        while c.next.next:
            c = c.next

        c.next = None
        return head

    def delete_position(self, head, pos):

        if head is None:
            return None

        if pos == 1:
            return head.next

        c = head
        count = 1

        while c is not None and count < pos - 1:
            c = c.next
            count += 1

        if c is None or c.next is None:
            print("Invalid Position")
            return head

        c.next = c.next.next
        return head


ll = LinkedList()
head = None

while True:

    print("\n===== Linked List Menu =====")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Print Linked List")
    print("8. Count Nodes")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        head = ll.insert_begin(head, data)

    elif choice == 2:
        data = int(input("Enter data: "))
        head = ll.insert_end(head, data)

    elif choice == 3:
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        head = ll.insert_position(head, data, pos)

    elif choice == 4:
        head = ll.delete_begin(head)

    elif choice == 5:
        head = ll.delete_end(head)

    elif choice == 6:
        pos = int(input("Enter position: "))
        head = ll.delete_position(head, pos)

    elif choice == 7:
        ll.print_list(head)

    elif choice == 8:
        print("Total Nodes =", ll.count(head))

    elif choice == 9:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")