from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    EtapaViewSet,
    UnidadeTematicaViewSet,
    ObjetoDeConhecimentoViewSet,
    NivelDeDificuldadeViewSet,
    QuestaoViewSet
)

from . import views

#############################################################
#                     Usuario autenticado                   #
#############################################################
router = SimpleRouter()
router.register('api/v1/etapa', EtapaViewSet)
router.register('api/v1/unidadetematica', UnidadeTematicaViewSet)
router.register('api/v1/objetodeconhecimento', ObjetoDeConhecimentoViewSet)
router.register('api/v1/niveldedificuldade', NivelDeDificuldadeViewSet)
router.register('api/v1/questao', QuestaoViewSet)
#############################################################
#                  Usuario nao autenticado                  #
#############################################################

"""
urlpatterns = [
    path('questao/contagem/questao/',
        views.contagem_questao,
        name='contagem_questao'
    ),
    path('questao/contagem/questao/status/2/',
        views.contagem_questao_status_2,
        name='contagem_questao_status_2'
    ),
    path('questao/contagem/imprimir/',
        views.contagem_imprimir,
        name='contagem_imprimir'
    ),
    path('questao/listar/etapas/',
        views.listar_etapas,
        name='listar_etapas'
    ),
    path('questao/listar/anos/<int:etapa>/',
        views.listar_anos,
        name='listar_anos'
    ),
    path('questao/listar/unidadetematica/<int:etapa>/<int:ano>/',
        views.listar_unidades_tematicas,
        name='listar_unidades_tematicas'
    ),
    path('questao/listar/objetodeconhecimento/<int:etapa>/<int:ano>/<int:unidade_tematica>/',
        views.listar_objetos_de_conhecimento,
        name='listar_objetos_de_conhecimento'
    ),
    path('questao/listar/niveldedificuldade/',
        views.listar_niveis_de_dificuldade,
        name='listar_niveis_de_dificuldade'
    ),
    path('questao/listar/usuario/<int:id_u>/',
        views.listar_usuario,
        name='listar_usuario'
    ),
]

urlpatterns += router.urls

"""

urlpatterns = []
urlpatterns += router.urls