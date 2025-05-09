# GROUP-ASSIGNMENT

# DoublyLinkedList;
-The code has a class Node that contains .data-tostore the values, .next-to point to the next node, .prev-to point to the previous node
-It has a class DoublyLinkedList that initializes an empty doubly linked list and self.head-to keep track of the first node in the list
-It also has an .append method that creates a new node with the data that has been input, it adds the new node at the end
-The .prepend method that creates a new node and adds it at the begining, it updates the prev pointer of the old head
-The Delete method finds the node with the given data the updates the next pointer of the previous node and updates the prev pointer of the next node
-The search method looks for the node with the given key then returns true if found
