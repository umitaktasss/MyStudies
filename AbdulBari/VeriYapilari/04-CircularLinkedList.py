# Node class to represent each element in the Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# CircularLinkedList class to manage the list operations
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Method to count the number of nodes in the circular linked list
    def list_length(self):
        if self.head is None:
            print("The list is empty.")
            return 0
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    # Method to display all elements of the circular linked list
    def display_list(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")  # To show it's circular.

    # Method to insert a node at the end of the circular linked list
    def insert_end(self, data):
        new_node = Node(data)
        new_node.next = new_node  # Initial setup for the node

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node

    # Method to insert a node at the front of the circular linked list
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = new_node  # Initial setup for the node

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    # Method to delete the last node in the circular linked list
    def delete_lastNode(self):
        if self.head is None:
            print("List is empty.")
            return

        tail = self.head
        ptail = None
        while tail.next != self.head:
            ptail = tail
            tail = tail.next

        if ptail is None:  # If there's only one node in the list
            self.head = None
        else:
            ptail.next = self.head
        del tail

    # Method to delete the first node in the circular linked list
    def delete_firstNode(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        if self.head == current:  # Only one node in the list
            self.head = None
        else:
            temp = self.head
            current.next = self.head.next
            self.head = self.head.next
            del temp

    # Method to delete a node at a specific position
    def delete_node_position(self, position):
        if self.head is None:
            print("List is empty.")
            return

        if position == 0:
            self.delete_firstNode()
            return

        current = self.head
        previous = None
        index = 0

        while current.next != self.head and index < position:
            previous = current
            current = current.next
            index += 1

        if current.next == self.head and index != position:
            print("Position out of bounds.")
            return

        if current.next == self.head:  # Deleting the last node
            self.delete_lastNode()
            return

        previous.next = current.next
        del current

    # Method to delete all nodes in the circular linked list
    def delete_all(self):
        if self.head is None:
            print("List is already empty.")
            return

        current = self.head
        while current.next != self.head:
            next_node = current.next
            self.head = next_node
            del current
            current = next_node

        del self.head
        self.head = None
        print("All nodes have been deleted.")

        # Example usage of CircularLinkedList
def example_usage():
    # Create a circular linked list
    cll = CircularLinkedList()
    print("Circular Linked List created.")

    # Insert nodes at the end
    cll.insert_end(10)
    print("Inserted 10 at the end.")
    cll.insert_end(20)
    print("Inserted 20 at the end.")
    cll.insert_end(30)
    print("Inserted 30 at the end.")

    # Display the list
    print("\nDisplaying the current list:")
    cll.display_list()

    # Insert a node at the beginning
    cll.insert_beginning(5)
    print("\nInserted 5 at the beginning.")

    # Display the list
    print("\nDisplaying the updated list:")
    cll.display_list()

    # Count the nodes in the list
    print("\nCounting the nodes in the list:")
    length = cll.list_length()
    print(f"Total nodes in the list: {length}")

    # Delete the first node
    cll.delete_firstNode()
    print("\nDeleted the first node.")

    # Display the list
    print("\nDisplaying the list after deleting the first node:")
    cll.display_list()

    # Delete the last node
    cll.delete_lastNode()
    print("\nDeleted the last node.")

    # Display the list
    print("\nDisplaying the list after deleting the last node:")
    cll.display_list()

    # Delete a node at a specific position
    print("\nDeleting node at position 1:")
    cll.delete_node_position(1)

    # Display the list
    print("\nDisplaying the list after deleting node at position 1:")
    cll.display_list()

    # Count the nodes again
    print("\nCounting the nodes in the list after deletions:")
    length = cll.list_length()
    print(f"Total nodes in the list: {length}")

    # Delete all nodes
    cll.delete_all()
    print("\nDeleted all nodes.")

    # Attempt to display the empty list
    print("\nDisplaying the list after deleting all nodes:")
    cll.display_list()


# Run the example usage
example_usage()
