from django.test import TestCase
from rest_framework.test import APIClient
from book.models import Books
from rest_framework import status
from django.urls import reverse

class BookCreateTestCase(TestCase):
    def setUp(self) -> None:
        """
        Set up the test case by creating an instance of APIClient.
        """
        self.client = APIClient()

    def test_create_instance(self):
        """
        Test the creation of a book instance through the "create" API endpoint.
        """
        url = reverse("create")
        data = {"Title": "shivay", "Author": "rangnathan", "Publicationyear": 2014}
        response = self.client.post(url, data, format="json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class BookUpdateTestCase(TestCase):
    def setUp(self) -> None:
        """
        Set up the test case by creating an instance of APIClient and a book instance.
        """
        self.client = APIClient()
        self.book = Books.objects.create(Title="Book 1", Author="Author 1", Publicationyear=2021)

    def test_update_books(self):
        """
        Test updating a book instance through the "update" API endpoint.
        """
        url = reverse("update", args=[self.book.id])
        data = {"Title": "Updated Book", "Author": "Updated Author", "Publicationyear": 2022}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.Title, "Updated Book")
        self.assertEqual(self.book.Author, "Updated Author")
        self.assertEqual(self.book.Publicationyear, 2022)

class BookListTestCase(TestCase):
    def setUp(self) -> None:
        """
        Set up the test case by creating an instance of APIClient and multiple book instances.
        """
        self.client = APIClient()
        self.book1 = Books.objects.create(Title="Book 1", Author="Author 1", Publicationyear=2021)
        self.book2 = Books.objects.create(Title="Book 2", Author="Author 2", Publicationyear=2022)
        self.book3 = Books.objects.create(Title="Book 3", Author="Author 3", Publicationyear=2023)

    def test_list_books(self):
        """
        Test listing books through the "book-list" API endpoint.
        """
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Assuming there are 3 books in the database
        # You can also check specific attributes of the retrieved books
        self.assertEqual(response.data[0]["Title"], self.book1.Title)
        self.assertEqual(response.data[1]["Author"], self.book2.Author)
        self.assertEqual(response.data[2]["Publicationyear"], self.book3.Publicationyear)

class BookRetrieveTestCase(TestCase):
    def setUp(self):
        """
        Set up the test case by creating an instance of APIClient and a book instance.
        """
        self.client = APIClient()
        self.books = Books.objects.create(Title="Book 1", Author="Author 1", Publicationyear=2021)

    def test_retrieve_book(self):
        """
        Test retrieving a book instance through the "retrieve" API endpoint.
        """
        url = reverse("retrieve", args=[self.books.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verify the retrieved book's attributes
        self.assertEqual(response.data["Title"], self.books.Title)
        self.assertEqual(response.data["Author"], self.books.Author)
        self.assertEqual(response.data["Publicationyear"], self.books.Publicationyear)

class BookDestroyTestCase(TestCase):
    def setUp(self):
        """
        Set up the test case by creating an instance of APIClient and a book instance.
        """
        self.client = APIClient()
        self.books = Books.objects.create(Title="Book 1", Author="Author 1", Publicationyear=2021)

    def test_destroy_book(self):
        """
        Test deleting a book instance through the "destroy" API endpoint.
        """
        url = reverse("destroy", args=[self.books.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify that the book instance has been deleted from the database
        with self.assertRaises(Books.DoesNotExist):
            self.books.refresh_from_db()
