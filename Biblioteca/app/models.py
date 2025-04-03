from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=50, null=True, blank=True)
    autor = models.CharField(max_length=30, null=True, blank=True)
    paginas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo