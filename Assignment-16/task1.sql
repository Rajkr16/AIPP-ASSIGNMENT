START TRANSACTION;

-- Books table
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    publisher VARCHAR(255),
    published_year SMALLINT CHECK (published_year > 0),
    total_copies INT NOT NULL DEFAULT 1 CHECK (total_copies >= 0),
    available_copies INT NOT NULL DEFAULT 1 CHECK (available_copies >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Members table
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(30),
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    membership_type VARCHAR(50) DEFAULT 'standard',
    is_active TINYINT(1) DEFAULT 1
);

-- Loans table
CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    due_date DATE NOT NULL,
    return_date DATE,
    status ENUM('ongoing', 'returned', 'overdue', 'lost') DEFAULT 'ongoing',
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- Indexes for optimization
CREATE INDEX idx_books_isbn ON books(isbn);
CREATE INDEX idx_members_email ON members(email);
CREATE INDEX idx_loans_book ON loans(book_id);
CREATE INDEX idx_loans_member ON loans(member_id);
CREATE INDEX idx_loans_due ON loans(due_date);

COMMIT;


--TASK-2
INSERT INTO books (isbn, title, author, publisher, published_year, total_copies, available_copies)
VALUES
('9780439064873', 'Harry Potter and the Chamber of Secrets', 'J.K. Rowling', 'Bloomsbury', 1998, 5, 5),
('9780747532743', 'Harry Potter and the Philosophers Stone', 'J.K. Rowling', 'Bloomsbury', 1997, 3, 3),
('9780316769488', 'The Catcher in the Rye', 'J.D. Salinger', 'Little, Brown and Company', 1951, 4, 4);

INSERT INTO members (first_name, last_name, email, phone, membership_type, is_active)
VALUES
('Raj', 'Kumar', 'rajkumar@example.com', '9876543210', 'standard', 1),
('Anita', 'Sharma', 'anita.sharma@example.com', '9876501234', 'premium', 1),
('Rohit', 'Verma', 'rohit.verma@example.com', '9898998899', 'standard', 1);

INSERT INTO loans (book_id, member_id, due_date, status)
VALUES
(1, 1, '2025-12-10', 'ongoing'),
(2, 2, '2025-12-08', 'ongoing'),
(3, 3, '2025-12-05', 'overdue');


SELECT * FROM books;
SELECT * FROM members;
SELECT * FROM loans;


--TASK 3
SELECT 
    l.loan_id,
    b.title,
    b.author,
    l.loan_date,
    l.due_date,
    l.status
FROM loans l
JOIN books b ON b.book_id = l.book_id
WHERE l.member_id = 1;   -- Replace 1 with the desired member ID

SELECT 
    l.loan_id,
    b.title,
    b.author,
    m.first_name,
    m.last_name,
    l.loan_date,
    l.due_date,
    l.status
FROM loans l
JOIN books b ON b.book_id = l.book_id
JOIN members m ON m.member_id = l.member_id
WHERE m.first_name = 'Raj' AND m.last_name = 'Kumar';


SELECT 
    m.first_name, m.last_name, b.title, l.due_date, l.status
FROM loans l
JOIN members m ON l.member_id = m.member_id
JOIN books b ON l.book_id = b.book_id;


--TASK-4

UPDATE books
SET available_copies = available_copies - 1
WHERE book_id = 1;   -- Replace 1 with specific book ID


UPDATE loans
SET return_date = CURRENT_DATE,
    status = 'returned'
WHERE loan_id = 1;  -- Replace loan ID


UPDATE books
SET available_copies = available_copies + 1
WHERE book_id = 1;  -- Same book ID as above

SELECT * FROM loans
WHERE member_id = 1 AND return_date IS NULL;


DELETE FROM members
WHERE member_id = 1;







