# Structure of the Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    #method for setting the data field of the node
    def setData(self, data):
        self.data = data
    #method for getting the data field of the node
    def getData(self):
        return self.data
    #method for setting the next field of the node
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next is not None
    def setPrev(self, prev):
        self.prev = prev
    def getPrev(self):
        return self.prev
    def hasPrev(self):
        return self.prev != None
    def __str__(self):
        return "Node [Data = %s]" % (self.data,)

# Doubly Linked List Class with all methods
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    # Insert at the beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length +=1
            return
        new_node.prev = None
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length +=1

    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length +=1
            return
        new_node.next = None
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def getNode(self, index):
        currentNode = self.head
        if currentNode == None:
            return None
        i = 0
        while i < index and currentNode.next is not None:
            currentNode = currentNode.next
            i+=1
        return currentNode
    # Insert at a specific position
    def insert_position(self, index, data):
        new_node = Node(data)
        if self.head is None or index  == 0:
            self.insert_beginning(data)
            return
        temp = self.getNode(index-1)
        
        if temp is None or temp.next is None:
            self.insert_end(data)
        else:
            new_node.next = temp.next
            new_node.prev = temp
            if temp.next is not None:
                temp.next.prev = new_node

            temp.next = new_node
        self.length +=1
    # Delete the first node
    def delete_beginning(self):
        if self.head is None:
            print("The list is empty.")
            return
        # If only one element in the list
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -=1


    # Delete the last node
    def delete_end(self):
        if self.head is None:
            print("The list is empty.")
            return
        if self.tail.prev is None and self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1


    # Delete a node at a specific position
    def delete_position(self, index):
        if self.head is None:
            print("The list is empty.")
            return
        if index ==0:
            self.delete_beginning()
            return
        if index == self.length-1:
            self.delete_end()
            return
        temp = self.getNode(index)

        if temp is None:
            print("The position does not exist")
            return
        temp.prev.next = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev

        self.length -=1


    def deleteWithData(self, data):
      found, index = self.find_element(data)
      if found:
          self.delete_position(index)
      else:
           print(f"Element '{data} not found, so it cannot be deleted.'")

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
        print(f"The list length: {self.length}")

    # Delete the entire list
    def delete_list(self):
        self.head = None
        self.tail = None
        self.length = 0
        print("The entire list has been deleted!")





# Creating an instance of DoublyLinkedList
dll = DoublyLinkedList()

# Insert elements at the beginning
print("Inserting 10, 20, and 30 at the beginning:")
dll.insert_beginning(10)
dll.insert_beginning(20)
dll.insert_beginning(30)
dll.display()  # Expected: 30 <-> 20 <-> 10

# Insert elements at the end
print("\nInserting 40 and 50 at the end:")
dll.insert_end(40)
dll.insert_end(50)
dll.display()  # Expected: 30 <-> 20 <-> 10 <-> 40 <-> 50

# Insert at a specific position
print("\nInserting 25 at position 2:")
dll.insert_position(2, 25)
dll.display()  # Expected: 30 <-> 20 <-> 25 <-> 10 <-> 40 <-> 50

# Find an element
print("\nFinding element 10:")
dll.find_element(10)  # Expected: "Element '10' found at index 3."

# Delete at a specific position
print("\nDeleting element at position 2:")
dll.delete_position(2)
dll.display()  # Expected: 30 <-> 20 <-> 10 <-> 40 <-> 50

# Delete with data
print("\nDeleting element with data 40:")
dll.deleteWithData(40)
dll.display()  # Expected: 30 <-> 20 <-> 10 <-> 50

# Delete the first node
print("\nDeleting the first node:")
dll.delete_beginning()
dll.display()  # Expected: 20 <-> 10 <-> 50

# Delete the last node
print("\nDeleting the last node:")
dll.delete_end()
dll.display()  # Expected: 20 <-> 10

# Count elements in the list
print("\nCounting the number of elements in the list:")
dll.count_list()
# Expected: 2

# Delete the entire list
print("\nDeleting the entire list:")
dll.delete_list()
dll.display()  # Expected: "The list is empty."
dll.count_list()
