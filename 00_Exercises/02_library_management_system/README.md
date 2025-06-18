# 📚 Library Management System

A simple command-line Library Management System built in Python using `@dataclass`. Users can manage or interact with books as **Admin** or **Member**.

---

## 🚀 Features
- 👨‍💼 **Admin:**
  - Add Books
  - Remove Books
  - View Library Info
- 🙋 **Member:**
  - Read Books
  - Lend Books

---

## ⚙️ How It Works
1. Start the program and choose your role: `admin` or `member`.
2. Perform actions based on your role using simple text input.

---

## 🛠 Code Highlights
- `@dataclass` simplifies data handling.
- Uses `field(default_factory=...)` for safe list defaults.
- Custom methods for book operations (`add`, `remove`, etc.).
- `try/except` handles invalid input gracefully.
- Dynamic `no_of_books` updates on changes.

---

## 🔧 Key Concepts

- `default_factory` ensures each instance has its **own book list**.
- `__post_init__()` calculates the number of books **after object creation**.

## 🧩 Methods

- `add_books(book_name)` – Adds a new book to the library.
- `remove_books(book_name)` – Removes a book if it exists.
- `read_book(book_name)` – Allows reading a book if available.
- `lend_book(book_name, days)` – Lends a book for a set number of days.
- `library_info()` – Shows total books and their names.

Each method handles one task and prints a **user-friendly message**.


## 📌 Example
Do you want to start the program (yes or no): yes
Are you an admin of library or a member: admin
Do you want to add a book or remove a book from Library or view details(add,remove,info): add
Enter name of book you want to add in your library: Science
Science Book is added to your Library!

## ✅ Notes

- Book names are auto-capitalized.
- Input errors are caught with `try/except`.
- Instance-level book list avoids shared state.
- Beginner-friendly OOP example using `@dataclass`.

---

## 🏁 Summary

A neat project to practice **Python classes**, **methods**, **control flow**, and **user input** — great for learning core programming concepts!
