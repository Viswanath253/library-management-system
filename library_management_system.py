import mysql.connector
from datetime import datetime

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',   # Replace with your MySQL username
    password='your_password',  # Replace with your MySQL password
    database='library_management'
)
cursor = conn.cursor()

# Function to add a new book to the library
def add_book(title, author):
    cursor.execute('INSERT INTO books (title, author) VALUES (%s, %s)', (title, author))
    conn.commit()
    print(f"Book '{title}' by {author} added to the library.")

# Function to view all available books
def view_available_books():
    cursor.execute('SELECT * FROM books WHERE available = TRUE')
    books = cursor.fetchall()
    print("Available books:")
    for book in books:
        print(f"{book[0]} - {book[1]} by {book[2]}")

# Function to check out a book
def checkout_book(book_id, user):
    cursor.execute('SELECT available FROM books WHERE book_id = %s', (book_id,))
    book = cursor.fetchone()
    
    if book and book[0]:  # Check if the book is available
        checkout_date = datetime.now()
        cursor.execute('UPDATE books SET available = FALSE WHERE book_id = %s', (book_id,))
        cursor.execute('INSERT INTO transactions (book_id, user, checkout_date, status) VALUES (%s, %s, %s, %s)', 
                       (book_id, user, checkout_date, 'checked out'))
        conn.commit()
        print(f"Book {book_id} has been checked out by {user}.")
    else:
        print("Book is not available for checkout.")

# Function to return a book
def return_book(book_id, user):
    cursor.execute('SELECT * FROM transactions WHERE book_id = %s AND user = %s AND status = "checked out"', (book_id, user))
    transaction = cursor.fetchone()
    
    if transaction:
        return_date = datetime.now()
        cursor.execute('UPDATE books SET available = TRUE WHERE book_id = %s', (book_id,))
        cursor.execute('UPDATE transactions SET return_date = %s, status = "returned" WHERE book_id = %s AND user = %s',
                       (return_date, book_id, user))
        conn.commit()
        print(f"Book {book_id} returned by {user}.")
    else:
        print(f"No checkout record found for book {book_id} and user {user}.")

# Function to view all books and their status
def view_all_books():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    
    print("All books in the library:")
    for book in books:
        status = "Available" if book[3] else "Checked Out"
        print(f"{book[0]} - {book[1]} by {book[2]} - {status}")

# Example Usage
def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add a new book")
        print("2. View available books")
        print("3. Check out a book")
        print("4. Return a book")
        print("5. View all books")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            add_book(title, author)
        elif choice == '2':
            view_available_books()
        elif choice == '3':
            book_id = int(input("Enter book ID to check out: "))
            user = input("Enter your name: ")
            checkout_book(book_id, user)
        elif choice == '4':
            book_id = int(input("Enter book ID to return: "))
            user = input("Enter your name: ")
            return_book(book_id, user)
        elif choice == '5':
            view_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
