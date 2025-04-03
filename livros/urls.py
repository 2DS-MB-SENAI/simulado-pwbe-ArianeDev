from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.get_livros, name="Livros")
]