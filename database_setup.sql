-- Create a new database
CREATE DATABASE library_management;

-- Use the created database
USE library_management;

-- Create the books table
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

-- Create the transactions table
CREATE TABLE transactions (
    trans_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    user VARCHAR(255) NOT NULL,
    checkout_date DATETIME,
    return_date DATETIME,
    status ENUM('checked out', 'returned'),
    FOREIGN KEY(book_id) REFERENCES books(book_id)
);
