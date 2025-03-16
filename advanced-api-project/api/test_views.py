from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('testuser', 'testuser@example.com', 'password')
        self.client.force_authenticate(user=self.user)
        self.book1 = Book.objects.create(title='Book 1', author='Author 1', publication_year=2020)
        self.book2 = Book.objects.create(title='Book 2', author='Author 2', publication_year=2021)

    def test_get_all_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_by_id(self):
        response = self.client.get(reverse('book-detail', args=[self.book1.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book 1')

    def test_create_book(self):
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2022}
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2022}
        response = self.client.put(reverse('book-detail', args=[self.book1.pk]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book1.pk).title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', args=[self.book1.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        response = self.client.get(reverse('book-list'), {'title': 'Book 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author(self):
        response = self.client.get(reverse('book-list'), {'search': 'Author 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        response = self.client.get(reverse('book-list'), {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
