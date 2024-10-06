
class Node:
    #Constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    #method for setting the data field of the node
    def setData(self, data):
        self.data = data
    #method for setting the next field of the dote
    def getData(self):
        return self.data
    #method for setting the field of the node
    def setNext(self, next):
        self.next = next
    #method for getting the next field of the node
    def getNext(self):
        return self.next
    #returns true if the node points to another node
    def hasNext(self):
        return self.next is not None


class LinkedList:
    #initializing a list
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def find_element(self, data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                return True, index
            current = current.next
            index += 1
        return False, -1

    def list_length(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count
    #method for inserting a new node at the end of a Linked List
    def insert_end(self, data):
        new_node = Node()
        new_node.data = data
        if self.tail is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    #method for inserting a new node at the beginning of the Linked List(at the head)
    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.data=data
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    #method for inserting a new node at any position in a linked list
    def insert_at_position(self, position, data):
        if position > self.length or position < 0:
            return None

        if position == 0:
            self.insert_at_beginning(data)
            return

        if position == self.length:
            self.insert_end(data)
            return

        new_node = Node()
        new_node.data = data
        count = 0
        current = self.head
        while count < position - 1:
            current = current.next
            count += 1
        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def delete_at_beginning(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            if self.length == 1:  # If there was only one node, reset tail
                self.tail = None
            self.length -= 1

    def deleteFromLinkedListWithNode(self, node):
        if self.length == 0:
            raise ValueError("List is empty.")
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current == node:
                found = True
            else:
                previous = current
                current = current.next

        if current is None:
            raise ValueError("Node not in Linked List")

        if current == self.head:
            self.delete_at_beginning()
        else:
            previous.next = current.next
            if current == self.tail:
                self.delete_last_node()

        self.length -= 1

    def delete_last_node(self):
        if self.length == 0:
            print("The list is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp_tail = self.head
            previous = None

            while temp_tail.next is not None:
                previous = temp_tail
                temp_tail = temp_tail.next

            self.tail = previous
            previous.next = None
        self.length -= 1

    def deleteAtPosition(self, pos):
        if pos >= self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
            return

        count = 0
        currentnode = self.head
        previousnode = None

        if pos == 0:
            self.head = currentnode.next
            if self.length == 1:
                self.tail = None
            self.length -= 1
            return

        while currentnode is not None and count < pos:
            count += 1
            previousnode = currentnode
            currentnode = currentnode.next

        if count == pos and currentnode is not None:
            previousnode.next = currentnode.next
            if currentnode == self.tail:
                self.tail = previousnode
            self.length -= 1
    def deleteWithValue(self, value):
        if self.head is None:  # Check if the list is empty
            print("The list is empty.")
            return

        currentnode = self.head
        previousnode = None

        # Case 1: If the node to be deleted is the head
        if currentnode.data == value:
            self.head = currentnode.next
            if currentnode == self.tail:  # If there was only one node, update tail
                self.tail = None
            self.length -= 1
            return

        # Traverse through the list to find the node with the value
        while currentnode is not None:
            if currentnode.data == value:
                previousnode.next = currentnode.next
                if currentnode == self.tail:  # If the node is the tail, update the tail
                    self.tail = previousnode
                self.length -= 1
                return
            previousnode = currentnode
            currentnode = currentnode.next

        # If the loop ends and value was not found
        print("The value provided is not present.")



    def clear(self):
        self.head = None
        self.tail = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next





# Creating an instance of the LinkedList class
llist = LinkedList()

# Insert elements at the end
print("Inserting elements at the end:")
llist.insert_end(10)
llist.insert_end(20)
llist.insert_end(30)
llist.insert_end(40)
llist.display()  # Expected output: 10 -> 20 -> 30 -> 40

# Insert an element at the beginning
print("\nInserting element at the beginning:")
llist.insert_at_beginning(5)
llist.display()  # Expected output: 5 -> 10 -> 20 -> 30 -> 40

# Insert an element at a specific position (index 2)
print("\nInserting element at position 2:")
llist.insert_at_position(2, 15)
llist.display()  # Expected output: 5 -> 10 -> 15 -> 20 -> 30 -> 40

# Find an element
print("\nFinding element 20:")
found, index = llist.find_element(20)
if found:
    print(f"Element 20 found at index {index}")
else:
    print("Element 20 not found")

# Delete the first element (head)
print("\nDeleting the first element (head):")
llist.delete_at_beginning()
llist.display()  # Expected output: 10 -> 15 -> 20 -> 30 -> 40

# Delete an element with a specific value (20)
print("\nDeleting the element with value 20:")
llist.deleteWithValue(20)
llist.display()  # Expected output: 10 -> 15 -> 30 -> 40

# Delete an element at a specific position (index 1)
print("\nDeleting element at position 1:")
llist.deleteAtPosition(1)
llist.display()  # Expected output: 10 -> 30 -> 40

# Delete the last element (tail)
print("\nDeleting the last element (tail):")
llist.delete_last_node()
llist.display()  # Expected output: 10 -> 30

# Clear the entire list
print("\nClearing the list:")
llist.clear()
llist.display()  # Expected output: No output (empty list)


