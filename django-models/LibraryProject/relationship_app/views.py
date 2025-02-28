from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Library
from .models import Book, Author, Librarian
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required

class LibraryDetailView(LoginRequiredMixin, DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

@method_decorator(login_required, name='dispatch')
class ListBooksView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'

@login_required
@permission_required('relationship_app.can_view_books')
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

@login_required
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        # Add book logic here
        pass
    return render(request, 'relationship_app/add_book.html')

@login_required
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        # Edit book logic here
        pass
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@login_required
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        # Delete book logic here
        pass
    return render(request, 'relationship_app/delete_book.html', {'book': book})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def admin_view(request):
    return render(request, 'admin_view.html')

def librarian_view(request):
    return render(request, 'librarian_view.html')

def member_view(request):
    return render(request, 'member_view.html')

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

admin_view = user_passes_test(is_admin)(admin_view)
librarian_view = user_passes_test(is_librarian)(librarian_view)
member_view = user_passes_test(is_member)(member_view)

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
