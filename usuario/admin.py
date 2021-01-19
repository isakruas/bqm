from django.contrib import admin

from .models import (
    Usuario,
    Filiacao
)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'password',
        'nome',
        'sobrenome',
        'escolaridade',
        'nivel_de_acesso',
        'is_superuser',
        'is_active'

    )


@admin.register(Filiacao)
class FiliacaoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'superior',
        'inferior'

    )
