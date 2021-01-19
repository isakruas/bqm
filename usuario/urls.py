from rest_framework.routers import SimpleRouter
from .views import (
    #############################################################
    #                  Usuario nao autenticado                  #
    #############################################################
    UsuarioViewSet,
    ImprimirViewSet,
    FiliacaoViewSet,
    UsuarioCriarConta,
    UsuarioEntrarConcluido,
    #############################################################
    #              Usuario com nivel de acesso Alfa             #
    #############################################################
    UsuarioAlfaInicio,
    UsuarioAlfaConfiguracao,
    UsuarioAlfaManual,
    UsuarioAlfaIrPara,
    UsuarioAlfaCadastrarUsuarioBeta,
    UsuarioAlfaListarUsuarioBeta,
    UsuarioAlfaDetalhesUsuarioBeta,
    UsuarioAlfaEditarUsuarioBeta,
    #############################################################
    #              Usuario com nivel de acesso Beta             #
    #############################################################
    UsuarioBetaInicio,
    UsuarioBetaConfiguracao,
    UsuarioBetaManual,
    UsuarioBetaIrPara,
    UsuarioBetaListarUsuarioGama,
    UsuarioBetaDetalhesUsuarioGama,
    UsuarioBetaCadastrarUsuarioGama,
    UsuarioBetaEditarUsuarioGama,
    UsuarioBetaCadastrarEtapa,
    UsuarioBetaListarEtapa,
    UsuarioBetaEditarEtapa,
    UsuarioBetaCadastrarUnidadeTematica,
    UsuarioBetaListarUnidadeTematica,
    UsuarioBetaEditarUnidadeTematica,
    UsuarioBetaCadastrarObjetoDeConhecimento,
    UsuarioBetaListarObjetoDeConhecimento,
    UsuarioBetaEditarObjetoDeConhecimento,
    UsuarioBetaCadastrarNivelDeDificuldade,
    UsuarioBetaListarNivelDeDificuldade,
    UsuarioBetaEditarNivelDeDificuldade,
    #############################################################
    #              Usuario com nivel de acesso Gama             #
    #############################################################
    UsuarioGamaInicio,
    UsuarioGamaConfiguracao,
    UsuarioGamaManual,
    UsuarioGamaIrPara,
    UsuarioGamaCadastrarUsuarioDelta,
    UsuarioGamaListarUsuarioDelta,
    UsuarioGamaDetalhesUsuarioDelta,
    UsuarioGamaEditarUsuarioDelta,
    UsuarioGamaRevisarQuestao,
    UsuarioGamaListarQuestao,
    UsuarioGamaListarQuestaoUID,
    #############################################################
    #              Usuario com nivel de acesso Delta            #
    #############################################################
    UsuarioDeltaInicio,
    UsuarioDeltaConfiguracao,
    UsuarioDeltaManual,
    UsuarioDeltaCadastrarQuestao,
    UsuarioDeltaListarQuestao,
    UsuarioDeltaEditarQuestao,
    #############################################################
    #            Usuario com nivel de acesso Epsilon            #
    #############################################################
    UsuarioEpsilonInicio,
    UsuarioEpsilonConfiguracao,
    UsuarioEpsilonManual,
    UsuarioEpsilonGerarAvaliacao,
    UsuarioEpsilonGerarAvaliacaoVisualizar,
    UsuarioEpsilonImprimirAvaliacao,
    UsuarioEpsilonBQP,
    UsuarioEpsilonBQPCadastrarQuestao,
    UsuarioEpsilonBQPListarQuestao,
    UsuarioEpsilonBQPEditarQuestao,
)

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

router = SimpleRouter()

router.register('api/v1/usuario/filiacao', FiliacaoViewSet)
router.register('api/v1/usuario', UsuarioViewSet)
router.register('api/v1/imprimir', ImprimirViewSet)

