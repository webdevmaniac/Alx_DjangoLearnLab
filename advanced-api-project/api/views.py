from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class BookListView(generics.ListAPIView):
    """Lists all books."""
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(generics.RetrieveAPIView):
    """Retrieves a single book by ID."""
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Book.objects.all()

class BookCreateView(generics.CreateAPIView):
    """Creates a new book."""
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Saves the new book instance."""
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """Updates an existing book."""
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.all()

    def perform_update(self, serializer):
        """Saves the updated book instance."""
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """Deletes a book."""
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.all()
