from django.contrib import admin

from .models import (
    Etapa,
    UnidadeTematica,
    ObjetoDeConhecimento,
    NivelDeDificuldade,
    Questao,
    Imprimir
)


# from django.contrib.auth.models import Group
# from django.contrib.auth.models import User


@admin.register(Imprimir)
class ImprimirAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'cadastro_pelo_usuario',
        'qids'
    )


@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = (
        'etapa',
        'etapa_nome'
    )


@admin.register(UnidadeTematica)
class UnidadeTematicaAdmin(admin.ModelAdmin):
    list_display = (

        'etapa',
        'unidade_tematica',
        'ano',
        'unidade_tematica_nome'
    )


@admin.register(ObjetoDeConhecimento)
class ObjetoDeConhecimentoAdmin(admin.ModelAdmin):
    list_display = (

        'etapa',
        'unidade_tematica',
        'ano',
        'objeto_de_conhecimento',
        'objeto_de_conhecimento_nome'
    )


@admin.register(NivelDeDificuldade)
class NivelDeDificuldadeAdmin(admin.ModelAdmin):
    list_display = (

        'nivel_de_dificuldade',
        'nivel_de_dificuldade_nome'
    )


@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = (

        'status',
        'imagem',
        'pergunta',
        'resposta',
        'etapa',
        'ano',
        'unidade_tematica',
        'objeto_de_conhecimento',
        'nivel_de_dificuldade',
        'cadastro_pelo_usuario'

    )

# admin.site.unregister(Group)
# admin.site.unregister(User)
