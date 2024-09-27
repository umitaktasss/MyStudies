from Library import *


def main():
    library_instance = library()  # Library s�n�f�ndan bir nesne olu�turuyoruz
    print("""**************************************************
           Welcome to the Library.

Menu: 
1- View all books.  
2- Search for a book.
3- Add a book.
4- Delete a book.
5- Update a book.
6- Show book count.

To Exit Press '*'
************************************************** """)



    while True:
        choice = input("Please select an option: ")
        
        if choice == '1':
            # T�m kitaplar� listele
            library_instance.list_books()
        
        elif choice == '2':
            # Kitap ara
            target_name = input("Enter the name of the book to search: ")
            found_book = library_instance.binary_search_books(target_name)
            time.sleep(0.3)
            if found_book:
                print(found_book)
            else:
                print("Book not found.")
        
        elif choice == '3':
            # Kitap ekle
            book_name = input("Enter book name: ")
            author = input("Enter author name: ")
            publication_year = input("Enter publication year: ")
            isbn = input("Enter ISBN: ")
            
            new_book = book(book_name, author, int(publication_year), int(isbn))
            library_instance.add_book(new_book)
            time.sleep(0.3)
            print("Book added successfully.")
        
        elif choice == '4':
            # Kitap sil
            isbn = input("Enter ISBN of the book to delete: ")
            library_instance.cursor.execute('DELETE FROM Books WHERE ISBN = ?', (isbn,))
            library_instance.con.commit()
            time.sleep(0.3)
            print("Book deleted successfully.")
        
        elif choice == '5':
            # Kitap g�ncelle
            isbn = input("Enter ISBN of the book to update: ")
            new_book_name = input("Enter new book name (leave blank if no change): ")
            new_author = input("Enter new author name (leave blank if no change): ")
            new_publication_year = input("Enter new publication year (leave blank if no change): ")
            
            library_instance.update_book(isbn, 
                                         new_book_name if new_book_name else None, 
                                         new_author if new_author else None, 
                                         int(new_publication_year) if new_publication_year else None)
            time.sleep(1)
            print("Book updated successfully.")
        
        elif choice == '6':
            # Kitap say�s�n� g�ster
            count = library_instance.count_books()
            time.sleep(0.3)
            print(f"Total number of books: {count}")
        

        elif choice == '7':
            # Loglar� g�ster
            library_instance.view_logs()
            time.sleep(0.3)



        elif choice == '*':
            print("Exiting the Library system. Goodbye!")
            time.sleep(0.3)
            library_instance.end_connection()  # Ba�lant�y� kapat
            break
        


        else:
            time.sleep(0.3)
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()




