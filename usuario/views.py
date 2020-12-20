from rest_framework import mixins, status
from rest_framework import viewsets

from .serializers import (
    UsuarioSerializer,
    FiliacaoSerializer
)

from questao.serializers import (
    ImprimirSerializer
)

from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from questao.models import (
    Etapa,
    UnidadeTematica,
    ObjetoDeConhecimento,
    NivelDeDificuldade,
    Questao,
    Imprimir
)
from questao.forms import (
    EtapaForm,
    UnidadeTematicaForm,
    ObjetoDeConhecimentoForm,
    NivelDeDificuldadeForm,
    QuestaoForm
)
from django.http import HttpResponse
from django.template import loader
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
from rest_framework.settings import api_settings


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


class Redirecionar:

    def para_usuario(url):
        return redirect('/usuario/')

    def para_entrar(url):
        return redirect('/usuario/entrar/')

    def para_criar_conta(url):
        return redirect('/usuario/criar_conta/')

    def para_recuperar_senha(url):
        return redirect('/usuario/recuperar_senha/')

    def para_entrar_concluido(request):
        template = loader.get_template('usuario/templates/registration/entrar_concluido.html')
        context = {}
        return HttpResponse(template.render(context, request))


#############################################################
#                  Usuario nao autenticado                  #
#############################################################

class UsuarioCriarConta(CreateView):
    '''  '''
    template_name = 'usuario/templates/registration/criar_conta.html'
    form_class = UsuarioCreationForm
    success_url = 'concluido/'


class UsuarioEntrarConcluido(TemplateView):
    template_name = 'usuario/templates/registration/entrar_concluido.html'


def UsuarioFiliacaoSuperiorInferior(request, id_u):
    fsi = Filiacao.objects.filter(superior=id_u)

    template = loader.get_template('usuario/templates/filiacao_superior_inferior.html')
    context = {
        'fsi': fsi,
    }

    return HttpResponse(template.render(context, request))


def UsuarioFiliacaoInferiorSuperior(request, id_u):
    fis = Filiacao.objects.filter(inferior=id_u)

    template = loader.get_template('usuario/templates/filiacao_inferior_superior.html')
    context = {
        'fis': fis,
    }

    return HttpResponse(template.render(context, request))


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


class UsuarioAlfaConfiguracaoExcluirConta(DeleteView):
    model = Usuario
    template_name = 'usuario/templates/alfa/excluir_conta.html'
    success_url = '../../../sair/'


class UsuarioAlfaManual(TemplateView):
    template_name = 'usuario/templates/alfa/manual.html'


class UsuarioAlfaIrPara(TemplateView):
    template_name = 'usuario/templates/alfa/ir_para.html'


class UsuarioAlfaCadastrarUsuarioBeta(CreateView):
    template_name = 'usuario/templates/alfa/cadastrar_usuario_beta.html'
    form_class = UsuarioCreationForm
    success_url = './concluido/'


def UsuarioAlfaCadastrarFiliacao(request):
    # tem que melhorar essa função para evitar erros no processamento, como por exemplo, a duplicidade de registro de ids
    el = Usuario.objects.last()
    user = request.user.id
    filiacao = Filiacao(superior=user, inferior=el.id)
    filiacao.save();

    return redirect('../../../../')


class UsuarioAlfaListarUsuarioGama(TemplateView):
    template_name = 'usuario/templates/alfa/listar_usuario_gama.html'


def UsuarioAlfaListarUsuarioGamaDetalhes(request, id_u):
    usuario = Usuario.objects.filter(id=id_u)

    template = loader.get_template('usuario/templates/alfa/listar_usuario_gama_detalhes.html')
    context = {
        'detalhes': usuario,
    }

    return HttpResponse(template.render(context, request))


class UsuarioAlfaListarUsuarioDelta(TemplateView):
    template_name = 'usuario/templates/alfa/listar_usuario_delta.html'


def UsuarioAlfaListarUsuarioDeltaDetalhes(request, id_u):
    usuario = Usuario.objects.filter(id=id_u)

    template = loader.get_template('usuario/templates/alfa/listar_usuario_delta_detalhes.html')
    context = {
        'detalhes': usuario,
    }

    return HttpResponse(template.render(context, request))


