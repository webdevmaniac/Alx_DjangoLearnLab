from django.urls import path, include
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

books_patterns = [
    path('', BookListView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
    path('create/', BookCreateView.as_view()),
    path('<int:pk>/update/', BookUpdateView.as_view()),
    path('<int:pk>/delete/', BookDeleteView.as_view()),
]

urlpatterns = [
    path('books/', include(books_patterns)),
]
