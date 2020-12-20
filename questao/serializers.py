from rest_framework import serializers

from .models import (
    Etapa,
    UnidadeTematica,
    ObjetoDeConhecimento,
    NivelDeDificuldade,
    Questao,
    Imprimir
)


class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # ocultar o email na hora da consulta
            # 'email' : {'write_only':True},
        }

        model = Etapa

        fields = '__all__'


class UnidadeTematicaSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # ocultar o email na hora da consulta
            # 'email' : {'write_only':True},
        }

        model = UnidadeTematica

        fields = '__all__'


class ObjetoDeConhecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # ocultar o email na hora da consulta
            # 'email' : {'write_only':True},
        }

        model = ObjetoDeConhecimento

        fields = '__all__'


class NivelDeDificuldadeSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # ocultar o email na hora da consulta
            # 'email' : {'write_only':True},
        }

        model = NivelDeDificuldade

        fields = '__all__'


class QuestaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # ocultar o email na hora da consulta
            # 'email' : {'write_only':True},
        }

        model = Questao

        fields = '__all__'


class ImprimirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imprimir

        fields = '__all__'
