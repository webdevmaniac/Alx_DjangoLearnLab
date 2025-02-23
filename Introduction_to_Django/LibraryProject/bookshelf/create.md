In the Django shell, execute the following command to create a new Book instance:

from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

Expected output:

# Successful creation of the book instance
