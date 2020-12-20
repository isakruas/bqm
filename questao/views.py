from rest_framework import mixins
from rest_framework import viewsets
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from .models import (
    Etapa,
    UnidadeTematica,
    ObjetoDeConhecimento,
    NivelDeDificuldade,
    Questao,
    Imprimir
)
from .serializers import (
    EtapaSerializer,
    UnidadeTematicaSerializer,
    ObjetoDeConhecimentoSerializer,
    NivelDeDificuldadeSerializer,
    QuestaoSerializer
)
from .permissions import (
    QuestaoPermissions,
    UsuarioPermissions
)


#############################################################
#                      Usuario autenticado                  #
#############################################################

class EtapaViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """API Etapa V1.0.0"""
    permission_classes = (UsuarioPermissions,)

    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer


class UnidadeTematicaViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """API Unidade temática V1.0.0"""

    permission_classes = (UsuarioPermissions,)

    queryset = UnidadeTematica.objects.all()
    serializer_class = UnidadeTematicaSerializer

    def list(self, request, *args, **kwargs):

        params = request.query_params
        params = params.dict()

        filters = ('etapa', 'ano')

        if 'format' in params:
            params.pop('format')

        if len(params) >> 0:
            query = {}
            for key in params:
                try:
                    if key in filters:
                        query[key] = int(params[key])
                except ValueError:
                    pass

            queryset = UnidadeTematica.objects.filter(**query)
            queryset = self.filter_queryset(queryset)
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ObjetoDeConhecimentoViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """API Objeto de conhecimento V1.0.0"""

    permission_classes = (UsuarioPermissions,)

    queryset = ObjetoDeConhecimento.objects.all()
    serializer_class = ObjetoDeConhecimentoSerializer

    def list(self, request, *args, **kwargs):

        params = request.query_params
        params = params.dict()

        filters = ('etapa', 'ano', 'unidade_tematica')

        if 'format' in params:
            params.pop('format')

        if len(params) >> 0:
            query = {}
            for key in params:
                try:
                    if key in filters:
                        query[key] = int(params[key])
                except ValueError:
                    pass

            queryset = ObjetoDeConhecimento.objects.filter(**query)
            queryset = self.filter_queryset(queryset)
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class NivelDeDificuldadeViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """API Nível de dificuldade V1.0.0"""

    permission_classes = (UsuarioPermissions,)

    queryset = NivelDeDificuldade.objects.all()
    serializer_class = NivelDeDificuldadeSerializer


class QuestaoViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """API Questao V1.0.0"""

    permission_classes = (QuestaoPermissions,)

    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer

    def list(self, request, *args, **kwargs):

        params = request.query_params
        params = params.dict()

        filters = ('status', 'etapa', 'ano', 'unidade_tematica', 'objeto_de_conhecimento', 'nivel_de_dificuldade')
        permission = ('admin', 'alfa', 'beta', 'gama', 'delta')
        if 'format' in params:
            params.pop('format')


        if len(params) >> 0:
            query = {}
            for key in params:
                try:
                    if key in filters:
                        if str(key) == 'status':
                            if str(request.user.nivel_de_acesso) in permission:
                                if 'cadastro_pelo_usuario' in params:
                                    query['cadastro_pelo_usuario'] = int(params['cadastro_pelo_usuario'])
                                else:
                                    query['cadastro_pelo_usuario'] = int(request.user.id)
                            else:
                                if int(params[key]) == 3:
                                    query['cadastro_pelo_usuario'] = int(request.user.id)
                                else:
                                    pass

                         
                        query[key] = int(params[key])
                         
                except ValueError:
                    pass

            queryset = Questao.objects.filter(**query)
            queryset = self.filter_queryset(queryset)
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)


        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


#############################################################
#                  Usuario nao autenticado                  #
#############################################################

def contagem_questao(request):
    contagem_questao = Questao.objects.all()

    return HttpResponse(contagem_questao.count())


def contagem_questao_status_2(request):
    contagem_questao_status_2 = Questao.objects.filter(status=2)

    return HttpResponse(contagem_questao_status_2.count())


def contagem_imprimir(request):
    contagem_imprimir = Imprimir.objects.all()

    return HttpResponse(contagem_imprimir.count())


def listar_etapas(request):
    etapa = Etapa.objects.all()

    template = loader.get_template('questao/templates/listar_etapas.html')
    context = {
        'etapa': etapa,
    }

    return HttpResponse(template.render(context, request))


def listar_anos(request, etapa):
    ano = UnidadeTematica.objects.filter(etapa=etapa)

    template = loader.get_template('questao/templates/listar_anos.html')
    context = {
        'ano': ano,
    }

    return HttpResponse(template.render(context, request))


def listar_unidades_tematicas(request, etapa, ano):
    unidade_tematica = UnidadeTematica.objects.filter(etapa=etapa, ano=ano)

    template = loader.get_template('questao/templates/listar_unidades_tematicas.html')
    context = {
        'unidade_tematica': unidade_tematica,
    }

    return HttpResponse(template.render(context, request))


def listar_objetos_de_conhecimento(request, etapa, ano, unidade_tematica):
    objeto_de_conhecimento = ObjetoDeConhecimento.objects.filter(etapa=etapa, ano=ano,
                                                                 unidade_tematica=unidade_tematica)
    template = loader.get_template('questao/templates/listar_objetos_de_conhecimento.html')
    context = {
        'objeto_de_conhecimento': objeto_de_conhecimento,
    }

    return HttpResponse(template.render(context, request))


def listar_niveis_de_dificuldade(request):
    nivel_de_dificuldade = NivelDeDificuldade.objects.all()

    template = loader.get_template('questao/templates/listar_niveis_de_dificuldade.html')
    context = {
        'nivel_de_dificuldade': nivel_de_dificuldade,
    }

    return HttpResponse(template.render(context, request))


def listar_usuario(request, id_u):
    usuario = Questao.objects.filter(cadastro_pelo_usuario=id_u)

    template = loader.get_template('questao/templates/listar_usuario.html')
    context = {
        'usuario': usuario,
    }

    return HttpResponse(template.render(context, request))
