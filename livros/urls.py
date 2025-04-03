from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.get_livros_template, name="livros"),
    path('api/livros/', views.get_livros, name="Livros"),
    path('api/livros/cadastrar', views.get_livros, name="Cadastrar livros")
]