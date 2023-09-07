from django.urls import path
from .views import GenreListApiView, BookListByAuthorAPIView

urlpatterns = [
    path('genre/', GenreListApiView.as_view()),
    path('book_add/', BookListByAuthorAPIView.as_view()),
]
