# GROUP-ASSIGNMENT
# Singly linked list
- The code has a class Library that contains a .data to store the books present in our Library and a .next to point to the next book present in our catalog
- It has a class Books that basically stores the string variable of books in our catalog(list)
- There is an append() method that adds a new node (Library).  
- There is a method presentBooks() that checks whether there is another node in the list;if not, the current node becomes the head. If there is already a node the current node acts as the head.
- In the main method an object of the class Books is created and titles of the Books are added to the list and displayed.
  
# DoublyLinkedList;
- The code has a class Node that contains .data-tostore the values, .next-to point to the next node, .prev-to point to the previous node
- It has a class DoublyLinkedList that initializes an empty doubly linked list and self.head-to keep track of the first node in the list
- It also has an .append method that creates a new node with the data that has been input, it adds the new node at the end
- The .prepend method that creates a new node and adds it at the begining, it updates the prev pointer of the old head
- The Delete method finds the node with the given data the updates the next pointer of the previous node and updates the prev pointer of the next node
- The search method looks for the node with the given key then returns true if found
 
 # CircularLinkedList 
- Node class holds .data for values and .next for linking to the next node.
- CircularLinkedList class starts with self.head = None to track the first node.
- .add adds a new node at the end and links it back to the head to form a loop.
- If the list is empty, .append sets the new node as head and points it to itself.
- If not empty, .append finds the last node, links it to the new node, and loops back to head.
- .display prints each node's data until it reaches the head again, showing it's circular.

 
