from django.db import models
from usuario.models import Usuario


class Base(models.Model):
    class Meta:
        abstract = True


class Etapa(Base):
    etapa = models.AutoField(
        primary_key=True
    )

    etapa_nome = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ['etapa']
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'

    def __str__(self):
        return ''


class UnidadeTematica(Base):
    etapa = models.IntegerField(
        null=False,
        blank=False,
    )

    unidade_tematica = models.AutoField(
        primary_key=True
    )

    ano = models.IntegerField(
        null=False,
        blank=False,
    )

    unidade_tematica_nome = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ['unidade_tematica']
        verbose_name = 'Unidade temática'
        verbose_name_plural = 'Unidades temáticas'

    def __str__(self):
        return ''


class ObjetoDeConhecimento(Base):
    etapa = models.IntegerField(
        null=False,
        blank=False,
    )

    unidade_tematica = models.IntegerField(
        null=False,
        blank=False,
    )

    ano = models.IntegerField(
        null=False,
        blank=False,
    )

    objeto_de_conhecimento = models.AutoField(
        primary_key=True
    )

    objeto_de_conhecimento_nome = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ['objeto_de_conhecimento']
        verbose_name = 'Objeto de conhecimento'
        verbose_name_plural = 'Objetos de conhecimento'

    def __str__(self):
        return ''


class NivelDeDificuldade(Base):
    nivel_de_dificuldade = models.AutoField(
        primary_key=True
    )

    nivel_de_dificuldade_nome = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ['nivel_de_dificuldade']
        verbose_name = 'Nível de dificuldade'
        verbose_name_plural = 'Níveis de dificuldade'

    def __str__(self):
        return ''


class Imprimir(Base):
    nome = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )

    cadastro_pelo_usuario = models.ForeignKey(Usuario, related_name='imprimir', on_delete=models.CASCADE)

    qids = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Imprimir'
        verbose_name_plural = 'Imprimir'

    def __str__(self):
        return ''


class Questao(Base):
    """
    status=1 registrada e aguardando verificação - usuário delta
    status=2 registrada e verificada - usuário delta e gama
    status=3 registrada - grupo elison - questão registrada pelo professor(a)
    status=4 registrada e verificada - elison questão registrada pelo professor e verificada por um gama
    """
    status = models.IntegerField(
        null=False,
        blank=False,
    )

    etapa = models.IntegerField(
        null=False,
        blank=False,
    )

    ano = models.IntegerField(
        null=False,
        blank=False,
    )

    unidade_tematica = models.IntegerField(
        null=False,
        blank=False,
    )

    objeto_de_conhecimento = models.IntegerField(
        null=False,
        blank=False,
    )

    nivel_de_dificuldade = models.IntegerField(
        null=False,
        blank=False,
    )

    imagem = models.IntegerField(
        null=True,
        blank=True
    )

    pergunta = models.TextField(
        null=False,
        blank=False,
    )

    resposta = models.TextField(
        null=False,
        blank=False,
    )

    cadastro_pelo_usuario = models.ForeignKey(Usuario, related_name='questao', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        ordering = ['id']

    def __str__(self):
        return ''
