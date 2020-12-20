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
    Redirecionar,
#############################################################
#              Usuario com nivel de acesso Alfa             #
#############################################################
    UsuarioAlfaInicio,
    UsuarioAlfaConfiguracao,
    UsuarioAlfaConfiguracaoExcluirConta,
    UsuarioAlfaManual,
    UsuarioAlfaIrPara,
    UsuarioAlfaCadastrarUsuarioBeta,
    UsuarioAlfaCadastrarFiliacao,
    UsuarioAlfaListarUsuarioGama,
    UsuarioAlfaListarUsuarioGamaDetalhes,
    UsuarioAlfaListarUsuarioDelta,
    UsuarioAlfaListarUsuarioDeltaDetalhes,
    UsuarioAlfaListarUsuarioBeta,
    UsuarioAlfaListarUsuarioBetaDetalhes,
#############################################################
#              Usuario com nivel de acesso Beta             #
#############################################################
    UsuarioBetaInicio,
    UsuarioBetaConfiguracao,
    UsuarioBetaConfiguracaoExcluirConta,
    UsuarioBetaManual,
    UsuarioBetaIrPara,
    UsuarioBetaListarEtapa,
    UsuarioBetaListarUnidadeTematica,
    UsuarioBetaListarObjetoDeConhecimento,
    UsuarioBetaListarNivelDeDificuldade,
    UsuarioBetaListarUsuarioGama,
    UsuarioBetaListarUsuarioGamaDetalhes,
    UsuarioBetaListarUsuarioDelta,
    UsuarioBetaListarUsuarioDeltaDetalhes,
    UsuarioBetaEditarEtapa,
    UsuarioBetaEditarUnidadeTematica,
    UsuarioBetaEditarObjetoDeConhecimento,
    UsuarioBetaEditarNivelDeDificuldade,
    UsuarioBetaCadastrarEtapa,
    UsuarioBetaCadastrarUnidadeTematica,
    UsuarioBetaCadastrarObjetoDeConhecimento,
    UsuarioBetaCadastrarNivelDeDificuldade,
    UsuarioBetaCadastrarUsuarioGama,
    UsuarioBetaCadastrarFiliacao,
#############################################################
#              Usuario com nivel de acesso Gama             #
#############################################################
    UsuarioGamaInicio,
    UsuarioGamaConfiguracao,
    UsuarioGamaConfiguracaoExcluirConta,
    UsuarioGamaManual,
    UsuarioGamaIrPara,
    UsuarioGamaCadastrarUsuarioDelta,
    UsuarioGamaListarUsuarioDelta,
    UsuarioGamaListarUsuarioDeltaDetalhes,
    UsuarioGamaCadastrarFiliacao,
    UsuarioGamaEditarQuestao,
    UsuarioGamaExcluirQuestao,
#############################################################
#              Usuario com nivel de acesso Delta            #
#############################################################
    UsuarioDeltaInicio,
    UsuarioDeltaConfiguracao,
    UsuarioDeltaManual,
    UsuarioDeltaCadastrarQuestao,
    UsuarioDeltaEditarQuestao,
    UsuarioDeltaExcluirQuestao,
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
from django.urls import path, include
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

    path('usuario/filiacao/superior/inferior/<int:id_u>/',
        views.UsuarioFiliacaoSuperiorInferior,
        name='usuario_filiacao_superior_inferior'
    ),

    path('usuario/filiacao/inferior/superior/<int:id_u>/',
        views.UsuarioFiliacaoInferiorSuperior,
        name='usuario_filiacao_inferior_superior'
    ),
	
    path('usuario/criar_conta/', UsuarioCriarConta.as_view(), name='criar_conta'),
	
    path('usuario/criar_conta/concluido/', Redirecionar.para_entrar, name='criar_conta_concluido'),
    
    path('usuario/entrar/', auth_views.LoginView.as_view(
        template_name = 'usuario/templates/registration/entrar.html',
        success_url='concluido/'
        ), name = 'usuario_entrar', ),
    
    path('usuario/entrar/concluido/',
        UsuarioEntrarConcluido.as_view(),
        name='usuario_entrar_concluido'),
    
    path('usuario/redefinicao_de_senha/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/redefinicao_de_senha.html',
            email_template_name = 'registration/redefinicao_de_senha_email.html',
            success_url='concluido/',
            from_email = 'no-reply@bq.mat.br'
        ), name='redefinicao_de_senha'
    ),
    #envia para o email da pessoa um link para ela clicar  
    path('usuario/redefinicao_de_senha/concluido/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/redefinicao_de_senha_concluido.html'
        ), name='redefinicao_de_senha_concluido'
    ),
    #quando a pessoa clica nolink, ela recai nesta pagina
    path('usuario/redefinicao_de_senha/<slug:uidb64>/<slug:token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/redefinicao_de_senha_confirmacao.html',
            success_url='concluido/'
        ), name='redefinicao_de_senha_confirmacao'
    ),

    #envia para o email da pessoa um link para ela clicar  
    path('usuario/redefinicao_de_senha/<slug:uidb64>/<slug:token>/concluido/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/redefinicao_de_senha_confirmacao_concluido.html'
        ), name='redefinicao_de_senha_confirmacao_concluido'
    ),



    
    path('usuario/sair/', auth_views.LogoutView.as_view(next_page = '/'), name = 'usuario_sair'),
    
    path('usuario/', Redirecionar.para_entrar_concluido, name='usuario'),

