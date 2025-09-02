"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = []

def add_book(book_id, title, author, **kwargs):
    """Add a new book into the library with flexible details."""
    for book in library:
        if book["id"] == book_id:
            return f"Book with ID {book_id} already exists!"

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }
    book.update(kwargs)  
    library.append(book)  

    return f"Book '{title}' added successfully!"


def search_books(*search_params):
    """Search for books by multiple keywords (title, author)."""
    results = []
    for book in library:
        for param in search_params:
            if (param.lower() in book["title"].lower()) or (param.lower() in book["author"].lower()):
                results.append(book)
                break 
    return results if results else "No books found!"


def borrow_book(book_id):
    """Borrow a book if available."""
    for book in library:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return f"You borrowed '{book['title']}'."
            else:
                return f"Book '{book['title']}' not available."
    return f"Book with ID {book_id} not found!"


def return_book(book_id):
    """Return a borrowed book."""
    for book in library:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                return f"You returned '{book['title']}'."
            else:
                return f"Book '{book['title']}' was not borrowed."
    return f"Book with ID {book_id} not found!"


print(add_book(1, "Python Basics", "Mark", year=2020, genre="Programming"))
print(add_book(2, "Data Science 101", "MP", year=2021))
print(add_book(3, "The Great Gatsby", "Dula", year=1925, genre="Novel"))

print(search_books("Python", "Mark"))
print(borrow_book(1))
print(borrow_book(1))
print(return_book(1))
print(return_book(1))


