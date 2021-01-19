from rest_framework import mixins
from rest_framework import viewsets
from .serializers import (
    UsuarioSerializer,
    FiliacaoSerializer
)
from questao.serializers import (
    ImprimirSerializer
)
from django.views.generic import TemplateView, CreateView
from questao.models import (
    Imprimir
)
from django.http import HttpResponse
from .forms import (
    UsuarioCreationForm
)
from .models import (
    Usuario,
    Filiacao
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .permissions import (
    UsuarioPermissions,
    FiliacaoPermissions,
    ImprimirPermissions
)


class FiliacaoViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """ Filiação API v1.0.0"""
    permission_classes = (FiliacaoPermissions,)

    queryset = Filiacao.objects.all()
    serializer_class = FiliacaoSerializer

    def list(self, request, *args, **kwargs):

        params = request.query_params
        params = params.dict()

        filters = ('superior', 'inferior')
        permission = ('admin', 'alfa', 'beta')
        if 'format' in params:
            params.pop('format')

        if len(params) >> 0:
            query = {}
            for key in params:
                try:
                    if key in filters:
                        if str(request.user.nivel_de_acesso) in permission:
                            if 'superior' in params:
                                query['superior'] = int(params['superior'])
                        elif str(request.user.nivel_de_acesso) == 'gama':
                            if 'superior' in params:
                                query['superior'] = int(request.user.id)
                        query[key] = int(params[key])
                except ValueError:
                    pass

            queryset = Filiacao.objects.filter(**query)
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


class UsuarioViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    permission_classes = (UsuarioPermissions,)

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def list(self, request, *args, **kwargs):

        params = request.query_params
        params = params.dict()

        filters = 'nivel_de_acesso'
        permission = ('admin', 'alfa')
        if 'format' in params:
            params.pop('format')

        if len(params) >> 0:
            query = {}
            for key in params:
                try:
                    if key in filters:
                        if str(request.user.nivel_de_acesso) in permission:
                            if 'nivel_de_acesso' in params:
                                query['nivel_de_acesso'] = str(params['nivel_de_acesso'])
                        query[key] = int(params[key])
                except ValueError:
                    pass

            queryset = Usuario.objects.filter(**query)
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


class ImprimirViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    permission_classes = (ImprimirPermissions,)

    queryset = Imprimir.objects.all()
    serializer_class = ImprimirSerializer


#############################################################
#                          Base                             #
#############################################################

"""
    Utilizada na API JS
"""


def get_or_create_token(request):
    uid = request.user.id

    for user in Usuario.objects.all():
        Token.objects.get_or_create(user=user)

    token = Token.objects.get(user=int(uid))

    return HttpResponse('{"token":"' + f"{token}" + '", "id":' + f"{uid}" + '}')


class UsuarioObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(UsuarioObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


#############################################################
#                  Usuario nao autenticado                  #
#############################################################

class UsuarioCriarConta(CreateView):
    template_name = 'usuario/templates/registration/criar_conta.html'
    form_class = UsuarioCreationForm
    success_url = 'concluido/'


class UsuarioEntrarConcluido(TemplateView):
    template_name = 'usuario/templates/registration/entrar_concluido.html'


#############################################################
#                     Usuario autenticado                   #
#############################################################

#############################################################
#              Usuario com nivel de acesso Alfa             #
#############################################################

class UsuarioAlfaInicio(TemplateView):
    template_name = 'usuario/templates/alfa/inicio.html'


class UsuarioAlfaConfiguracao(TemplateView):
    template_name = 'usuario/templates/alfa/configuracao.html'


class UsuarioAlfaManual(TemplateView):
    template_name = 'usuario/templates/alfa/manual.html'


class UsuarioAlfaIrPara(TemplateView):
    template_name = 'usuario/templates/alfa/ir_para.html'


class UsuarioAlfaCadastrarUsuarioBeta(TemplateView):
    template_name = 'usuario/templates/alfa/cadastrar_usuario_beta.html'


class UsuarioAlfaListarUsuarioBeta(TemplateView):
    template_name = 'usuario/templates/alfa/listar_usuario_beta.html'


class UsuarioAlfaDetalhesUsuarioBeta(TemplateView):
    template_name = 'usuario/templates/alfa/detalhes_usuario_beta.html'


class UsuarioAlfaEditarUsuarioBeta(TemplateView):
    template_name = 'usuario/templates/alfa/editar_usuario_beta.html'


#############################################################
#              Usuario com nivel de acesso Beta             #
#############################################################

class UsuarioBetaInicio(TemplateView):
    template_name = 'usuario/templates/beta/inicio.html'


class UsuarioBetaConfiguracao(TemplateView):
    template_name = 'usuario/templates/beta/configuracao.html'


class UsuarioBetaManual(TemplateView):
    template_name = 'usuario/templates/beta/manual.html'


class UsuarioBetaIrPara(TemplateView):
    template_name = 'usuario/templates/beta/ir_para.html'


class UsuarioBetaListarUsuarioGama(TemplateView):
    template_name = 'usuario/templates/beta/listar_usuario_gama.html'


class UsuarioBetaCadastrarUsuarioGama(TemplateView):
    template_name = 'usuario/templates/beta/cadastrar_usuario_gama.html'


class UsuarioBetaDetalhesUsuarioGama(TemplateView):
    template_name = 'usuario/templates/beta/detalhes_usuario_gama.html'


class UsuarioBetaEditarUsuarioGama(TemplateView):
    template_name = 'usuario/templates/beta/editar_usuario_gama.html'


class UsuarioBetaCadastrarEtapa(TemplateView):
    template_name = 'usuario/templates/beta/cadastrar_etapa.html'


class UsuarioBetaListarEtapa(TemplateView):
    template_name = 'usuario/templates/beta/listar_etapa.html'


class UsuarioBetaEditarEtapa(TemplateView):
    template_name = 'usuario/templates/beta/editar_etapa.html'


class UsuarioBetaCadastrarUnidadeTematica(TemplateView):
    template_name = 'usuario/templates/beta/cadastrar_unidade_tematica.html'


class UsuarioBetaListarUnidadeTematica(TemplateView):
    template_name = 'usuario/templates/beta/listar_unidade_tematica.html'


class UsuarioBetaEditarUnidadeTematica(TemplateView):
    template_name = 'usuario/templates/beta/editar_unidade_tematica.html'


class UsuarioBetaCadastrarObjetoDeConhecimento(TemplateView):
    template_name = 'usuario/templates/beta/cadastrar_objeto_de_conhecimento.html'


class UsuarioBetaListarObjetoDeConhecimento(TemplateView):
    template_name = 'usuario/templates/beta/listar_objeto_de_conhecimento.html'


class UsuarioBetaEditarObjetoDeConhecimento(TemplateView):
    template_name = 'usuario/templates/beta/editar_objeto_de_conhecimento.html'


class UsuarioBetaCadastrarNivelDeDificuldade(TemplateView):
    template_name = 'usuario/templates/beta/cadastrar_nivel_de_dificuldade.html'


class UsuarioBetaListarNivelDeDificuldade(TemplateView):
    template_name = 'usuario/templates/beta/listar_nivel_de_dificuldade.html'


class UsuarioBetaEditarNivelDeDificuldade(TemplateView):
    template_name = 'usuario/templates/beta/editar_nivel_de_dificuldade.html'


#############################################################
#              Usuario com nivel de acesso Gama             #
#############################################################

class UsuarioGamaInicio(TemplateView):
    template_name = 'usuario/templates/gama/inicio.html'


class UsuarioGamaConfiguracao(TemplateView):
    template_name = 'usuario/templates/gama/configuracao.html'


class UsuarioGamaManual(TemplateView):
    template_name = 'usuario/templates/gama/manual.html'


class UsuarioGamaIrPara(TemplateView):
    template_name = 'usuario/templates/gama/ir_para.html'


class UsuarioGamaCadastrarUsuarioDelta(TemplateView):
    template_name = 'usuario/templates/gama/cadastrar_usuario_delta.html'


class UsuarioGamaListarUsuarioDelta(TemplateView):
    template_name = 'usuario/templates/gama/listar_usuario_delta.html'


class UsuarioGamaDetalhesUsuarioDelta(TemplateView):
    template_name = 'usuario/templates/gama/detalhes_usuario_delta.html'


class UsuarioGamaEditarUsuarioDelta(TemplateView):
    template_name = 'usuario/templates/gama/editar_usuario_delta.html'


class UsuarioGamaRevisarQuestao(TemplateView):
    template_name = 'usuario/templates/gama/revisar_questao.html'


class UsuarioGamaListarQuestao(TemplateView):
    template_name = 'usuario/templates/gama/listar_questao.html'


class UsuarioGamaListarQuestaoUID(TemplateView):
    template_name = 'usuario/templates/gama/listar_questao_uid.html'


#############################################################
#              Usuario com nivel de acesso Delta            #
#############################################################

class UsuarioDeltaInicio(TemplateView):
    template_name = 'usuario/templates/delta/inicio.html'


class UsuarioDeltaConfiguracao(TemplateView):
    template_name = 'usuario/templates/delta/configuracao.html'


class UsuarioDeltaManual(TemplateView):
    template_name = 'usuario/templates/delta/manual.html'


class UsuarioDeltaCadastrarQuestao(TemplateView):
    template_name = 'usuario/templates/delta/cadastrar_questao.html'


class UsuarioDeltaListarQuestao(TemplateView):
    template_name = 'usuario/templates/delta/listar_questao.html'


class UsuarioDeltaEditarQuestao(TemplateView):
    template_name = 'usuario/templates/delta/editar_questao.html'


#############################################################
#            Usuario com nivel de acesso Epsilon            #
#############################################################

class UsuarioEpsilonManual(TemplateView):
    template_name = 'usuario/templates/epsilon/manual.html'


class UsuarioEpsilonConfiguracao(TemplateView):
    template_name = 'usuario/templates/epsilon/configuracao.html'


class UsuarioEpsilonBQP(TemplateView):
    template_name = 'usuario/templates/epsilon/bqp.html'


class UsuarioEpsilonBQPCadastrarQuestao(TemplateView):
    template_name = 'usuario/templates/epsilon/bqp_cadastrar_questao.html'


class UsuarioEpsilonBQPListarQuestao(TemplateView):
    template_name = 'usuario/templates/epsilon/bqp_listar_questao.html'


class UsuarioEpsilonBQPEditarQuestao(TemplateView):
    template_name = 'usuario/templates/epsilon/bqp_editar_questao.html'


class UsuarioEpsilonInicio(TemplateView):
    template_name = 'usuario/templates/epsilon/inicio.html'


class UsuarioEpsilonGerarAvaliacao(TemplateView):
    template_name = 'usuario/templates/epsilon/gerar_avaliacao.html'


class UsuarioEpsilonGerarAvaliacaoVisualizar(TemplateView):
    template_name = 'usuario/templates/epsilon/gerar_avaliacao_visualizar.html'


class UsuarioEpsilonImprimirAvaliacao(TemplateView):
    template_name = 'usuario/templates/epsilon/imprimir_avaliacao.html'
