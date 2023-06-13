from rest_framework import serializers
from book.models import Books

class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Books model."""

    class Meta:
        model = Books
        fields = ['id', 'Title', 'Author', 'Publicationyear']
