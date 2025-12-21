from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )

        # Create authenticated client
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        # Sample Books
        self.book1 = Book.objects.create(
            title="Django for Beginners", author="William", price=50
        )
        self.book2 = Book.objects.create(
            title="Python Tricks", author="Dan", price=30
        )

        # Endpoints
        self.list_url = reverse("book-list")      # GET, POST
        self.detail_url = lambda pk: reverse("book-detail", args=[pk])  # PUT, DELETE


    # -------------------------------
    # 1. TEST: LIST ALL BOOKS
    # -------------------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    # -------------------------------
    # 2. TEST: CREATE BOOK
    # -------------------------------
    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "John Doe",
            "price": 100
        }
        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")


    # -------------------------------
    # 3. TEST: RETRIEVE SINGLE BOOK
    # -------------------------------
    def test_retrieve_book(self):
        url = self.detail_url(self.book1.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)


    # -------------------------------
    # 4. TEST: UPDATE BOOK
    # -------------------------------
    def test_update_book(self):
        url = self.detail_url(self.book1.id)
        data = {"title": "Updated Title", "author": "William", "price": 70}

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")


    # -------------------------------
    # 5. TEST: DELETE BOOK
    # -------------------------------
    def test_delete_book(self):
        url = self.detail_url(self.book1.id)

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


    # -------------------------------
    # 6. PERMISSIONS: UNAUTHENTICATED USER CANNOT CREATE/UPDATE/DELETE
    # -------------------------------
    def test_unauthenticated_user_cannot_create(self):
        client = APIClient()  # not logged in
        data = {"title": "Unauthorized", "author": "X", "price": 20}

        response = client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_unauthenticated_user_cannot_update(self):
        client = APIClient()
        url = self.detail_url(self.book1.id)
        data = {"title": "Hack Update", "author": "X", "price": 20}

        response = client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_unauthenticated_user_cannot_delete(self):
        client = APIClient()
        url = self.detail_url(self.book1.id)

        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # -------------------------------
    # 7. TEST FILTERING
    # -------------------------------
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + "?author=William")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "William")


    # -------------------------------
    # 8. TEST SEARCH
    # -------------------------------
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django for Beginners")


    # -------------------------------
    # 9. TEST ORDERING
    # -------------------------------
    def test_order_books_by_price(self):
        response = self.client.get(self.list_url + "?ordering=price")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        prices = [book["price"] for book in response.data]
        self.assertEqual(prices, sorted(prices))