#############################################################
#              Usuario com nivel de acesso Alfa             #
#############################################################
    
    path('usuario/alfa/contagem/usuario/alfa/',

        views.usuario_alfa_contagem_usuario_alfa,
        name='usuario_alfa_contagem_usuario_alfa'
    ),
    
    path('usuario/alfa/contagem/usuario/beta/',
        views.usuario_alfa_contagem_usuario_beta,
        name='usuario_alfa_contagem_usuario_beta'
    ),
    
    path('usuario/alfa/contagem/usuario/gama/',
        views.usuario_alfa_contagem_usuario_gama,
        name='usuario_alfa_contagem_usuario_gama'
    ),
    
    path('usuario/alfa/contagem/usuario/delta/',
        views.usuario_alfa_contagem_usuario_delta,
        name='usuario_alfa_contagem_usuario_delta'
    ),
    
    path('usuario/alfa/contagem/usuario/epsilon/',
        views.usuario_alfa_contagem_usuario_epsilon,
        name='usuario_alfa_contagem_usuario_epsilon'
    ),
    
    path('usuario/alfa/', UsuarioAlfaInicio.as_view(),
        name='usuario_alfa_inicio'),
    
    path('usuario/alfa/configuracao/',
        UsuarioAlfaConfiguracao.as_view(),
        name='usuario_alfa_configuracao'),
    
    #path('usuario/alfa/configuracao/excluir_conta/<int:pk>/', UsuarioAlfaConfiguracaoExcluirConta.as_view(), name='usuario_alfa_configuracao_excluir_conta'),
    
    path('usuario/alfa/configuracao/modificar_senha/',
        auth_views.PasswordChangeView.as_view(
            template_name='usuario/templates/alfa/modificar_senha.html',
            success_url='concluido/'
        ),
    ),
    
    path('usuario/alfa/configuracao/modificar_senha/concluido/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='usuario/templates/alfa/modificar_senha_concluido.html'
        ),
    ),
    
    path('usuario/alfa/ir_para/',
        UsuarioAlfaIrPara.as_view(),
        name='usuario_alfa_ir_para'),
    
    path('usuario/alfa/manual/',
        UsuarioAlfaManual.as_view(),
        name='usuario_alfa_manual'),
    
    path('usuario/alfa/cadastrar/usuario/beta/',
        UsuarioAlfaCadastrarUsuarioBeta.as_view(),
        name='usuario_alfa_cadastrar_usuario_beta'),
    
    path('usuario/alfa/cadastrar/usuario/beta/concluido/',
        views.UsuarioAlfaCadastrarFiliacao,
        name='usuario_alfa_cadastrar_usuario_beta_concluido'),
    
    path('usuario/alfa/listar/usuario/beta/',
        UsuarioAlfaListarUsuarioBeta.as_view(),
        name='usuario_alfa_listar_usuario_beta'),
    
    path('usuario/alfa/listar/usuario/beta/detalhes/<int:id_u>/',
        views.UsuarioAlfaListarUsuarioBetaDetalhes,
        name='usuario_alfa_listar_usuario_beta_detalhes_pk'),
    
    path('usuario/alfa/listar/usuario/gama/',
        UsuarioAlfaListarUsuarioGama.as_view(),
        name='usuario_alfa_listar_usuario_gama'),
    
    path('usuario/alfa/listar/usuario/gama/detalhes/<int:id_u>/',
        views.UsuarioAlfaListarUsuarioGamaDetalhes,
        name='usuario_alfa_listar_usuario_gama_detalhes_pk'),
    
    path('usuario/alfa/listar/usuario/delta/',
        UsuarioAlfaListarUsuarioDelta.as_view(),
        name='usuario_alfa_listar_usuario_delta'),
    
    path('usuario/alfa/listar/usuario/delta/detalhes/<int:id_u>/',
        views.UsuarioAlfaListarUsuarioDeltaDetalhes,
        name='usuario_alfa_listar_usuario_delta_detalhes_pk'),
