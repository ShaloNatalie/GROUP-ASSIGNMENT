class Library:
    def __init__(self,data):
        self.data = data
        self.next = None


class Books:
    def __init__(self):
        self.head = None     

    def append(self, data):

        new_Library = Library(data)

        if self.head is None:
            self.head = new_Library
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = new_Library

    def presentBooks(self):
        current = self.head

        while current is not None:

            print(current.data, end=" -> ") 

            current = current.next
        print("None")

if __name__ =="__main__":
    catalog = Books()

    catalog.append("The Great Gatsby")
    catalog.append("Chozi la Heri")
    catalog.append("Psychology of Money")
    catalog.append("Blossoms of the Savannah")

    catalog.presentBooks()
        