#from django.urls import path
#from . import views

#urlpatterns = [
#   path('books/', views.list_books, name='list_books'),
#   path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
#] 


from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', views.ListBooksView.as_view(), name='book_list'),
    path('library/<pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<pk>/', views.delete_book, name='delete_book'),
]


