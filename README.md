# Library Management System

## Overview
The **Library Management System** is a Python-based application that allows users to manage books in a library efficiently. This system enables users to add new books, check them out, return them, and view all available books. It uses SQLite for data storage, providing a simple yet functional interface for managing library operations.

## Features
- **Add New Books**: Admins can add books with titles and authors to the library database.
- **View Available Books**: Users can view a list of all currently available books for checkout.
- **Checkout Books**: Users can check out books by entering the book ID, updating its status to "checked out."
- **Return Books**: Users can return books, updating their status to "returned."
- **View All Books**: A comprehensive view of all books in the library, displaying their availability status.

## Technologies Used
- **Python**: The primary programming language used for application logic.
- **SQLite**: Lightweight database for storing book and transaction data.
- **Datetime Module**: For handling dates and times related to checkouts and returns.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
