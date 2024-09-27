from pdb import _rstr


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        


class CircularLinkedList:
    
    def __init__(self):
        self.head = None
        


    def insert_at_end(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            
            temp.next = new_node
            new_node.next = self.head
        
            
        temp = None
        
    def list_length(self):
        if self.head is None:
            print("The list is empty.")
        count = 0
        current = self.head
        
        while True:
            count +=1
            current = current.next
            if current == self.head:
                break
        return count
    
    def display_list(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head

        
        while True:
            print(current.data, end ="->")
            current = current.next
            if current == self.head:
                break
        
        print ("Head") #Dairesel yapıyı belirtmek için.
        

    
scll=CircularLinkedList()
scll.insert_at_end(11)
scll.insert_at_end(13)
scll.insert_at_end(15)
scll.display_list()
