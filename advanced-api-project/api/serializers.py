from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """Serializes a book."""
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Ensures publication year is not in the future."""
        if value > datetime.date.today().year:
            raise serializers.ValidationError('Publication year cannot be in the future.')
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """Serializes an author."""
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
