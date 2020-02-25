from django.db import models

class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return self.nome
