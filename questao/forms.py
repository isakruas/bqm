from django import forms

from .models import (
    Etapa,
    UnidadeTematica,
    ObjetoDeConhecimento,
    NivelDeDificuldade,
    Questao
)


class QuestaoForm(forms.ModelForm):
    class Meta:
        extra_kwargs = {
            # ocultar o email na hora da consulta
            # 'email' : {'write_only':True},
        }

        model = Questao

        fields = '__all__'


class EtapaForm(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = '__all__'


class UnidadeTematicaForm(forms.ModelForm):
    class Meta:
        model = UnidadeTematica
        fields = '__all__'


class ObjetoDeConhecimentoForm(forms.ModelForm):
    class Meta:
        model = ObjetoDeConhecimento
        fields = '__all__'


class NivelDeDificuldadeForm(forms.ModelForm):
    class Meta:
        model = NivelDeDificuldade
        fields = '__all__'
