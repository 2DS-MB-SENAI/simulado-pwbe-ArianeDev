from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import Forms

# @api_view(['GET', 'POST'])
# def get_livros(request):
#     if request.method == 'GET':
#         livros = Livro.objects.all()
#         serializer = LivroSerializer(livros, many = True)

#         return Response(serializer.data), render(request, 'livros.html', {'livros': livros})
    
#     if request.method == 'POST':
#         serializer = LivroSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.errors, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_livros_template(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})