class UsuarioAlfaListarUsuarioBeta(TemplateView):
    template_name = 'usuario/templates/alfa/listar_usuario_beta.html'


def UsuarioAlfaListarUsuarioBetaDetalhes(request, id_u):
    usuario = Usuario.objects.filter(id=id_u)

    template = loader.get_template('usuario/templates/alfa/listar_usuario_beta_detalhes.html')
    context = {
        'detalhes': usuario,
    }

    return HttpResponse(template.render(context, request))


def usuario_alfa_contagem_usuario_alfa(request):
    usuario_alfa_contagem_usuario_alfa = Usuario.objects.filter(nivel_de_acesso='alfa')

    return HttpResponse(usuario_alfa_contagem_usuario_alfa.count())


def usuario_alfa_contagem_usuario_beta(request):
    usuario_alfa_contagem_usuario_beta = Usuario.objects.filter(nivel_de_acesso='beta')

    return HttpResponse(usuario_alfa_contagem_usuario_beta.count())


def usuario_alfa_contagem_usuario_gama(request):
    usuario_alfa_contagem_usuario_gama = Usuario.objects.filter(nivel_de_acesso='gama')

    return HttpResponse(usuario_alfa_contagem_usuario_gama.count())


def usuario_alfa_contagem_usuario_delta(request):
    usuario_alfa_contagem_usuario_delta = Usuario.objects.filter(nivel_de_acesso='delta')

    return HttpResponse(usuario_alfa_contagem_usuario_delta.count())


def usuario_alfa_contagem_usuario_epsilon(request):
    usuario_alfa_contagem_usuario_epsilon = Usuario.objects.filter(nivel_de_acesso='epsilon')

    return HttpResponse(usuario_alfa_contagem_usuario_epsilon.count())


#############################################################
#              Usuario com nivel de acesso Beta             #
#############################################################

class UsuarioBetaInicio(TemplateView):
    template_name = 'usuario/templates/beta/inicio.html'


class UsuarioBetaConfiguracao(TemplateView):
    template_name = 'usuario/templates/beta/configuracao.html'


class UsuarioBetaConfiguracaoExcluirConta(DeleteView):
    model = Usuario
    template_name = 'usuario/templates/beta/excluir_conta.html'
    success_url = '../../../sair/'


class UsuarioBetaManual(TemplateView):
    template_name = 'usuario/templates/beta/manual.html'


class UsuarioBetaIrPara(TemplateView):
    template_name = 'usuario/templates/beta/ir_para.html'


class UsuarioBetaCadastrarEtapa(CreateView):
    template_name = 'usuario/templates/beta/cadastrar_etapa.html'
    form_class = EtapaForm
    success_url = 'concluido/'


class UsuarioBetaCadastrarUnidadeTematica(CreateView):
    template_name = 'usuario/templates/beta/cadastrar_unidade_tematica.html'
    form_class = UnidadeTematicaForm
    success_url = 'concluido/'


class UsuarioBetaCadastrarObjetoDeConhecimento(CreateView):
    template_name = 'usuario/templates/beta/cadastrar_objeto_de_conhecimento.html'
    form_class = ObjetoDeConhecimentoForm
    success_url = 'concluido/'


class UsuarioBetaCadastrarNivelDeDificuldade(CreateView):
    template_name = 'usuario/templates/beta/cadastrar_nivel_de_dificuldade.html'
    form_class = NivelDeDificuldadeForm
    success_url = 'concluido/'


def UsuarioBetaListarEtapa(request):
    etapa = Etapa.objects.all()

    template = loader.get_template('usuario/templates/beta/listar_etapa.html')
    context = {
        'etapa': etapa,
    }

    return HttpResponse(template.render(context, request))


def UsuarioBetaListarUnidadeTematica(request):
    unidade_tematica = UnidadeTematica.objects.all()

    template = loader.get_template('usuario/templates/beta/listar_unidade_tematica.html')
    context = {
        'unidade_tematica': unidade_tematica,
    }

    return HttpResponse(template.render(context, request))


