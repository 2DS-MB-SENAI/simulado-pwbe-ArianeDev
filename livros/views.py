from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import LivroSerializer, UsuarioSerializer
from rest_framework import status
from .models import Livro, Usuario
from .forms import Forms

@api_view(['GET', 'POST'])
def get_livros(requests):
    if requests.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many = True)

        return Response(serializer.data), render(requests, 'livros.html', {'livros': livros})
    
    if requests.method == 'POST':
        serializer = LivroSerializer(data=requests.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_livros_template(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})

@api_view(['POST', 'GET'])
def post_usuario(request):
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # if request.method == 'GET':