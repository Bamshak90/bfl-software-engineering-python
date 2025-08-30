import json

try:
    with open('system_library.json', 'r') as file:
        data = json.load(file)
        library = data["library"]
        system_library = data["borrowed_books"]
        #json.dump(system_library.json, file)

except FileNotFoundError:
    library = ["python for Beginners", "Data Structures in C", "AI Basics"]
    borrowed_books = {}

def save_data():
    data = {
        "library": library,
        "borrowed_books": borrowed_books
    }
    with open("system_library.json", "w") as file:
        json.dump(data, file, indent = 3)





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
        if user_choice == 7:
            print("Thank you for checking in")
            break
        call_function(user_choice)

def call_function(user_choice):
    if user_choice == 1:
        display_books()
    elif user_choice == 2:
        book_name = input("Enter book name to add: ")
        add_book(book_name)
    elif user_choice == 3:
        borrowing_id = int(input("Enter Student ID: "))
        book_name = input("Name of book to borrow: ")
        borrowed_book(borrowing_id, book_name)
    elif user_choice == 4:
        returning_id = int(input("Enter student ID: "))
        book_name = input("Book name to return: ")
        return_book(returning_id,book_name)
    elif user_choice == 5:
        list_borrowed_books()

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
        save_data()


def borrowed_book(student_id, book_name):
    #global student_id
    if book_name in library:
        library.remove(book_name)
        borrowed_books.setdefault(student_id, []).append(book_name)
        print(f"You have borrowed {book_name} with the ID:{student_id}")
        print(borrowed_books)
        save_data()
    else:
        print(f"{book_name} does not exist")

def return_book(student_id,book_name):
    #global student_id
    if student_id in borrowed_books and book_name in borrowed_books[student_id]:
        borrowed_books[student_id].remove(book_name)
        library.append(book_name)
        print(f"{book_name} has been returned by student {student_id}.")
        print(borrowed_books)
        save_data()
        
    else:
        print(f"You did not borrow {book_name}")

def list_borrowed_books():
    if borrowed_books:
        for student_id, books in borrowed_books.items():
            print(f"Student {student_id} borrowed: {books}")
    else:
        print("No borrowed books yet.")
  
        


start()
