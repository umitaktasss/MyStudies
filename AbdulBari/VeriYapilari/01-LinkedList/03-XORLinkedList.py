#New node definition for XOR linked list
class Node:
    #constructor
    def __inti__(self):
        self.data = None
        self.ptrdiff = None
    #method for setting data field of node
    def setData(self,data):
        self.data = data
    
    #method for getting the data field of the node
    def getData(self):
        return self.data
    #method for setting the pointer difference field of the node
    def setPtrDiff(self, prev, next):
        self.ptrdiff = prev ^ next
    #method for getting the next field of the node
    def getPtrDiff(self):
        return self.ptrdiff


#Ptrdiff = pointer to previous node ⊕ pointer to next node


