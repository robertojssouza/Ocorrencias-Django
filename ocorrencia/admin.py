from django.contrib import admin
from ocorrencia.models import Filial, Curso, AulaAvulsa, Hora

admin.site.register(Filial)
admin.site.register(Curso)
admin.site.register(Hora)
admin.site.register(AulaAvulsa)