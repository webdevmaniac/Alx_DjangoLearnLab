Retrieve Operation

from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

Expected Output
The title, author, and publication year of the book
