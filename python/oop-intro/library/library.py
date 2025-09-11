'''
Store a collection of books (title, author, availability status).

Provide a method to add a book.

Provide a method to borrow a book (only if available).

Provide a method to return a book.

Provide a method to display all books with their status.
'''



class Library:
  def __init__(self):
    self.books = {}
  
  def add_book(self,title, author):
    if title in self.books:
      return "Book already exist"
    else:
      self.books[title] = {
        "author": author,
        "status": "Available",
        "borrower": None
      } 
      return f"'{title}' by {author} added successfully"
    
  def borrow_book(self, title, borrower):
    if title in self.books:
        if self.books[title]["status"] == "Available":
            self.books[title]["status"] = "Borrowed"
            self.books[title]["borrower"] = borrower
            return f"You have borrowed '{title}'"
        else:
            return f"'{title}' is not available"
    else:
        return f"'{title}' does not exist in the library"

  def return_book(self, title, borrower):
    if title in self.books:
        if self.books[title]["status"] == "Borrowed":
            borrower = self.books[title]["borrower"]
            self.books[title]["status"] = "Available"
            self.books[title]["borrower"] = None
            return f"'{title}' has been returned by {borrower}"
        else:
            return f"'{title}' was not borrowed"
    else:
        return f"'{title}' does not exist in the library"

  def display_books(self):
    for title, info in self.books.items():
        print(f"Title: {title}, Author: {info['author']}, Status: {info['status']}, Borrower: {info['borrower']}")





library = Library()
library.add_book("The Hobbit", "J.R.R. Tolkien")
library.add_book("1984", "George Orwell")

library.borrow_book("The Hobbit", "Mark") 
# library.return_book("The Hobbit", "Mark") 


library.display_books()
