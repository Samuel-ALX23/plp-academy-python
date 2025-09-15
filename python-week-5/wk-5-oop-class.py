# This script defines two classes, Book and Ebook, to fulfill the assignment requirements.

# --- 1. The Parent Class: Book ---
class Book:
    """
    A class to represent a physical book.
    """

    def __init__(self, title, author, publication_year, pages):
        """
        The constructor method, used to initialize a new Book object.
        """
        # Attributes are created and assigned within the constructor.
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.pages = pages
        # A simple flag to check if the book has been read.
        self.is_read = False

    def get_info(self):
        """
        A method to return a formatted string with the book's details.
        """
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Published: {self.publication_year}\n"
            f"Pages: {self.pages}"
        )

    def is_long_book(self):
        """
        A method to check if the book is considered long (more than 400 pages).
        """
        if self.pages > 400:
            return "This is a long book."
        else:
            return "This is a standard book."
        
    def mark_as_read(self):
        """
        A method to update the status of the book.
        """
        self.is_read = True
        print(f"'{self.title}' has been marked as read.")

# --- 2. The Child Class: Ebook (Inheritance and Polymorphism) ---
class Ebook(Book):
    """
    A class representing an Ebook, which inherits from the Book class.
    """

    def __init__(self, title, author, publication_year, pages, file_size_mb):
        """
        The constructor for the Ebook class.
        """
        # Use super() to call the constructor of the parent class (Book).
        super().__init__(title, author, publication_year, pages)
        # Add a new attribute unique to the Ebook class.
        self.file_size_mb = file_size_mb

    def get_info(self):
        """
        This method overrides the get_info() method in the parent Book class.
        """
        # Get the information from the parent class's get_info() method.
        parent_info = super().get_info()
        # Add the ebook-specific information.
        return f"{parent_info}\nFile Size: {self.file_size_mb} MB"

# --- Main Execution Block ---
# This block runs when the script is executed.
if __name__ == "__main__":
    # Create an instance (object) of the Book class.
    # We pass the required values to the constructor.
    book1 = Book("Python Crash Course", "Eric Matthes", 2019, 544)
    print("--- Book Object Details ---")
    print(book1.get_info())
    print(book1.is_long_book())
    book1.mark_as_read()
    print("-" * 25)

    # Create an instance of the Ebook class, which also requires file_size_mb.
    ebook1 = Ebook("Python for Data Analysis", "Wes McKinney", 2017, 500, 25)
    print("\n--- Ebook Object Details (Inheritance & Polymorphism) ---")
    # This calls the overridden get_info() method from the Ebook class.
    print(ebook1.get_info())
    ebook1.mark_as_read()
