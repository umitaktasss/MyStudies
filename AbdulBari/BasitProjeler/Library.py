import sqlite3
import logging
import time
class book():
    def __init__(self,book_name,author, publication_year, isbn):
        self.book_name=book_name
        self.author=author
        self.publication_year=publication_year
        self.isbn=isbn
        
    def __str__(self):
        return f"""Book name: {self.book_name}\nAuthor: {self.author}\nPublication year: {self.publication_year}\nISBN: {self.isbn}"""
    


class library():
    def __init__(self):
        self.create_connection()
        
    def create_connection(self):
        self.con = sqlite3.connect("library.db")
        self.cursor = self.con.cursor()
        
        table = '''
        CREATE TABLE IF NOT EXISTS Books (
            Book_Name TEXT,
            Author TEXT,
            Publication_Year INTEGER,
            ISBN INTEGER PRIMARY KEY
        )
        '''
        self.cursor.execute(table)
        self.con.commit()
        
    def end_connection(self):
        self.con.close()
        
    def fetch_all_books(self):
        self.cursor.execute("SELECT * FROM Books ORDER BY Book_Name ASC")
        books=self.cursor.fetchall()
        return [book(book_name=row[0], author=row[1], publication_year=row[2], isbn=row[3]) for row in books]
    #Binary Search Kullan�ld�!
    def binary_search_books(self, target_name):
        books = self.fetch_all_books()
        left,right =0, len(books)-1
        while left<=right:
            mid=(left+right)//2
            mid_book=books[mid].book_name.lower()
            target_name = target_name.lower()
            
            if mid_book == target_name:
                return books[mid]
            
            elif mid_book < target_name:
                left = mid+1
            else:
                right = mid-1
                
        return None
    def list_books(self, order_by="Book_Name"):
        self.cursor.execute(f"SELECT * FROM Books ORDER BY {order_by} ASC")
        books = self.cursor.fetchall()
        if not books:  # E�er kitap listesi bo�sa
            print("Library is empty.")
        else:
            for row in books:
                print("**************************************************")
                print(f"Book Name: {row[0]}\nAuthor: {row[1]}\nPublication Year: {row[2]}\nISBN: {row[3]}")
    
    def count_books(self):
        self.cursor.execute("SELECT COUNT(*) FROM Books")
        count = self.cursor.fetchone()[0]
        return count

    
    def update_book(self, isbn, new_book_name=None, new_author=None, new_publication_year=None):
        if new_book_name:
            self.cursor.execute('UPDATE Books SET Book_Name = ? WHERE ISBN = ?', (new_book_name, isbn))
        if new_author:
            self.cursor.execute('UPDATE Books SET Author = ? WHERE ISBN = ?', (new_author, isbn))
        if new_publication_year:
            self.cursor.execute('UPDATE Books SET Publication_Year = ? WHERE ISBN = ?', (new_publication_year, isbn))
        self.con.commit()
        
    def add_book(self, book):
        self.cursor.execute('''
            INSERT INTO Books (Book_Name, Author, Publication_Year, ISBN) 
            VALUES (?, ?, ?, ?)
        ''', (book.book_name, book.author, book.publication_year, book.isbn))
        self.con.commit()
    def setup_logging(self, log_file="library.log"):
        logging.basicConfig(filename=log_file, level=logging.INFO)
    
    def log_action(self, action):
        logging.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {action}")    
    
    def view_logs(self, log_file="library.log"):
        try:
            with open(log_file, "r") as file:
                logs = file.readlines()
                if logs:
                    print("Library Logs:")
                    for log in logs:
                        print(log.strip())
                else:
                    print("No logs available.")
        except FileNotFoundError:
            print("Log file not found.")