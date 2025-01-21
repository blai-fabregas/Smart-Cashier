import cv2
from pyzbar.pyzbar import decode
import sqlite3
import pandas as pd

# Initialize SQLite database connection
def initialize_database():
    conn = sqlite3.connect('shopping_assistant.db')
    cursor = conn.cursor()

    # Create a table to store items and prices
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                        barcode TEXT PRIMARY KEY,
                        name TEXT,
                        price REAL,
                        stock INTEGER)''')

    conn.commit()
    conn.close()

# Fetch item details from the database
def get_item_details(barcode):
    conn = sqlite3.connect('shopping_assistant.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, price, stock FROM items WHERE barcode = ?', (barcode,))
    item = cursor.fetchone()
    conn.close()
    return item

# Update stock in the database
def update_stock(barcode, quantity):
    conn = sqlite3.connect('shopping_assistant.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE items SET stock = stock - ? WHERE barcode = ? AND stock >= ?', (quantity, barcode, quantity))
    conn.commit()
    conn.close()

# Remove item from database and Excel file
def remove_item(barcode, file_path):
    try:
        # Remove from the database
        conn = sqlite3.connect('shopping_assistant.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items WHERE barcode = ?', (barcode,))
        conn.commit()
        conn.close()

        # Read Excel file and ensure Barcode is treated as a string
        data = pd.read_excel(file_path, dtype={'Barcode': str})
        barcode_str = str(barcode)  # Ensure the scanned barcode is a string

        # Filter out the item with the scanned barcode
        data = data[data['Barcode'] != barcode_str]
        data.to_excel(file_path, index=False)

        print(f"Item with barcode {barcode} removed from the database and Excel file.")
    except PermissionError:
        print(f"Permission denied: Unable to write to the file '{file_path}'. Ensure it is not open in another program.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Admin function to update item details or add a new item
def add_or_update_item(barcode, file_path):
    # Check if the barcode exists in the database
    item = get_item_details(barcode)
    if item:
        # Item exists, display current details
        name, price, stock = item
        print(f"Current details for {name}:")
        print(f"Price: ${price}, Stock: {stock}")
        
        # Ask if the admin wants to remove the item
        remove_item_choice = input("Do you want to remove this item from the database and Excel file? (y/n): ").strip().lower()
        if remove_item_choice == 'y':
            remove_item(barcode, file_path)
    else:
        print(f"New barcode scanned: {barcode}")
        # Allow admin to enter details for a new item
        new_name = input("Enter name for this item: ").strip()
        new_price = float(input("Enter price for this item: ").strip())
        new_stock = int(input("Enter stock quantity for this item: ").strip())
        
        # Insert new item into the SQLite database
        conn = sqlite3.connect('shopping_assistant.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO items (barcode, name, price, stock) VALUES (?, ?, ?, ?)''',
                       (barcode, new_name, new_price, new_stock))
        conn.commit()
        conn.close()

        # Also, add the new item to the Excel file
        data = pd.read_excel(file_path)

        # Create a new DataFrame with the new row
        new_item_df = pd.DataFrame([{'Barcode': barcode, 'Name': new_name, 'Price': new_price, 'Stock': new_stock}])
        
        # Concatenate the new item to the existing data
        data = pd.concat([data, new_item_df], ignore_index=True)

        # Save the updated data to the Excel file
        data.to_excel(file_path, index=False)

        print("New item added to the database and Excel file.")

# Admin interface to allow barcode scanning and updating or adding items
def admin_interface():
    print("Admin Interface: Choose an option.")
    print("1. Remove items from database and Excel")
    print("2. Scan item to update or add")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        file_path = input("Enter the path to the Excel file to remove items: ").strip()
        print("Scan the barcode of the item to remove.")
        
        # Open the camera for barcode scanning
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to access the camera.")
                break
            
            # Decode barcodes in the frame
            barcodes = decode(frame)
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                print(f"Scanned barcode: {barcode_data}")

                # Remove the item from the database and Excel file
                remove_item(barcode_data, file_path)

            # Display the video feed
            cv2.imshow('Barcode Scanner', frame)

            # Quit the application when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    elif choice == '2':
        file_path = input("Enter the path to the Excel file: ").strip()
        print("Scan the barcode of the item to update or add.")
        
        # Open the camera for barcode scanning
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to access the camera.")
                break
            
            # Decode barcodes in the frame
            barcodes = decode(frame)
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                print(f"Scanned barcode: {barcode_data}")

                # Update item details or add a new item
                add_or_update_item(barcode_data, file_path)

            # Display the video feed
            cv2.imshow('Barcode Scanner', frame)

            # Quit the application when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

# Customer interface to scan items and add to cart or skip
def customer_interface():
    print("Welcome to the Smart Shopping Assistant!")
    print("Scan items to add them to your cart. Press 'q' to quit.")

    total_cost = 0.0
    cart = []  # Track items added to the cart
    skipped_items = []  # Track skipped items

    # Open the camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to access the camera.")
            break

        # Decode barcodes in the frame
        barcodes = decode(frame)
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            item = get_item_details(barcode_data)

            if item:
                name, price, stock = item
                print(f"Scanned: {name} - ${price:.2f} (Stock: {stock})")

                if stock > 0:
                    # Ask the customer if they want to add it to the cart
                    add_to_cart = input(f"Add {name} to your cart? (y/n): ").strip().lower()
                    if add_to_cart == 'y':
                        cart.append((name, price))
                        total_cost += price
                        update_stock(barcode_data, 1)
                        print(f"Added to cart. Current total: ${total_cost:.2f}")
                    else:
                        skipped_items.append(name)  # Track skipped item
                        print("Item skipped.")
                else:
                    print("Item out of stock.")
            else:
                print("Item not found in the database.")

        # Display the video feed
        cv2.imshow('Barcode Scanner', frame)

        # Quit the application when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Display the final cart summary
    print("\nFinal Cart Summary:")
    for name, price in cart:
        print(f"- {name}: ${price:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

    # Display skipped items
    if skipped_items:
        print("\nItems Not Bought:")
        for item in skipped_items:
            print(f"- {item}")

# Main menu to choose between customer and admin interface
def main():
    while True:
        print("\n1. Customer Interface")
        print("2. Admin Interface")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            customer_interface()
        elif choice == '2':
            admin_interface()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    initialize_database()
    main()
