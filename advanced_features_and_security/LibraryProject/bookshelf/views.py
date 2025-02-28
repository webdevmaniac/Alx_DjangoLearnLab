from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('bookshelf.can_create_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Create book logic here
        pass
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        # Edit book logic here
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        # Delete book logic here
        pass
    return render(request, 'delete_book.html', {'book': book})
