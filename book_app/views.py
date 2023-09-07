from django.shortcuts import render
from .serializers import CustomUserSerializers
from .models import CustomUser
from rest_framework import generics


class SignUpApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
