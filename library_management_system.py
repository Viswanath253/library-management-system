import mysql.connector
from datetime import datetime

# connect to database
conn = mysql.connector.connect(
    host='localhost',
    user='Viswanath',     
    password='21121A0253@eee', 
    database='library_management'
)

cur = conn.cursor()

# Add new book
def add_book(title, author):
    sql = "INSERT INTO books (title, author) VALUES (%s, %s)"
    cur.execute(sql, (title, author))
    conn.commit()
    print("Book added!")

# Show only available books
def view_available():
    cur.execute("SELECT * FROM books WHERE available = TRUE")
    data = cur.fetchall()
    for row in data:
        print(f"{row[0]}. {row[1]} by {row[2]}")

# Checkout a book
def checkout(book_id, user):
    cur.execute("SELECT available FROM books WHERE book_id = %s", (book_id,))
    available = cur.fetchone()
    if available and available[0]:
        time = datetime.now()
        cur.execute("UPDATE books SET available = FALSE WHERE book_id = %s", (book_id,))
        cur.execute("INSERT INTO transactions (book_id, user, checkout_date, status) VALUES (%s, %s, %s, 'checked out')", (book_id, user, time))
        conn.commit()
        print("Book checked out.")
    else:
        print("Book not available.")

# Return a book
def return_book(book_id, user):
    cur.execute("SELECT * FROM transactions WHERE book_id = %s AND user = %s AND status = 'checked out'", (book_id, user))
    result = cur.fetchone()
    if result:
        time = datetime.now()
        cur.execute("UPDATE books SET available = TRUE WHERE book_id = %s", (book_id,))
        cur.execute("UPDATE transactions SET return_date = %s, status = 'returned' WHERE book_id = %s AND user = %s", (time, book_id, user))
        conn.commit()
        print("Book returned.")
    else:
        print("No record found for this return.")

# Show all books
def view_all():
    cur.execute("SELECT * FROM books")
    data = cur.fetchall()
    for row in data:
        status = "Available" if row[3] else "Checked Out"
        print(f"{row[0]}. {row[1]} by {row[2]} - {status}")

# Main program
def main():
    while True:
        print("\n--- Library System ---")
        print("1. Add Book")
        print("2. View Available Books")
        print("3. Checkout Book")
        print("4. Return Book")
        print("5. View All Books")
        print("6. Exit")
        
        ch = input("Enter your choice: ")
        
        if ch == '1':
            t = input("Enter title: ")
            a = input("Enter author: ")
            add_book(t, a)
        elif ch == '2':
            view_available()
        elif ch == '3':
            try:
                id = int(input("Book ID: "))
                u = input("Your name: ")
                checkout(id, u)
            except:
                print("Invalid input.")
        elif ch == '4':
            try:
                id = int(input("Book ID: "))
                u = input("Your name: ")
                return_book(id, u)
            except:
                print("Invalid input.")
        elif ch == '5':
            view_all()
        elif ch == '6':
            print("Exiting...")
            break
        else:
            print("Wrong choice.")

if __name__ == "__main__":
    main()
    conn.close()
