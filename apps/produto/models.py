from django.db import models

class Produto(models.Model):
    TIPO_CHOICES = [
        ('mercado', 'Mercado (Unidade)'),
        ('estoque', 'Estoque (Caixa)'),
    ]

    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    estoque = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='mercado')  

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()}"