#############################################################
#              Usuario com nivel de acesso Beta             #
#############################################################
    
    path('usuario/beta/', UsuarioBetaInicio.as_view(), name='usuario_beta_inicio'),
    
    path('usuario/beta/configuracao/',  UsuarioBetaConfiguracao.as_view(), name='usuario_beta_configuracao'),
    
    #path('usuario/beta/configuracao/excluir_conta/<int:pk>/', UsuarioBetaConfiguracaoExcluirConta.as_view(), name='usuario_beta_configuracao_excluir_conta'),
    
    path('usuario/beta/configuracao/modificar_senha/',
        auth_views.PasswordChangeView.as_view(
            template_name='usuario/templates/beta/modificar_senha.html',
            success_url='concluido/'
        ),
    ),
    
    path('usuario/beta/configuracao/modificar_senha/concluido/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='usuario/templates/beta/modificar_senha_concluido.html'
        ),
    ),
    
    path('usuario/beta/ir_para/',
        UsuarioBetaIrPara.as_view(),
        name='usuario_beta_ir_para'),
    
    path('usuario/beta/manual/',
        UsuarioBetaManual.as_view(),
        name='usuario_beta_manual'),
    
    path('usuario/beta/listar/etapa/',
        views.UsuarioBetaListarEtapa,
        name='usuario_beta_listar_etapa'),
    
    path('usuario/beta/listar/unidade_tematica/',
        views.UsuarioBetaListarUnidadeTematica,
        name='usuario_beta_listar_unidade_tematica'),
    
    path('usuario/beta/listar/objeto_de_conhecimento/',
        views.UsuarioBetaListarObjetoDeConhecimento,
        name='usuario_beta_listar_objeto_de_conhecimento'),
    
    path('usuario/beta/listar/nivel_de_dificuldade/',
        views.UsuarioBetaListarNivelDeDificuldade,
        name='usuario_beta_listar_nivel_de_dificuldade'),
    
    path('usuario/beta/cadastrar/etapa/',
        UsuarioBetaCadastrarEtapa.as_view(),
        name='usuario_beta_cadastrar_etapa'),
    
    path('usuario/beta/cadastrar/etapa/concluido/',
        Redirecionar.para_usuario,
        name='usuario_beta_cadastrar_etapa_concluido'),
    
    path('usuario/beta/cadastrar/unidade_tematica/',
        UsuarioBetaCadastrarUnidadeTematica.as_view(),
        name='usuario_beta_cadastrar_unidade_tematica'),
    
    path('usuario/beta/cadastrar/unidade_tematica/concluido/',
        Redirecionar.para_usuario,
        name='usuario_beta_cadastrar_unidade_tematica_concluido'),
    
    path('usuario/beta/cadastrar/objeto_de_conhecimento/',
        UsuarioBetaCadastrarObjetoDeConhecimento.as_view(),
        name='usuario_beta_cadastrar_objeto_de_conhecimento'),
    
    path('usuario/beta/cadastrar/objeto_de_conhecimento/concluido/',
        Redirecionar.para_usuario,
        name='usuario_beta_cadastrar_objeto_de_conhecimento_concluido'),
    
    path('usuario/beta/cadastrar/nivel_de_dificuldade/',
        UsuarioBetaCadastrarNivelDeDificuldade.as_view(),
        name='usuario_beta_cadastrar_nivel_de_dificuldade'),
    
    path('usuario/beta/cadastrar/nivel_de_dificuldade/concluido/',
        Redirecionar.para_usuario,
        name='usuario_beta_cadastrar_nivel_de_dificuldade_concluido'),
    
    path('usuario/beta/editar/etapa/<int:pk>/',
        UsuarioBetaEditarEtapa.as_view(),
        name='usuario_beta_usuario_editar_etapa_pk'),
    
    path('usuario/beta/editar/etapa/concluido/',Redirecionar.para_usuario,
         name='usuario_beta_usuario_editar_etapa_concluido'),
    
    path('usuario/beta/editar/unidade_tematica/<int:pk>/',
        UsuarioBetaEditarUnidadeTematica.as_view(),
        name='usuario_beta_usuario_editar_unidade_tematica_pk'),
    
    path('usuario/beta/editar/unidade_tematica/concluido/',Redirecionar.para_usuario,
         name='usuario_beta_usuario_editar_unidade_tematica_concluido'),
    
    path('usuario/beta/editar/objeto_de_conhecimento/<int:pk>/',
        UsuarioBetaEditarObjetoDeConhecimento.as_view(),
        name='usuario_beta_usuario_editar_objeto_de_conhecimento_pk'),
    
    path('usuario/beta/editar/objeto_de_conhecimento/concluido/',Redirecionar.para_usuario,
         name='usuario_beta_usuario_editar_objeto_de_conhecimento_concluido'),
    
    path('usuario/beta/editar/nivel_de_dificuldade/<int:pk>/',
        UsuarioBetaEditarNivelDeDificuldade.as_view(),
        name='usuario_beta_usuario_editar_nivel_de_dificuldade_pk'),
    
    path('usuario/beta/editar/nivel_de_dificuldade/concluido/',Redirecionar.para_usuario,
         name='usuario_beta_usuario_editar_nivel_de_dificuldade_concluido'),
    
    path('usuario/beta/listar/usuario/gama/',
        UsuarioBetaListarUsuarioGama.as_view(),
        name='usuario_beta_listar_usuario_gama'),
    
    path('usuario/beta/listar/usuario/gama/detalhes/<int:id_u>/',
        views.UsuarioBetaListarUsuarioGamaDetalhes,
        name='usuario_beta_listar_usuario_gama_detalhes_pk'),
    
    path('usuario/beta/listar/usuario/delta/',
        UsuarioBetaListarUsuarioDelta.as_view(),
        name='usuario_beta_listar_usuario_delta'),
    
    path('usuario/beta/listar/usuario/delta/detalhes/<int:id_u>/',
        views.UsuarioBetaListarUsuarioDeltaDetalhes,
        name='usuario_beta_listar_usuario_delta_detalhes_pk'),
    
    path('usuario/beta/cadastrar/usuario/gama/',
        UsuarioBetaCadastrarUsuarioGama.as_view(),
        name='usuario_beta_cadastrar_usuario_gama'),
    
    path('usuario/beta/cadastrar/usuario/gama/concluido/',
        views.UsuarioBetaCadastrarFiliacao,
        name='usuario_beta_cadastrar_usuario_gama_concluido'),
