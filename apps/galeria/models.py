from django.db import models

from datetime import datetime

from django.contrib.auth.models import User


class Fotografia(models.Model): ## Faz a classe de POO funcionar como um banco de dados

    OPCOES_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)## Maximo de caracteres dentro do nome
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')  
    descricao = models.TextField(null = False, blank = False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)## colocou data para quando for cadastrado, blank = True pois faremos uma configuração para quando não houver foto cadastrada
    publicada = models.BooleanField(default=True) ## Para ja ficar como False antes de publicar, se quiser na pagina inicial tera que acionar o true
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )


    def __str__(self):
        return self.nome
