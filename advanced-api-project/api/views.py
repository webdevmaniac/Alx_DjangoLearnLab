from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated as IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly as IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

# Create your views here.
class BookListView(generics.ListAPIView):
    """Lists all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    """Retrieves a single book by ID."""
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthenticated]

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
