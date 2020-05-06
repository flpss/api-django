from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    edicao = models.CharField(max_length=50)
    quantidade = models.PositiveIntegerField()
    def __str__(self):
        return self.titulo + " - " + self.autor

class Emprestimo(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30, null=True, blank=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        self.nome + " - " + self.livro.autor