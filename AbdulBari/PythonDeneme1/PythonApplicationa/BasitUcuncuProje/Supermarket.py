import sqlite3
import time

class Goods:
    def __init__(self, product_name, price, quantity, category, expiry_date, calories=None, is_frozen=None):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.expiry_date = expiry_date
        self.calories = calories
        self.is_frozen = is_frozen

    def __str__(self):
        return ("Product: {}\nPrice: {}\nQuantity: {}\nCategory: {}\nExpiry Date: {}\n"
                "Calories: {}\nFrozen: {}").format(
            self.product_name, self.price, self.quantity, self.category,
            self.expiry_date, self.calories if self.calories else "N/A", 
            "Yes" if self.is_frozen else "No")

class Supermarket:
    def __init__(self):
        self.make_connection()

    def make_connection(self):
        self.connection = sqlite3.connect(r"C:\Users\Tulpar\Desktop\Algorithm\AbdulBari\AbdulBari\PythonDeneme1\PythonApplicationa\supermarket.db")

        self.cursor = self.connection.cursor()

        # Create the Goods table if it doesn't exist
        ask = """CREATE TABLE IF NOT EXISTS Goods (
                    Product TEXT, 
                    Price REAL, 
                    Quantity INTEGER, 
                    Category TEXT, 
                    Expiry_Date TEXT, 
                    Calories INTEGER, 
                    Is_Frozen BOOLEAN
                )"""
        self.cursor.execute(ask)
        self.connection.commit()

    def cut_connection(self):
        self.connection.close()

    def add_good(self, good):
        ask = """INSERT INTO Goods 
                (Product, Price, Quantity, Category, Expiry_Date, Calories, Is_Frozen) 
                VALUES (?, ?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(ask, (
            good.product_name, 
            good.price, 
            good.quantity, 
            good.category, 
            good.expiry_date, 
            good.calories, 
            good.is_frozen
        ))
        self.connection.commit()
        print(f"Good '{good.product_name}' has been added to the database.")

    def delete_good(self, product_name):
        ask = "SELECT * FROM Goods WHERE Product = ?"
        self.cursor.execute(ask, (product_name,))
        good = self.cursor.fetchone()

        if good:
            ask = "DELETE FROM Goods WHERE Product = ?"
            self.cursor.execute(ask, (product_name,))
            self.connection.commit()
            print(f"Good '{product_name}' has been deleted.")
        else:
            print(f"Warning: Good '{product_name}' does not exist in the database.")

    def update_good(self, product_name, new_price=None, new_quantity=None, new_expiry_date=None):
        ask = "SELECT * FROM Goods WHERE Product = ?"
        self.cursor.execute(ask, (product_name,))
        good = self.cursor.fetchone()

        if good:
            if new_price:
                ask = "UPDATE Goods SET Price = ? WHERE Product = ?"
                self.cursor.execute(ask, (new_price, product_name))
            if new_quantity:
                ask = "UPDATE Goods SET Quantity = ? WHERE Product = ?"
                self.cursor.execute(ask, (new_quantity, product_name))
            if new_expiry_date:
                ask = "UPDATE Goods SET Expiry_Date = ? WHERE Product = ?"
                self.cursor.execute(ask, (new_expiry_date, product_name))

            self.connection.commit()
            print(f"Good '{product_name}' has been updated.")
        else:
            print(f"Warning: Good '{product_name}' does not exist in the database.")

    def show_all_goods(self):
        ask = "SELECT * FROM Goods"
        self.cursor.execute(ask)
        goods = self.cursor.fetchall()

        if len(goods) == 0:
            print("The list is empty...")
        else:
            for good in goods:
                product = Goods(good[0], good[1], good[2], good[3], good[4], good[5], good[6])
                print("*************************************************************")
                print(product)

    def show_good(self, product_name):
        ask = "SELECT * FROM Goods WHERE Product = ?"
        self.cursor.execute(ask, (product_name,))
        good = self.cursor.fetchone()

        if good:
            found_good = Goods(good[0], good[1], good[2], good[3], good[4], good[5], good[6])
            print(found_good)
        else:
            print(f"Warning: Good '{product_name}' does not exist in the database.")

    def calculate_total_value(self):
        ask = "SELECT SUM(Price * Quantity) FROM Goods"
        self.cursor.execute(ask)
        total_value = self.cursor.fetchone()[0]

        if total_value:
            print(f"Total value of all goods: ${total_value:.2f}")
        else:
            print("No goods in the database to calculate total value.")

    def show_goods_by_category(self, category):
        """Show all goods belonging to a specific category"""
        ask = "SELECT * FROM Goods WHERE Category = ?"
        self.cursor.execute(ask, (category,))
        goods = self.cursor.fetchall()

        if len(goods) == 0:
            print(f"No goods found in the '{category}' category.")
        else:
            print("*************************************************************")
            print(f"Goods in the '{category}' category:")
            for good in goods:
                product = Goods(good[0], good[1], good[2], good[3], good[4], good[5], good[6])
                print(product)
            print("*************************************************************")
