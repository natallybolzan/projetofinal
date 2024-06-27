from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    unidade_medida = models.CharField(max_length=50)
    quantidade = models.FloatField()

    def __str__(self):
        return self.nome

class Receita(models.Model):
    nome_receita = models.CharField(max_length=255)
    ingrediente_Nome = models.TextField()
    qt_ingre = models.TextField()
    data = models.DateField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.nome_receita,self.ingrediente_Nome

class Lancamento(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return f"Lançamento de {self.receita} em {self.data}"

