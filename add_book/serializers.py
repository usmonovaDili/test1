from rest_framework import serializers
from .models import AuthorModel, GenerModel, BookModel


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = GenerModel
        fields = ('name',)


class BookSerialziers(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('name', 'image', 'price', 'pages', 'year', 'author', 'genre', 'desc')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('user', 'bio', 'date_of_birth', 'is_dead', 'date_of_dead', 'image', 'genre', 'country')
