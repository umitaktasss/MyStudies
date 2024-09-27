class Node:
    def __init__(self, data):
        self.data = data   
        self.prev = None
        self.next = None
        
class XORLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.nodes = {}
        
    def _xor (self, a, b):
        #Helper function to get the XOR of two IDS
        return a ^ b
    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_id = id(new_node)
        self.nodes[new_id] = new_node
        
        
        
    

