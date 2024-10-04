#Node olu�turuldu.
#Nodun bir k�sm� datay� tutacak bir k�sm�ysa nullu g�sterecek.
class Node:
    #Node olu�turuldu, node i�erisinde data ve sonraki node'u i�aret edicek, pointer eklendi.
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    


    def find_element(self, data):
        current = self.head  # Listenin ba��ndan ba�la
        index = 0  # �ndeksi takip etmek i�in saya�
        while current is not None: #Son node'a gelinceye kadar
            if current.data == data:  # E�er eleman bulunursa
                return True, index  # Eleman bulunduysa True ve indeksi d�nd�r
            current = current.next  # Bir sonraki d���me ge�
            index += 1  # �ndeksi bir art�r
        return False, -1
    # Listenin uzunlu�unu hesaplayan fonksiyon
    def list_length(self):
        current = self.head  # listenin ba��ndan ba�la
        count = 0
        while current is not None:
            count += 1
            current = current.next  # Bir sonraki d���me ge�
        return count

    # Listenin sonuna eleman ekleme
    def insert_end(self, data):
        new_node = Node(data)  # Yeni bir d���m olu�tur
        if self.head is None:  # E�er liste bo�sa
            self.head = new_node  # Yeni d���m� listenin ba�� yap
        else:
            current = self.head  # Listenin ba��ndan ba�la
            while current.next is not None:  # Listenin sonuna git
                current = current.next
            current.next = new_node  # Yeni d���m� listenin sonuna ekler

    # Belirli bir pozisyona eleman ekleme
    def insert_at_position(self, position, data):
        new_node = Node(data)  # Yeni d���m olu�tur
        if position == 0:  # E�er ba�a ekleniyorsa
            new_node.next = self.head  # Yeni d���m�n next'i eski head'i g�sterir
            self.head = new_node  # Head yeni d���m� i�aret eder
        else:
            current = self.head  # Listeyi dola�mak i�in ge�ici i�aret�i
            previous = None  # Bir �nceki d���m� saklamak i�in i�aret�i
            index = 0  # Mevcut pozisyonu tutan saya�

            # �stenen pozisyona kadar listeyi dola�
            while current is not None and index < position:
                previous = current  # Bir �nceki d���m kaydedilir
                current = current.next  # Bir sonraki d���me ge�ilir
                index += 1  # �ndeksi art�r

            # Yeni d���m� istenilen pozisyona ekle
            if previous is not None:
                new_node.next = current  # Yeni d���m�n next pointer'�, current'i i�aret eder
                previous.next = new_node  # Bir �nceki d���m�n next pointer'�, yeni d���m� i�aret eder

    def delete_node_at_position(self, position):
        if self.head is None:  # Eğer liste boşsa
            print("List is empty.")
            return

        # İlk düğümü silmek istiyorsak
        if position == 0:
            temp = self.head  # İlk düğümü geçici olarak tut
            self.head = self.head.next  # Head'i bir sonraki düğüme güncelle
            temp = None  # Geçici düğümü serbest bırak
            return

        # Orta veya son düğümü silmek için listeyi gez
        current = self.head
        previous = None
        index = 0

        # Pozisyona kadar listeyi dolaş
        while current is not None and index < position:
            previous = current
            current = current.next
            index += 1

        # Eğer pozisyon listenin dışındaysa
        if current is None:
            print("Position does not exist.")
            return

        # Silinecek düğüm ile bir önceki düğümün bağlantısını güncelle
        previous.next = current.next  # Bir önceki düğümün next pointer'ını güncelle
        current = None  # Silinecek düğümü serbest bırak


    # Listenin sonundaki d���m� silen fonksiyon
    def delete_last_node(self):
        if self.head is None:  # E�er liste bo�sa
            print("List is empty.")
            return

        # E�er listede yaln�zca bir d���m varsa
        if self.head.next is None:
            self.head = None  # Head'i None yaparak d���m� sil
            return

        # Birden fazla d���m varsa
        current = self.head
        previous = None

        # Listenin sonuna kadar git, son d���mden bir �nceki d���m� bul
        while current.next is not None:
            previous = current
            current = current.next

        # Son d���m� silme i�lemi: previous'un next pointer'�n� None yap
        previous.next = None
        current = None  # Son d���m� serbest b�rak

    # T�m ba�l� listeyi silen fonksiyon
    def delete_list(self):
        current = self.head

        while current:
            auxiliary_node = current.next  # Bir sonraki d���m� tut
            print(f"Deleting node with data: {current.data}")  # Silinen d���m� g�ster
            current = None  # Mevcut d���m� serbest b�rak (Python garbage collector otomatik olarak halleder)
            current = auxiliary_node  # Bir sonraki d���me ge�

        self.head = None  # T�m liste silindikten sonra head'i None yap

    # Listeyi yazd�rma i�lemi
    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)


# Kullan�m
llist = LinkedList()
llist.insert_end(10)
llist.insert_end(20)
llist.insert_end(30)
llist.insert_end(40)

print("List: ", llist)  # ��kt�: 10 -> 20 -> 30 -> 40

# Listenin uzunlu�u
print("List length: ", llist.list_length())  # ��kt�: 4

# Pozisyona eleman ekleme
llist.insert_at_position(2, 25)
print("25 has added to the list:", llist)  # ��kt�: 10 -> 20 -> 25 -> 30 -> 40

# Son d���m� silme
llist.delete_last_node()
print("Last Node has been deleted:", llist)  # ��kt�: 10 -> 20 -> 25 -> 30

# Belirli pozisyondaki d���m� silme
llist.delete_node_at_position(1)
print("The second node has been deleted:", llist)  # ��kt�: 10 -> 25 -> 30

# Belirli eleman� bulma
print("Does the list include 30 ? ",llist.find_element(30))

# T�m listeyi silme
llist.delete_list()
print("All node has been removed, list has been deleted:", llist)  # ��kt�: (bo� liste)
