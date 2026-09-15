import os

FILE_NAME = "books.txt"


def load_books():
    books = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 2:
                    books[data[0]] = data[1]
    return books


def save_books(books):
    with open(FILE_NAME, "w") as file:
        for book, status in books.items():
            file.write(f"{book},{status}\n")


def add_book(books):
    book = input("Enter Book Name: ")
    if book in books:
        print("Book already exists!")
    else:
        books[book] = "Available"
        save_books(books)
        print("Book added successfully.")


def view_books(books):
    if not books:
        print("No books available.")
        return

    print("\n===== BOOK LIST =====")
    for book, status in books.items():
        print(f"{book} --> {status}")


def search_book(books):
    book = input("Enter Book Name: ")
    if book in books:
        print(f"{book} --> {books[book]}")
    else:
        print("Book not found.")


def issue_book(books):
    book = input("Enter Book Name to Issue: ")
    if book in books:
        if books[book] == "Available":
            books[book] = "Issued"
            save_books(books)
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")


def return_book(books):
    book = input("Enter Book Name to Return: ")
    if book in books:
        if books[book] == "Issued":
            books[book] = "Available"
            save_books(books)
            print("Book returned successfully.")
        else:
            print("Book was not issued.")
    else:
        print("Book not found.")


def delete_book(books):
    book = input("Enter Book Name to Delete: ")
    if book in books:
        del books[book]
        save_books(books)
        print("Book deleted successfully.")
    else:
        print("Book not found.")


def main():
    books = load_books()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            view_books(books)

        elif choice == "3":
            search_book(books)

        elif choice == "4":
            issue_book(books)

        elif choice == "5":
            return_book(books)

        elif choice == "6":
            delete_book(books)

        elif choice == "7":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()