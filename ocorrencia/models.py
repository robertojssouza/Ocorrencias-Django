from django.db import models


class Filial(models.Model):
    filial = models.CharField(max_length=30)

    def __str__(self):
        return self.filial


class Curso(models.Model):
    curso = models.CharField(max_length=50)

    def __str__(self):
        return self.curso


class Hora(models.Model):
    hora_inicio = models.TimeField(blank=False, null=False)
    hora_fim = models.TimeField(blank=False, null=False)

    def __str__(self):
        return f'{self.hora_inicio} - {self.hora_fim}'


class AulaAvulsa(models.Model):
    professor = models.CharField(max_length=100, blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    filial = models.ForeignKey(Filial, blank=False, null=False, on_delete=models.DO_NOTHING)
    curso = models.ForeignKey(Curso, blank=False, null=False, on_delete=models.DO_NOTHING)
    hora = models.ForeignKey(Hora, blank=False, null=False, on_delete=models.DO_NOTHING)
    motivo = models.TextField(blank=False, null=False)
    observacao = models.TextField(blank=True, null=False)

    def __str__(self):
        return f'{self.data}'
