class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        class CircularLinkedList:
            def __init__(self):
                self.head = None

                def add(self, data):
                    new_node = Node(data)
                    if self.head is None:
                        self.head = new_node
                        new_node.next = self.head

                    else:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                            temp.next = new_node

                            def display(self):
                                if self.head is None:
                                    print("None")
                                    return

                                temp=self.head
                                while true:
                                    print(temp.data, end="->")
                                    
                                    temp=temp.next
                                    if temp==self.head:
                                        break
                                        print("(back to head)")
