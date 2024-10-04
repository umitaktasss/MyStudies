# Structure of the Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List Class with all methods
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at the beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = None
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # Insert at a specific position
    def insert_position(self, data, position):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        if position == 0:
            self.insert_beginning(data)
            return
        current = self.head
        index = 0

        while current is not None and index < position:
            position_prev = current
            current = current.next
            index += 1

        if current is None:
            self.insert_end(data)
            return
        new_node.next = current
        new_node.prev = position_prev
        position_prev.next = new_node
        current.prev = new_node

    # Delete the first node
    def delete_beginning(self):
        if self.head is None:
            print("The list is empty.")
            return
        # If only one element in the list
        if self.head.next is None:
            del self.head
            self.head = None
            self.tail = None
            return
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        del temp

    # Delete the last node
    def delete_end(self):
        if self.head is None:
            print("The list is empty.")
            return
        if self.tail.prev is None and self.head.next is None:
            del self.head
            self.head = None
            self.tail = None
            return
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        del temp

    # Delete a node at a specific position
    def delete_position(self, position):
        if self.head is None:
            print("The list is empty.")
            return
        if position == 0:
            self.delete_beginning()
            return
        current = self.head
        prev = None
        index = 0
        while current is not None and index < position:
            prev = current
            current = current.next
            index += 1
        if current is None:
            print("Position out of bounds.")
            return

        if current.next is None:
            self.tail = prev
            prev.next = None
        else:
            prev.next = current.next
            current.next.prev = prev

        del current

    # Find an element in the list
    def find_element(self, data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                print(f"Element '{data}' found at index {index}.")
                return True, index
            current = current.next
            index += 1
        print(f"Element '{data}' not found in the list.")
        return False, -1

    # Display all elements in the list
    def display(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

    # Count the number of elements in the list
    def count_list(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    # Delete the entire list
    def delete_list(self):
        current = self.head
        while current:
            auxiliary_node = current.next
            print(f"Deleting node with data: {current.data}")
            del current
            current = auxiliary_node

        self.head = None
        self.tail = None
        print("The entire list has been deleted!")




dll = DoublyLinkedList()

# Example 1: Insert elements at the beginning
# Example 1: Insert elements at the beginning

print("Inserting elements at the beginning:")
dll.insert_beginning(30)
dll.insert_beginning(20)
dll.insert_beginning(10)
dll.display()  # Expected output: 10 <-> 20 <-> 30

# Example 2: Insert elements at the end

print("\nInserting elements at the end:")
dll.insert_end(40)
dll.insert_end(50)
dll.display()  # Expected output: 10 <-> 20 <-> 30 <-> 40 <-> 50

# Example 3: Insert an element at a specific position

print("\nInserting elements at a specific position:")
dll.insert_position(25, 2)  # Insert 25 at index 2
dll.insert_position(35, 4)  # Insert 35 at index 4
dll.display()  # Expected output: 10 <-> 20 <-> 25 <-> 30 <-> 35 <-> 40 <-> 50

# Example 4: Find an element in the list

print("\nFinding elements:")
found, index = dll.find_element(25)  # Expected: "Element '25' found at index 2."
found, index = dll.find_element(60)  # Expected: "Element '60' not found in the list."

# Example 5: Count the elements in the list

print("\nCounting elements in the list:")
count = dll.count_list()
print(f"Number of elements in the list: {count}")  # Expected output: 7

# Example 6: Delete the first node

print("\nDeleting the first node:")
dll.delete_beginning()
dll.display()  # Expected output: 20 <-> 25 <-> 30 <-> 35 <-> 40 <-> 50

# Example 7: Delete the last node

print("\nDeleting the last node:")
dll.delete_end()
dll.display()  # Expected output: 20 <-> 25 <-> 30 <-> 35 <-> 40

# Example 8: Delete a node at a specific position

print("\nDeleting a node at a specific position:")
dll.delete_position(2)  # Deletes the node at index 2
dll.display()  # Expected output: 20 <-> 25 <-> 35 <-> 40

# Example 9: Delete the entire list

print("\nDeleting the entire list:")
dll.delete_list()
dll.display()  # Expected output: "The list is empty."