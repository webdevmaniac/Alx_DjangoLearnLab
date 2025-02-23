from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book, Author, Library, Librarian

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