#############################################################
#              Usuario com nivel de acesso Gama             #
#############################################################
    
    path('usuario/gama/', UsuarioGamaInicio.as_view(),
        name='usuario_gama_inicio'),
    
    path('usuario/gama/configuracao/', 
        UsuarioGamaConfiguracao.as_view(),
        name='usuario_gama_configuracao'),
    
    #path('usuario/gama/configuracao/excluir_conta/<int:pk>/', UsuarioGamaConfiguracaoExcluirConta.as_view(), name='usuario_gama_configuracao_excluir_conta'),
    
    path('usuario/gama/configuracao/modificar_senha/',
        auth_views.PasswordChangeView.as_view(
            template_name='usuario/templates/gama/modificar_senha.html',
            success_url='concluido/'
        ),
    ),
    
    path('usuario/gama/configuracao/modificar_senha/concluido/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='usuario/templates/gama/modificar_senha_concluido.html'
        ),
    ),
    
    path('usuario/gama/ir_para/', UsuarioGamaIrPara.as_view(), name='usuario_gama_ir_para'),
    
    path('usuario/gama/manual/', UsuarioGamaManual.as_view(), name='usuario_gama_manual'),
    
    path('usuario/gama/cadastrar/usuario/delta/',
        UsuarioGamaCadastrarUsuarioDelta.as_view(),
        name='usuario_gama_cadastrar_usuario_delta'),
    
    path('usuario/gama/cadastrar/usuario/delta/concluido/',
        views.UsuarioGamaCadastrarFiliacao,
        name='usuario_gama_cadastrar_usuario_delta_concluido'),
    
    path('usuario/gama/listar/usuario/delta/',
        UsuarioGamaListarUsuarioDelta.as_view(),
        name='usuario_gama_listar_usuario_delta'),
    
    path('usuario/gama/listar/usuario/delta/detalhes/<int:id_u>/',
        views.UsuarioGamaListarUsuarioDeltaDetalhes,
        name='usuario_gama_listar_usuario_delta_detalhes_pk'),
    
    path('usuario/gama/editar/questao/<int:pk>/',
        UsuarioGamaEditarQuestao.as_view(),
        name='usuario_gama_editar_questao_pk'),
    
    path('usuario/gama/editar/questao/concluido/',
        Redirecionar.para_usuario,
        name='usuario_gama_editar_questao_concluido'),
    
    path('usuario/gama/excluir/questao/<int:pk>/',
        UsuarioGamaExcluirQuestao.as_view(),
        name='usuario_gama_excluir_questao_pk'),
    
    path('usuario/gama/excluir/questao/concluido/',
        Redirecionar.para_usuario,
        name='usuario_gama_excluir_questao_concluido'),