def UsuarioBetaListarObjetoDeConhecimento(request):
    objeto_de_conhecimento = ObjetoDeConhecimento.objects.all()

    template = loader.get_template('usuario/templates/beta/listar_objeto_de_conhecimento.html')
    context = {
        'objeto_de_conhecimento': objeto_de_conhecimento,
    }

    return HttpResponse(template.render(context, request))


def UsuarioBetaListarNivelDeDificuldade(request):
    nivel_de_dificuldade = NivelDeDificuldade.objects.all()

    template = loader.get_template('usuario/templates/beta/listar_nivel_de_dificuldade.html')
    context = {
        'nivel_de_dificuldade': nivel_de_dificuldade,
    }

    return HttpResponse(template.render(context, request))


class UsuarioBetaEditarEtapa(UpdateView):
    model = Etapa
    template_name = 'usuario/templates/beta/editar_etapa.html'
    fields = ['etapa_nome']
    success_url = '../concluido/'


class UsuarioBetaEditarUnidadeTematica(UpdateView):
    model = UnidadeTematica
    template_name = 'usuario/templates/beta/editar_unidade_tematica.html'
    fields = ['etapa', 'ano', 'unidade_tematica_nome']
    success_url = '../concluido/'


class UsuarioBetaEditarObjetoDeConhecimento(UpdateView):
    model = ObjetoDeConhecimento
    template_name = 'usuario/templates/beta/editar_objeto_de_conhecimento.html'
    fields = ['etapa', 'unidade_tematica', 'ano', 'objeto_de_conhecimento_nome']
    success_url = '../concluido/'


class UsuarioBetaEditarNivelDeDificuldade(UpdateView):
    model = NivelDeDificuldade
    template_name = 'usuario/templates/beta/editar_nivel_de_dificuldade.html'
    fields = ['nivel_de_dificuldade_nome']
    success_url = '../concluido/'


class UsuarioBetaListarUsuarioGama(TemplateView):
    template_name = 'usuario/templates/beta/listar_usuario_gama.html'


def UsuarioBetaListarUsuarioGamaDetalhes(request, id_u):
    usuario = Usuario.objects.filter(id=id_u)

    template = loader.get_template('usuario/templates/beta/listar_usuario_gama_detalhes.html')
    context = {
        'detalhes': usuario,
    }

    return HttpResponse(template.render(context, request))


class UsuarioBetaListarUsuarioDelta(TemplateView):
    template_name = 'usuario/templates/beta/listar_usuario_delta.html'


def UsuarioBetaListarUsuarioDeltaDetalhes(request, id_u):
    usuario = Usuario.objects.filter(id=id_u)

    template = loader.get_template('usuario/templates/beta/listar_usuario_delta_detalhes.html')
    context = {
        'detalhes': usuario,
    }

    return HttpResponse(template.render(context, request))


class UsuarioBetaCadastrarUsuarioGama(CreateView):
    template_name = 'usuario/templates/beta/cadastrar_usuario_gama.html'
    form_class = UsuarioCreationForm
    success_url = './concluido/'


def UsuarioBetaCadastrarFiliacao(request):
    # tem que melhorar essa função para evitar erros no processamento, como por exemplo, a duplicidade de registro de ids
    el = Usuario.objects.last()
    user = request.user.id
    filiacao = Filiacao(superior=user, inferior=el.id)
    filiacao.save();

    return redirect('../../../../ir_para/')


#############################################################
#              Usuario com nivel de acesso Gama             #
#############################################################

class UsuarioGamaInicio(TemplateView):
    template_name = 'usuario/templates/gama/inicio.html'


class UsuarioGamaConfiguracao(TemplateView):
    template_name = 'usuario/templates/gama/configuracao.html'


class UsuarioGamaConfiguracaoExcluirConta(DeleteView):
    model = Usuario
    template_name = 'usuario/templates/gama/excluir_conta.html'
    success_url = '../../../sair/'


