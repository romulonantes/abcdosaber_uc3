from django.db import models

class Aluno(models.Model):
    codigo = models.AutoField(
        primary_key=True,
        help_text='Código do Aluno'
    )

    nome = models.CharField(
        max_length=100,
        null=False,
        help_text='Informe o nome do aluno'
    )

    def __str__(self):
        return f'{self.codigo} - {self.nome}'