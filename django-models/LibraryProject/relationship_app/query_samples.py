from django.db.models import Q
from .models import Book, Author, Library, Librarian

def query_books_by_author(author_name):
    """
    Retrieves books written by a specific author.

    Args:
        author_name (str): The name of the author.

    Returns:
        QuerySet: A queryset of books written by the author.
    """
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):
    """
    Retrieves books in a specific library.

    Args:
        library_name (str): The name of the library.

    Returns:
        QuerySet: A queryset of books in the library.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return None

def retrieve_librarian_for_library(library_name):
    """
    Retrieves the librarian for a specific library.

    Args:
        library_name (str): The name of the library.

    Returns:
        Librarian: The librarian for the library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return None

# Example usage:
author_books = query_books_by_author('John Doe')
print(author_books)

library_books = list_books_in_library('New York Public Library')
print(library_books)

librarian = retrieve_librarian_for_library('New York Public Library')
print(librarian)
