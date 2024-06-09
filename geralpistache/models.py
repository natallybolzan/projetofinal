from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    unidade_medida = models.CharField(max_length=50)
    quantidade = models.FloatField()

    def __str__(self):
        return self.descricao


class Compra(models.Model):
    data = models.DateField()
    fornecedor = models.CharField(max_length=255)

    def __str__(self):
        return f"Compra {self.id} de {self.fornecedor} em {self.data}"


class CompraItem(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    unidade_medida = models.CharField(max_length=50)
    quantidade = models.FloatField()

    def __str__(self):
        return f"{self.quantidade} {self.unidade_medida} de {self.produto} na {self.compra}"

class Receita(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class ReceitaItem(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    unidade_medida = models.CharField(max_length=50)
    quantidade = models.FloatField()

    def __str__(self):
        return f"{self.quantidade} {self.unidade_medida} de {self.produto} na {self.receita}"

class Lancamento(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return f"Lançamento de {self.receita} em {self.data}"

