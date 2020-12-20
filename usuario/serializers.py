from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import (
    Usuario,
    Filiacao
)

from questao.serializers import QuestaoSerializer, ImprimirSerializer
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)


class UsuarioSerializer(serializers.ModelSerializer):

    """
    questao = QuestaoSerializer(many=True, read_only=True)
    imprimir = ImprimirSerializer(many=True, read_only=True)

    questao = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='questao-detail'
    )

    imprimir = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='imprimir-detail'
    )
    """
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

    def validate_password(self, obj):
        return make_password(obj)


class FiliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # ocultar o email na hora da consulta
            # 'email' : {'write_only':True},
        }

        model = Filiacao

        fields = '__all__'