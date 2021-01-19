from rest_framework import serializers
from .models import (
    Usuario,
    Filiacao
)
from django.contrib.auth.hashers import (
    make_password,
)


class UsuarioSerializer(serializers.ModelSerializer):
    questao = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    imprimir = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Usuario

        fields = [
            'id',
            'nome',
            'sobrenome',
            'email',
            'password',
            'escolaridade',
            'nivel_de_acesso',
            'questao',
            'imprimir'
        ]

    @staticmethod
    def validate_password(obj):
        return make_password(obj)


class FiliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # ocultar o email na hora da consulta
            # 'email' : {'write_only':True},
        }

        model = Filiacao

        fields = '__all__'
