from django.urls import path
from .views import UserRejestracjaView
urlpatterns = [
    path('rejestracja/', UserRejestracjaView.as_view(), name="rejestracja"),
]
