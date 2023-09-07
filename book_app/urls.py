from django.urls import path
from .views import SignUpApiView
from .models import CustomUser

urlpatterns = [
    path('sign_up/', SignUpApiView.as_view()),
]
