from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
