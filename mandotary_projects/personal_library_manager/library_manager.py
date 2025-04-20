import os
import json

class BooksCollection():
    """A class to manage a personal library, including adding, deleting, searching, and tracking reading progress."""

    def __init__(self):
        """Initialize the book collection, set the path to the data file, and load existing data."""
        self.book_list = []
        self.storage_file = os.path.join(os.path.dirname(__file__), "books_data.json")
        self.load_file()

    def load_file(self):
        """Load books from the JSON file into the book list. Start with an empty list if the file is missing or corrupt."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_file(self):
        """Save the current book list to the JSON file."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)
    
    def create_new_book(self):
        """Prompt user to enter new book details and add the book to the collection."""
        book_title = input("Enter book title: ")
        book_author = input("Enter author name: ")
        try:
            book_published_year = int(input("Enter published year: "))
        except ValueError:
            print("Enter valid year: ")
            return  # Return early if the year is not valid

        book_genre = input("Enter book genre: ")
        book_read_status = input("Have you read this book? (yes or no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "published_year": book_published_year,
            "genre": book_genre,
            "read_status": book_read_status
        }

        self.book_list.append(new_book)
        self.save_file()
        print("Book added successfully.\n")

    def delete_book(self):
        """Remove a book from the collection by title."""
        book_title = input("Enter book title to remove it: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_file()
                print("Book successfully removed.\n")
                return
        print("Book not found.\n")

    def find_book(self):
        """Search for books by title or author."""
        search_type = input("1. Title\n2. Author\nChoose your type: ")
        search_term = input("Enter search term: ").lower()

        # Filter books that match the search term in either title or author
        found_book = [
            book for book in self.book_list
            if search_term in book["title"].lower() or search_term in book["author"].lower()
        ]

        if found_book:
            for index, book in enumerate(found_book, 1):
                read_status = "Read" if book["read_status"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} - {book['genre']} - {read_status}\n")
        else:
            print("No matching books found.\n")

    def display_all_books(self):
        """Display all books in the collection with details."""
        if not self.book_list:
            print("Your collection of books is empty.")
            return

        for index, book in enumerate(self.book_list, 1):
            read_status = "Read" if book["read_status"] else "Unread"
            print(f"{index}. {book['title']} by {book['author']} - {book['genre']} - {read_status}\n")
        print()

    def show_reading_progress(self):
        """Display the total number of books and the percentage of books read."""
        total_books = len(self.book_list)

        if total_books == 0:
            print("No books in your collection yet.")
            return

        # Count how many books have been read using a generator expression
        read_books = sum(1 for book in self.book_list if book["read_status"])
        percentage_read = (read_books / total_books) * 100

        print(f"📚 Total Books: {total_books}")
        print(f"✅ Books Read: {read_books}")
        print(f"📊 Reading Progress: {percentage_read:.2f}%\n")

    def start_application(self):
        """Run the interactive menu-driven application for managing the book collection."""
        while True:
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. View all books")
            print("5. View reading progress")
            print("6. Exit")
            user_choice = input("Please choose an option (1-6): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.display_all_books()
            elif user_choice == "5":
                self.show_reading_progress()
            elif user_choice == "6":
                self.save_file()
                print("Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    # Run the application
    book_manager = BooksCollection()
    book_manager.start_application()