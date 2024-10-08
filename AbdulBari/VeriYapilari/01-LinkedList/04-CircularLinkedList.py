# Node class to represent each element in the Circular Linked List
from operator import index


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# CircularLinkedList class to manage the list operations
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.next = None
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next !=None

    def getNode(self, index):
        currentNode = self.head
        if currentNode == None:
            return None
        i = 0
        if index == 0:
            return currentNode
        while i < index and currentNode.next != self.head:
            currentNode = currentNode.next
            i+=1
        if i == index:
           return currentNode
            
        return None

        
    def find_element(self, data):
        if self.head is None:
            print("The list is empty.")
            return False, -1

        current = self.head
        index = 0
        if current.data == data:
            print(f"Element '{data}' found at index '{index}'.")
            return True, index

        current = self.head.next
        index +=1
        while current != self.head:
            if current.data == data:
                print(f"Element '{data}' found at index '{index}'.")
                return True, index
            current = current.next
            index +=1
        print(f"Element '{data}' not found in the list.")
        return False, -1
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
        
        ptail.next = self.head
        tail.next = None
        return

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
            temp.next = None

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
        current.next = None

    def delete_with_data(self, data):
        found, index = self.find_element(data)
        if found:
            self.delete_node_position(index)
        else:
            print(f"Element '{data}' not found, so it cannot be deleted.")
    # Method to delete all nodes in the circular linked list de-referenced
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

def example_usage():
    cll = CircularLinkedList()

    # Inserting nodes at the end: 10 -> 20 -> 30 (circular: head -> 10 -> 20 -> 30 -> head)
    cll.insert_end(10)
    cll.insert_end(20)
    cll.insert_end(30)

    # Display the current list: Expected: 10 -> 20 -> 30 -> head
    print("\nDisplaying the current list:")
    cll.display_list()

    # Inserting node at the beginning: 5 -> 10 -> 20 -> 30 -> head
    cll.insert_beginning(5)

    # Display the updated list: Expected: 5 -> 10 -> 20 -> 30 -> head
    print("\nDisplaying the updated list after inserting 5 at the beginning:")
    cll.display_list()

    # Counting the nodes in the list: Expected: 4 nodes
    print("\nCounting the nodes in the list:")
    length = cll.list_length()
    print(f"Total nodes in the list: {length}")  # Expected: 4

    # Finding element 20: Expected: Element '20' found at index 2
    cll.find_element(20)

    # Getting the node at position 2: Expected: Node at position 2 has data: 20
    print("\nGetting node at position 2:")
    node = cll.getNode(2)
    if node:
        print(f"Node at position 2 has data: {node.data}")
    else:
        print("Node at position 2 does not exist.")

    # Deleting the first node (head): Expected: 10 -> 20 -> 30 -> head
    cll.delete_firstNode()

    # Display the list after deleting the first node: Expected: 10 -> 20 -> 30 -> head
    print("\nDisplaying the list after deleting the first node:")
    cll.display_list()

    # Deleting the last node: Expected: 10 -> 20 -> head
    cll.delete_lastNode()

    # Display the list after deleting the last node: Expected: 10 -> 20 -> head
    print("\nDisplaying the list after deleting the last node:")
    cll.display_list()

    # Deleting node at position 1: Expected: 10 -> head
    cll.delete_node_position(1)

    # Display the list after deleting node at position 1: Expected: 10 -> head
    print("\nDisplaying the list after deleting node at position 1:")
    cll.display_list()

    # Deleting node with data 30: Expected: Element not found, list remains as 10 -> head
    cll.delete_with_data(30)

    # Display the list after trying to delete node with data 30
    print("\nDisplaying the list after trying to delete node with data 30 (not found):")
    cll.display_list()

    # Counting nodes after deletions: Expected: 1 node
    print("\nCounting the nodes in the list after deletions:")
    length = cll.list_length()
    print(f"Total nodes in the list: {length}")  # Expected: 1

    # Deleting all nodes in the list
    cll.delete_all()

    # Display the list after deleting all nodes: Expected: Empty list
    print("\nDisplaying the list after deleting all nodes:")
    cll.display_list()

# Run the updated example usage
example_usage()
