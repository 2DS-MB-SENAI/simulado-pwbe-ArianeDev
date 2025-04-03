from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import LivroSerializer
from .models import Livro

@api_view(['GET'])
def get_livros(request):
    livros = Livro.objects.all()
    serializer = LivroSerializer(livros, many = True)
    return Response(serializer.data)

