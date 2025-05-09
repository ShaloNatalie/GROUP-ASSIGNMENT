class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                return
            temp = temp.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True  # Node found
            temp = temp.next
        return False  # Node not found


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)

print(dll.search(20))
print(dll.search(50))