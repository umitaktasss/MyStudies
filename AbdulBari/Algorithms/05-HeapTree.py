import math

class Heap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def delete_root(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def search(self, element, index=0):
        if index >= len(self.heap):
            return -1  # Aranan eleman yok

        if self.heap[index] == element:
            return index  # Eleman bulundu

        if self.heap[index] > element:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

            left_search = self.search(element, left_child_index)
            if left_search != -1:
                return left_search

            right_search = self.search(element, right_child_index)
            return right_search
        
        return -1  # Aranan eleman bu alt a�a�ta bulunamaz

    def display_tree(self):
        if len(self.heap) == 0:
            print("Heap is empty.")
            return

        level = 0
        max_index = len(self.heap) - 1
        height = math.ceil(math.log2(len(self.heap) + 1))  # Heap'in y�ksekli�i

        while True:
            start_index = 2**level - 1
            end_index = min(2**(level + 1) - 2, max_index)

            if start_index > max_index:
                break

            # Her seviyede uygun bo�luklar� ayarlama
            spaces = ' ' * (2**(height - level - 1) - 1)
            between_spaces = ' ' * (2**(height - level) - 1)

            print(spaces, end='')
            for i in range(start_index, end_index + 1):
                print(f"{self.heap[i]:2}", end=between_spaces)

            print()  # Yeni sat�r i�in

            level += 1

print("""*********************************************************
Yapmak Istediginiz Islemi Secin:
1-Display Tree
2-Delete 
3-Insert Element     
4-Search Element     
Cikis icin * basiniz      
*********************************************************""")

heap = Heap()

while True:
    a = input("Isleminiz: ")
    if a == "1":
        heap.display_tree()
    elif a == "2":
        heap.delete_root()
        print("Kok eleman silindi.")
    elif a == "3":
        while True:
            element = int(input("Eklemek istediginiz sayiyi giriniz (-1 ile cikis yapabilirsiniz): "))
            if element == -1:
                break
            heap.insert(element)
            print(f"Eleman {element} eklendi.")
    elif a == "4":
        element = int(input("Aramak istediginiz sayiyi giriniz: "))
        index = heap.search(element)
        if index != -1:
            print(f"Eleman bulundu! Index: {index}")
        else:
            print("Eleman bulunamadi.")
    elif a == "*":
        print("Cikis yapiliyor...")
        break
    else:
        print("Yanlis Islem")

            
    