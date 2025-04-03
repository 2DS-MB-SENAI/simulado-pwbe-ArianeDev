from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import LivroSerializer
from rest_framework import status
from .models import Livro

@api_view(['GET', 'POST'])
def get_livros(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)