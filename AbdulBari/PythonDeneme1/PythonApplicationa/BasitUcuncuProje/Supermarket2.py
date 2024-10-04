from Supermarket import Goods, Supermarket
import time
def main():
    supermarket = Supermarket()

    print("""
    **************************************************
    Welcome to the Supermarket Management Program.

    Operations:
    1- Show All Goods
    2- Search for a Good
    3- Add a Good
    4- Delete a Good
    5- Update a Good
    6- Calculate Total Inventory Value
    7- Show Goods by Category
    Press '*' to exit.
    **************************************************
    """)

    while True:
        operation = input("Select an operation: ")

        if operation == '*':
            print("Exiting the program...")
            supermarket.cut_connection()  # Close the database connection
            break
        
        elif operation == '1':
            supermarket.show_all_goods()

        elif operation == '2':
            product_name = input("Enter the product name you want to search for: ")
            print("Searching for the product...")
            time.sleep(2)
            supermarket.show_good(product_name)

        elif operation == '3':
            product_name = input("Product Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            category = input("Category (e.g., Bakery, Fruits, Fast Food): ")
            expiry_date = input("Expiry Date (YYYY-MM-DD): ")
            calories = input("Calories (if applicable, else leave blank): ")
            calories = int(calories) if calories else None
            is_frozen = input("Is the product frozen? (Yes/No): ").lower() == 'yes'

            new_good = Goods(product_name, price, quantity, category, expiry_date, calories, is_frozen)

            print("Adding the product...")
            time.sleep(2)
            supermarket.add_good(new_good)

        elif operation == '4':
            product_name = input("Enter the product name you want to delete: ")
            confirm = input(f"Are you sure you want to delete '{product_name}'? (Y/N): ")
            if confirm.upper() == 'Y':
                print("Deleting the product...")
                time.sleep(2)
                supermarket.delete_good(product_name)
            elif confirm.upper() == 'N':
                print("Deletion canceled.")
            else:
                print("Invalid input!")

        elif operation == '5':
            product_name = input("Which product would you like to update? ")

            print("""
            What would you like to update?
            1- Price
            2- Quantity
            3- Expiry Date
            """)
            update_choice = input("Select the number of the field to update: ")

            if update_choice == '1':
                new_price = float(input("Enter the new price: "))
                print("Updating price...")
                time.sleep(2)
                supermarket.update_good(product_name, new_price=new_price)

            elif update_choice == '2':
                new_quantity = int(input("Enter the new quantity: "))
                print("Updating quantity...")
                time.sleep(2)
                supermarket.update_good(product_name, new_quantity=new_quantity)

            elif update_choice == '3':
                new_expiry_date = input("Enter the new expiry date (YYYY-MM-DD): ")
                print("Updating expiry date...")
                time.sleep(2)
                supermarket.update_good(product_name, new_expiry_date=new_expiry_date)

            else:
                print("Invalid choice! Please select a valid option.")

        elif operation == '6':
            print("Calculating total inventory value...")
            time.sleep(2)
            supermarket.calculate_total_value()

        elif operation == '7':  # New option for showing goods by category
            category = input("Enter the category to search for: ")
            supermarket.show_goods_by_category(category)
        else:
            print("Invalid operation! Please try again.")

if __name__ == "__main__":
    main()
