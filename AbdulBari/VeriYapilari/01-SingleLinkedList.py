class Node:
    #Node initilazed, holds data and has next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

    #Main and Auxiliary Operations
class LinkedList:
    #Tail and head initilazed
    def __init__(self):
        self.head = None
        self.tail = None

    #Traverse in LinkedList and find element
    def find_element(self, data):
        current = self.head  
        index = 0  
        while current is not None: 
            if current.data == data:  
                return True, index  
            current = current.next  
            index += 1  
        return False, -1 
    #Traverse in list and count how many element in current list
    def list_length(self):
        current = self.head  
        count = 0 
        while current is not None:
            count += 1
            current = current.next  
        return count

    # Insert element at the end
    def insert_end(self, data):
        new_node = Node(data)  
        if self.head is None:  
            self.head = new_node  
            self.tail = new_node  
        else:
            self.tail.next = new_node   
            self.tail = new_node  

    #Insert element at the beginning
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node
        
        # Insert element at a specific position
    def insert_at_position(self, position, data):
        new_node = Node(data)  
        if position == 0:  
            self.insert_at_beginning(data)
            return
            
        else:
            current = self.head  
            previous = None  
            index = 0  

            
            while current is not None and index < position:
                previous = current 
                current = current.next  
                index += 1 

            # Insert new node at the correct position
            if previous is not None:
                new_node.next = current  
                previous.next = new_node  
                if new_node.next is None:
                    self.tail = new_node
            else:
                print("Position out of bounds")
    
    def delete_at_beginning(self):

        if self.head is None:
            print("The list is empty.")
            return
        temp = self.head
        self.head = self.head.next
        del temp

    #Delete node at position
    def delete_node_at_position(self, position):
        if self.head is None:  
            print("List is empty.")
            return


        if position == 0:
            self.delete_at_beginning()
            return

        
        current = self.head
        previous = None
        index = 0

        
        while current is not None and index < position:
            previous = current
            current = current.next
            index += 1

        if current is None:
            print("Position does not exist.")
            return

        
        previous.next = current.next  
        del current 
        


    def delete_last_node(self):
        if self.head is None:  
            print("List is empty.")
            return

        
        if self.head == self.tail:
            self.head = None  
            self.tail = None  
            return

       
        temp_tail = self.head
        previous = None

        
        while temp_tail.next is not None:  
            previous = temp_tail
            temp_tail = temp_tail.next

        
        self.tail = previous
        previous.next = None

        del temp_tail

    
    def delete_list(self):
        current = self.head

        while current:
            auxiliary_node = current.next  
            print(f"Deleting node with data: {current.data}")  
            del current 
            current = auxiliary_node  

        self.head = None  
        self.tail = None

   
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next




llist = LinkedList()
llist.insert_end(10)
llist.insert_end(20)
llist.insert_end(30)
llist.insert_end(40)

print("List:")
llist.display()

print("List length:", llist.list_length())

llist.insert_at_position(2, 25)
print("25 has been added to the list:")
llist.display()

llist.delete_last_node()
print("Last node has been deleted:")
llist.display()

llist.delete_node_at_position(1)
print("The second node has been deleted:")
llist.display()

print("Does the list include 30?", llist.find_element(30))

llist.delete_list()
print("All nodes have been removed, the list has been deleted:")
llist.display() 


