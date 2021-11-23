from django.urls import path, include
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api_register'),
    path('login/', LoginView.as_view(), name='api_login'),
]

