from django.contrib import admin

from .models import (
    Usuario
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