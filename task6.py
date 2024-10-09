# Task 6: Create a program to manage a library system using classes, including methods for adding, removing, and displaying books.

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' by {book.author} removed from the library.")
                return
        print(f"No book found with ISBN: {isbn}")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(book)

# Example usage:
library = Library()

# Adding books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Displaying all books
library.display_books()

# Removing a book
library.remove_book("9780451524935")

# Displaying all books after removal
library.display_books()

# Attempting to remove a non-existent book
library.remove_book("1234567890")
