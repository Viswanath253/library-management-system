-- Create database
CREATE DATABASE library_management;
USE library_management;

-- Table for books
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    available BOOLEAN DEFAULT TRUE
);

-- Table for transactions
CREATE TABLE transactions (
    trans_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    user VARCHAR(100),
    checkout_date DATETIME,
    return_date DATETIME,
    status ENUM('checked out', 'returned'),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