#############################################################
#              Usuario com nivel de acesso Delta            #
#############################################################
    
    path('usuario/delta/', UsuarioDeltaInicio.as_view(), name='usuario_delta_inicio'),
    
    path('usuario/delta/configuracao/', 
        UsuarioDeltaConfiguracao.as_view(),
        name='usuario_delta_configuracao'),
    
    #path('usuario/delta/configuracao/excluir_conta/<int:pk>/', UsuarioDeltaConfiguracaoExcluirConta.as_view(), name='usuario_delta_configuracao_excluir_conta'),
    
    path('usuario/delta/configuracao/modificar_senha/',
        auth_views.PasswordChangeView.as_view(
            template_name='usuario/templates/delta/modificar_senha.html',
            success_url='concluido/'
        ),
    ),
    
    path('usuario/delta/configuracao/modificar_senha/concluido/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='usuario/templates/delta/modificar_senha_concluido.html'
        ),
    ),
    
    path('usuario/delta/manual/', UsuarioDeltaManual.as_view(), name='usuario_delta_manual'),
    
    path('usuario/delta/cadastrar/questao/',
        UsuarioDeltaCadastrarQuestao.as_view(),
        name='usuario_delta_cadastrar_questao'),
    
    path('usuario/delta/cadastrar/questao/concluido/',
        Redirecionar.para_usuario,
        name='usuario_delta_cadastrar_questao_concluido'),
    
    path('usuario/delta/editar/questao/<int:pk>/',
        UsuarioDeltaEditarQuestao.as_view(),
        name='usuario_delta_editar_questao_pk'),
    
    path('usuario/delta/editar/questao/concluido/',
        Redirecionar.para_usuario,
        name='usuario_delta_editar_questao_concluido'),
    
    path('usuario/delta/excluir/questao/<int:pk>/',
        UsuarioDeltaExcluirQuestao.as_view(),
        name='usuario_delta_excluir_questao_pk'),
    
    path('usuario/delta/excluir/questao/concluido/',
        Redirecionar.para_usuario,
        name='usuario_delta_excluir_questao_concluido'),
    
#############################################################
#            Usuario com nivel de acesso Epsilon            #
#############################################################

    path('usuario/epsilon/', UsuarioEpsilonInicio.as_view(), name='usuario_epsilon_inicio'),

    path('usuario/epsilon/configuracao/', UsuarioEpsilonConfiguracao.as_view(), name='usuario_epsilon_configuracao'),

    path('usuario/epsilon/gerar/avaliacao/', UsuarioEpsilonGerarAvaliacao.as_view(), name='usuario_epsilon_gerar_avaliacao'),

    path('usuario/epsilon/gerar/avaliacao/visualizar/', UsuarioEpsilonGerarAvaliacaoVisualizar.as_view(), name='usuario_epsilon_gerar_avaliacao_visualizar'),

    path('usuario/epsilon/imprimir/avaliacao/', UsuarioEpsilonImprimirAvaliacao.as_view(), name='usuario_epsilon_imprimir_avaliacao'),

    path('usuario/epsilon/manual/', UsuarioEpsilonManual.as_view(), name='usuario_epsilon_manual'),
 
    path('usuario/epsilon/bqp/', UsuarioEpsilonBQP.as_view(), name='usuario_epsilon_bqp'),

    path('usuario/epsilon/bqp/cadastrar/questao/', UsuarioEpsilonBQPCadastrarQuestao.as_view(), name='usuario_epsilon_bqp_cadastrar_questao'),

    path('usuario/epsilon/bqp/listar/questao/', UsuarioEpsilonBQPListarQuestao.as_view(), name='usuario_epsilon_bqp_listar_questao'),

    path('usuario/epsilon/bqp/editar/questao/', UsuarioEpsilonBQPEditarQuestao.as_view(), name='usuario_epsilon_bqp_editar_questao'),
 
]

 








urlpatterns += router.urls