urlpatterns = [
    #############################################################
    #                  Usuario nao autenticado                  #
    #############################################################

    path('api/v1/token/getorcreate/', views.get_or_create_token, name='get_or_create_token'),

    path('usuario/criar_conta/', UsuarioCriarConta.as_view(), name='criar_conta'),

    path('usuario/criar_conta/concluido/', UsuarioEntrarConcluido.as_view(), name='criar_conta_concluido'),

    path('usuario/entrar/', auth_views.LoginView.as_view(
        template_name='usuario/templates/registration/entrar.html',
        success_url='concluido/'
    ), name='usuario_entrar', ),

    path('usuario/entrar/concluido/',
         UsuarioEntrarConcluido.as_view(),
         name='usuario_entrar_concluido'),

    path('usuario/redefinicao_de_senha/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/redefinicao_de_senha.html',
             email_template_name='registration/redefinicao_de_senha_email.html',
             success_url='concluido/',
             from_email='no-reply@bq.mat.br'
         ), name='redefinicao_de_senha'
         ),
    # envia para o email da pessoa um link para ela clicar
    path('usuario/redefinicao_de_senha/concluido/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/redefinicao_de_senha_concluido.html'
         ), name='redefinicao_de_senha_concluido'
         ),
    # quando a pessoa clica nolink, ela recai nesta pagina
    path('usuario/redefinicao_de_senha/<slug:uidb64>/<slug:token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/redefinicao_de_senha_confirmacao.html',
             success_url='concluido/'
         ), name='redefinicao_de_senha_confirmacao'
         ),

    # envia para o email da pessoa um link para ela clicar
    path('usuario/redefinicao_de_senha/<slug:uidb64>/<slug:token>/concluido/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/redefinicao_de_senha_confirmacao_concluido.html'
         ), name='redefinicao_de_senha_confirmacao_concluido'
         ),

    path('usuario/sair/', auth_views.LogoutView.as_view(next_page='/'), name='usuario_sair'),

    path('usuario/', UsuarioEntrarConcluido.as_view(), name='usuario'),

    #############################################################
    #              Usuario com nivel de acesso Alfa             #
    #############################################################

    path('usuario/alfa/', UsuarioAlfaInicio.as_view(),
         name='usuario_alfa_inicio'),

    path('usuario/alfa/configuracao/',
         UsuarioAlfaConfiguracao.as_view(),
         name='usuario_alfa_configuracao'),

    path('usuario/alfa/manual/',
         UsuarioAlfaManual.as_view(),
         name='usuario_alfa_manual'),

    path('usuario/alfa/ir_para/',
         UsuarioAlfaIrPara.as_view(),
         name='usuario_alfa_ir_para'),

    path('usuario/alfa/cadastrar/usuario/beta/',
         UsuarioAlfaCadastrarUsuarioBeta.as_view(),
         name='usuario_alfa_cadastrar_usuario_beta'),

    path('usuario/alfa/listar/usuario/beta/',
         UsuarioAlfaListarUsuarioBeta.as_view(),
         name='usuario_alfa_listar_usuario_beta'),


    path('usuario/alfa/detalhes/usuario/beta/',
         UsuarioAlfaDetalhesUsuarioBeta.as_view(),
         name='usuario_alfa_detalhes_usuario_beta'),


    path('usuario/alfa/editar/usuario/beta/',
         UsuarioAlfaEditarUsuarioBeta.as_view(),
         name='usuario_alfa_editar_usuario_beta'),

    #############################################################
    #              Usuario com nivel de acesso Beta             #
    #############################################################


    path('usuario/beta/', UsuarioBetaInicio.as_view(), name='usuario_beta_inicio'),


    path('usuario/beta/configuracao/', UsuarioBetaConfiguracao.as_view(), name='usuario_beta_configuracao'),


    path('usuario/beta/ir_para/',
         UsuarioBetaIrPara.as_view(),
         name='usuario_beta_ir_para'),


    path('usuario/beta/manual/',
         UsuarioBetaManual.as_view(),
         name='usuario_beta_manual'),

    path('usuario/beta/listar/usuario/gama/',
         UsuarioBetaListarUsuarioGama.as_view(),
         name='usuario_beta_listar_usuario_gama'),


    path('usuario/beta/cadastrar/usuario/gama/',
         UsuarioBetaCadastrarUsuarioGama.as_view(),
         name='usuario_beta_cadastrar_usuario_gama'),


    path('usuario/beta/detalhes/usuario/gama/',
         UsuarioBetaDetalhesUsuarioGama.as_view(),
         name='usuario_beta_detalhes_usuario_gama'),


    path('usuario/beta/editar/usuario/gama/',
         UsuarioBetaEditarUsuarioGama.as_view(),
         name='usuario_beta_editar_usuario_gama'),


    path('usuario/beta/cadastrar/etapa/',
         UsuarioBetaCadastrarEtapa.as_view(),
         name='usuario_beta_cadastrar_etapa'),

    path('usuario/beta/listar/etapa/',
         UsuarioBetaListarEtapa.as_view(),
         name='usuario_beta_listar_etapa'),


    path('usuario/beta/editar/etapa/',
         UsuarioBetaEditarEtapa.as_view(),
         name='usuario_beta_editar_etapa'),


    path('usuario/beta/cadastrar/unidade_tematica/',
         UsuarioBetaCadastrarUnidadeTematica.as_view(),
         name='usuario_beta_cadastrar_unidade_tematica'),

    path('usuario/beta/listar/unidade_tematica/',
         UsuarioBetaListarUnidadeTematica.as_view(),
         name='usuario_beta_listar_unidade_tematica'),


    path('usuario/beta/editar/unidade_tematica/',
         UsuarioBetaEditarUnidadeTematica.as_view(),
         name='usuario_beta_editar_unidade_tematica'),


    path('usuario/beta/cadastrar/objeto_de_conhecimento/',
         UsuarioBetaCadastrarObjetoDeConhecimento.as_view(),
         name='usuario_beta_cadastrar_objeto_de_conhecimento'),


    path('usuario/beta/listar/objeto_de_conhecimento/',
         UsuarioBetaListarObjetoDeConhecimento.as_view(),
         name='usuario_beta_listar_objeto_de_conhecimento'),


    path('usuario/beta/editar/objeto_de_conhecimento/',
         UsuarioBetaEditarObjetoDeConhecimento.as_view(),
         name='usuario_beta_usuario_editar_objeto_de_conhecimento'),


    path('usuario/beta/cadastrar/nivel_de_dificuldade/',
         UsuarioBetaCadastrarNivelDeDificuldade.as_view(),
         name='usuario_beta_cadastrar_nivel_de_dificuldade'),

    path('usuario/beta/listar/nivel_de_dificuldade/',
         UsuarioBetaListarNivelDeDificuldade.as_view(),
         name='usuario_beta_listar_nivel_de_dificuldade'),


    path('usuario/beta/editar/nivel_de_dificuldade/',
         UsuarioBetaEditarNivelDeDificuldade.as_view(),
         name='usuario_beta_usuario_editar_nivel_de_dificuldade'),

    #############################################################
    #              Usuario com nivel de acesso Gama             #
    #############################################################

    path('usuario/gama/',
         UsuarioGamaInicio.as_view(),
         name='usuario_gama_inicio'),

    path('usuario/gama/configuracao/',
         UsuarioGamaConfiguracao.as_view(),
         name='usuario_gama_configuracao'),

    path('usuario/gama/ir_para/',
         UsuarioGamaIrPara.as_view(),
         name='usuario_gama_ir_para'),

    path('usuario/gama/manual/',
         UsuarioGamaManual.as_view(),
         name='usuario_gama_manual'),

    path('usuario/gama/cadastrar/usuario/delta/',
         UsuarioGamaCadastrarUsuarioDelta.as_view(),
         name='usuario_gama_cadastrar_usuario_delta'),

    path('usuario/gama/listar/usuario/delta/',
         UsuarioGamaListarUsuarioDelta.as_view(),
         name='usuario_gama_listar_usuario_delta'),

    path('usuario/gama/detalhes/usuario/delta/',
         UsuarioGamaDetalhesUsuarioDelta.as_view(),
         name='usuario_gama_detalhes_usuario_delta'),

    path('usuario/gama/editar/usuario/delta/',
         UsuarioGamaEditarUsuarioDelta.as_view(),
         name='usuario_gama_editar_usuario_delta'),

    path('usuario/gama/revisar/questao/',
         UsuarioGamaRevisarQuestao.as_view(),
         name='usuario_gama_revisar_questao'),

    path('usuario/gama/listar/questao/',
         UsuarioGamaListarQuestao.as_view(),
         name='usuario_gama_listar_questao'),

    path('usuario/gama/listar/questao/<slug:uid>/',
         UsuarioGamaListarQuestaoUID.as_view(),
         name='usuario_gama_listar_questao_uid'),

    #############################################################
    #              Usuario com nivel de acesso Delta            #
    #############################################################

    path('usuario/delta/', UsuarioDeltaInicio.as_view(), name='usuario_delta_inicio'),

    path('usuario/delta/configuracao/',
         UsuarioDeltaConfiguracao.as_view(),
         name='usuario_delta_configuracao'),

    path('usuario/delta/manual/', UsuarioDeltaManual.as_view(), name='usuario_delta_manual'),

    path('usuario/delta/cadastrar/questao/',
         UsuarioDeltaCadastrarQuestao.as_view(),
         name='usuario_delta_cadastrar_questao'),

    path('usuario/delta/listar/questao/',
         UsuarioDeltaListarQuestao.as_view(),
         name='usuario_delta_listar_questao'),

    path('usuario/delta/editar/questao/',
         UsuarioDeltaEditarQuestao.as_view(),
         name='usuario_delta_editar_questao'),

    #############################################################
    #            Usuario com nivel de acesso Epsilon            #
    #############################################################

    path('usuario/epsilon/', UsuarioEpsilonInicio.as_view(), name='usuario_epsilon_inicio'),

    path('usuario/epsilon/configuracao/', UsuarioEpsilonConfiguracao.as_view(), name='usuario_epsilon_configuracao'),

    path('usuario/epsilon/gerar/avaliacao/', UsuarioEpsilonGerarAvaliacao.as_view(),
         name='usuario_epsilon_gerar_avaliacao'),

    path('usuario/epsilon/gerar/avaliacao/visualizar/', UsuarioEpsilonGerarAvaliacaoVisualizar.as_view(),
         name='usuario_epsilon_gerar_avaliacao_visualizar'),

    path('usuario/epsilon/imprimir/avaliacao/', UsuarioEpsilonImprimirAvaliacao.as_view(),
         name='usuario_epsilon_imprimir_avaliacao'),

    path('usuario/epsilon/manual/', UsuarioEpsilonManual.as_view(), name='usuario_epsilon_manual'),

    path('usuario/epsilon/bqp/', UsuarioEpsilonBQP.as_view(), name='usuario_epsilon_bqp'),

    path('usuario/epsilon/bqp/cadastrar/questao/', UsuarioEpsilonBQPCadastrarQuestao.as_view(),
         name='usuario_epsilon_bqp_cadastrar_questao'),

    path('usuario/epsilon/bqp/listar/questao/', UsuarioEpsilonBQPListarQuestao.as_view(),
         name='usuario_epsilon_bqp_listar_questao'),

    path('usuario/epsilon/bqp/editar/questao/', UsuarioEpsilonBQPEditarQuestao.as_view(),
         name='usuario_epsilon_bqp_editar_questao'),

]

urlpatterns += router.urls
