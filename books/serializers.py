from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.conf import settings
from .models import *


# class BookSerializers(serializers.Serializer):
#     name = serializers.CharField()
#
#
#     book = Book.objects.get(id=1)
#     book.name
#     book.author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Favorites
        fields = '__all__'