class UsuarioGamaManual(TemplateView):
    template_name = 'usuario/templates/gama/manual.html'


class UsuarioGamaIrPara(TemplateView):
    template_name = 'usuario/templates/gama/ir_para.html'


class UsuarioGamaCadastrarUsuarioDelta(CreateView):
    template_name = 'usuario/templates/gama/cadastrar_usuario_delta.html'
    form_class = UsuarioCreationForm
    success_url = './concluido/'


def UsuarioGamaCadastrarFiliacao(request):
    # tem que melhorar essa função para evitar erros no processamento, como por exemplo, a duplicidade de registro de ids
    el = Usuario.objects.last()
    user = request.user.id
    filiacao = Filiacao(superior=user, inferior=el.id)
    filiacao.save();

    return redirect('../../../../ir_para/')


class UsuarioGamaListarUsuarioDelta(TemplateView):
    template_name = 'usuario/templates/gama/listar_usuario_delta.html'


def UsuarioGamaListarUsuarioDeltaDetalhes(request, id_u):
    usuario = Usuario.objects.filter(id=id_u)

    template = loader.get_template('usuario/templates/gama/listar_usuario_delta_detalhes.html')
    context = {
        'detalhes': usuario,
    }

    return HttpResponse(template.render(context, request))


class UsuarioGamaEditarQuestao(UpdateView):
    model = Questao
    template_name = 'usuario/templates/gama/editar_questao.html'
    fields = ['etapa', 'ano', 'unidade_tematica', 'objeto_de_conhecimento', 'nivel_de_dificuldade', 'imagem',
              'pergunta', 'resposta', 'status']

    success_url = '../concluido/'


class UsuarioGamaExcluirQuestao(DeleteView):
    model = Questao
    template_name = 'usuario/templates/gama/excluir_questao.html'
    success_url = '../concluido/'


#############################################################
#              Usuario com nivel de acesso Delta            #
#############################################################

class UsuarioDeltaInicio(TemplateView):
    template_name = 'usuario/templates/delta/inicio.html'


class UsuarioDeltaConfiguracao(TemplateView):
    template_name = 'usuario/templates/delta/configuracao.html'


class UsuarioDeltaConfiguracaoExcluirConta(DeleteView):
    model = Usuario
    template_name = 'usuario/templates/delta/excluir_conta.html'
    success_url = '../../../sair/'


class UsuarioDeltaManual(TemplateView):
    template_name = 'usuario/templates/delta/manual.html'


class UsuarioDeltaCadastrarQuestao(CreateView):
    template_name = 'usuario/templates/delta/cadastrar_questao.html'
    form_class = QuestaoForm
    success_url = 'concluido/'


class UsuarioDeltaEditarQuestao(UpdateView):
    model = Questao
    template_name = 'usuario/templates/delta/editar_questao.html'
    fields = ['etapa', 'ano', 'unidade_tematica', 'objeto_de_conhecimento', 'nivel_de_dificuldade', 'imagem',
              'pergunta', 'resposta']

    success_url = '../concluido/'


class UsuarioDeltaExcluirQuestao(DeleteView):
    model = Questao
    template_name = 'usuario/templates/delta/excluir_questao.html'
    success_url = '../concluido/'


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
    template_name =  'usuario/templates/epsilon/bqp_listar_questao.html'


class UsuarioEpsilonBQPEditarQuestao(TemplateView):
    template_name =  'usuario/templates/epsilon/bqp_editar_questao.html'
 

class UsuarioEpsilonInicio(TemplateView):
    template_name = 'usuario/templates/epsilon/inicio.html'


class UsuarioEpsilonGerarAvaliacao(TemplateView):
    template_name = 'usuario/templates/epsilon/gerar_avaliacao.html'


class UsuarioEpsilonGerarAvaliacaoVisualizar(TemplateView):
    template_name = 'usuario/templates/epsilon/gerar_avaliacao_visualizar.html'


class UsuarioEpsilonImprimirAvaliacao(TemplateView):
    template_name = 'usuario/templates/epsilon/imprimir_avaliacao.html'

