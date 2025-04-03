from django.db import models
from django.contrib.auth.models import AbstractUser

class Livro(models.Model):
    titulo = models.CharField(max_length=50, null=True, blank=True)
    autor = models.CharField(max_length=30, null=True, blank=True)
    paginas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username
