# Node of a Singly Linked List
class Node:
    # Constructor
    def __init__(self, value=None):
        self.value = value
        self.next = None

# LinkedBlock class
class LinkedBlock:
    # Constructor
    def __init__(self):
        self.head = None
        self.next = None
        self.nodeCount = 0

    blockSize = 2
    blockHead = None

    # Create an empty block
    def newLinkedBlock(self):
        block = LinkedBlock()
        block.next = None
        block.head = None
        block.nodeCount = 0
        return block

    # Create a new node
    def newNode(self, value):
        temp = Node(value)
        return temp

    # Search for the k-th element
    def searchElements(self, blockHead, k):
        # Find the block containing the k-th element
        j = (k + self.blockSize - 1) // self.blockSize
        p = blockHead
        j -= 1
        while j > 0 and p is not None:
            p = p.next
            j -= 1
        fLinkedBlock = p

        # Find the node in the block
        q = p.head
        k = k % self.blockSize
        if k == 0:
            k = self.blockSize
        k = p.nodeCount + 1 - k
        while k > 1:
            q = q.next
            k -= 1
        fNode = q
        return fLinkedBlock, fNode

    # Shift nodes between blocks to maintain block size balance
    def shift(self, A):
        while A.nodeCount > self.blockSize:
            if A.next is None:
                A.next = self.newLinkedBlock()
            B = A.next

            # Shifting the last node of A to the head of B
            temp = A.head
            if A.nodeCount == 1:  # If there's only one element, move it to the next block
                A.head = None
            else:
                while temp.next.next is not None:
                    temp = temp.next
                shiftedNode = temp.next
                temp.next = None

            # Insert the node at the head of B
            shiftedNode.next = B.head
            B.head = shiftedNode
            A.nodeCount -= 1
            B.nodeCount += 1
        return A

    # Add an element at position k
    def addElement(self, k, x):
        if self.blockHead is None:
            self.blockHead = self.newLinkedBlock()
            self.blockHead.head = self.newNode(x)
            self.blockHead.nodeCount += 1
        else:
            if k == 0:
                new_node = self.newNode(x)
                new_node.next = self.blockHead.head
                self.blockHead.head = new_node
                self.blockHead.nodeCount += 1
                self.shift(self.blockHead)
            else:
                r, p = self.searchElements(self.blockHead, k)
                new_node = self.newNode(x)
                new_node.next = p.next
                p.next = new_node
                r.nodeCount += 1
                self.shift(r)
        return self.blockHead

    # Search for an element at position k
    def searchElement(self, blockHead, k):
        _, p = self.searchElements(blockHead, k)
        return p.value

# Testing the implementation
linked_block_list = LinkedBlock()

# Adding elements
linked_block_list.addElement(0, 11)
linked_block_list.addElement(0, 21)
linked_block_list.addElement(1, 19)
linked_block_list.addElement(1, 23)
linked_block_list.addElement(2, 16)
linked_block_list.addElement(2, 35)

# Searching for an element
result = linked_block_list.searchElement(linked_block_list.blockHead, 1)
print("Element found at position 1:", result)
result = linked_block_list.searchElement(linked_block_list.blockHead, 16)
print("Element found at position :", result)







