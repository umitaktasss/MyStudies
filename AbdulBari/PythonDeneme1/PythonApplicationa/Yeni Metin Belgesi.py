import sqlite3

# B�yle bir veri taban� yoksa olu�turup ba�lanacak
con = sqlite3.connect("Library.db")
cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS library (name TEXT, Author TEXT, Publisher TEXT, Page INT)")
    con.commit()

def add_Data():
    cursor.execute("INSERT INTO library VALUES ('Istanbul Hatirasi', 'Ahmet Umit', 'IS BANKASI', 561)")
    con.commit()

def add_InputData(name, author, publisher, page):
    cursor.execute("INSERT INTO library VALUES (?, ?, ?, ?)", (name, author, publisher, page))
    con.commit()
    

def get_Data():
    cursor.execute("Select * From library")
    liste= cursor.fetchall()
    for i in liste:
        print(i)
        

def get_Data2():
    cursor.execute("Select name, Author From library")
    liste=cursor.fetchall()
    for i in liste:
        print(i)

def get_Data3(Author):
    cursor.execute("Select name, Author From library where Author= ?", (Author,))
    liste=cursor.fetchall()
    for i in liste:
        print(i)        

# Tabloyu olu�turma
#create_table()

# Veritaban�na �nceden belirlenmi� veri ekleme
#add_Data()

# Kullan�c�dan veri al�p ekleme
#while True:
#  name = input("Name (* to exit): ")
#    if name == "*":  # E�er kullan�c� * tu�una basarsa d�ng�den ��k
#        break
    
#   author = input("Author: ")
#    publisher = input("Publisher: ")
#   page = int(input("Page: "))
    
    # Kullan�c�dan al�nan veriyi ekleme
#    add_InputData(name, author, publisher, page)
 
get_Data3("J.D. Salinger")
# Ba�lant�y� kapatma
con.close()
