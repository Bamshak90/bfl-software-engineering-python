library = ["python for Beginners", "Data Structures in C", "AI Basics"]
borrowed_books = {}
student_id = 1
def start():
    while True:
        print('''
        1. Display available books
        2. Add books
        3. Borrow books
        4. Return books
        5. Borrowed books
        6. Students that Borrowed books
        7. Exit
        ''')

        user_choice = int(input("Choose an option: "))
        call_function(user_choice)

def call_function(user_choice):
    if user_choice == 1:
        display_books()
    elif user_choice == 2:
        book_name = input("Enter book name to add: ")
        add_book(book_name)
    elif user_choice == 3:
        book_name = input("Name of book to borrow: ")
        borrowed_book(book_name)
    elif user_choice == 4:
        book_name = input("Book name to return: ")
        return_book(book_name)

def display_books():

    if len(library) != 0:
        for books in library:
            print(books)
    else:
        print("No books to available")

def add_book(book_name):
    if book_name in library:
        print("Book Already Exist")
    else:
        library.append(book_name)
        print(f"{book_name} successfully added.")


def borrowed_book(book_name):
    global student_id
    if book_name in library:
        library.remove(book_name)
        borrowed_books[student_id] = book_name
        student_id += 1
    else:
        print(f"{book_name} does not exist")

def return_book(book_name):
    global student_id
    if book_name in borrowed_books[student_id]:
        library.append(book_name)
        borrowed_books[student_id] = book_name
        student_id -= 1
    else:
        print(f"You did not borrow {book_name}")
  
        











start()
