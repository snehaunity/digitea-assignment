from django.shortcuts import render
from book.models import Books
from book.serializers import BookSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)

class BookListApiView(ListAPIView):
    """View to retrieve a list of books."""

    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookCreateApiView(CreateAPIView):
    """View to create a new book."""

    serializer_class = BookSerializer

class BookUpdateView(UpdateAPIView):
    """View to update an existing book."""

    serializer_class = BookSerializer

    def get_queryset(self):
        """Return the queryset of all books."""
        return Books.objects.all()

class BookRetrieveView(RetrieveAPIView):
    """View to retrieve a specific book."""

    serializer_class = BookSerializer

    def get_queryset(self):
        """Return the queryset of all books."""
        return Books.objects.all()

class BookDestroyView(DestroyAPIView):
    """View to delete a specific book."""

    queryset = Books.objects.all()
    serializer_class = BookSerializer
