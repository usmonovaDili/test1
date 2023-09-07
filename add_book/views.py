from django.shortcuts import render
from rest_framework import generics
from .models import AuthorModel, BookModel, GenerModel
from .serializers import GenreSerializers, AuthorSerializer, BookSerialziers
from config.permissions import AuthorPermission, AdminPermissions


class GenreListApiView(generics.ListCreateAPIView):
    queryset = GenerModel.objects.all()
    serializer_class = GenreSerializers
    permission_classes = (AdminPermissions,)


class BookListByAuthorAPIView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerialziers
    permission_classes = (AuthorPermission,)

    def get_queryset(self):
        user = self.request.user
        author = AuthorModel.objects.get(user=user)
        return BookModel.objects.filter(author=author.id)

    def filter_queryset(self, queryset):
        params = self.request.query_params
        name = params.get('name')
        genre = params.get('genre')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if genre:
            queryset = queryset.filter(genre__icontains=genre)

        return queryset

