from rest_framework.routers import SimpleRouter
from .views import (
    EtapaViewSet,
    UnidadeTematicaViewSet,
    ObjetoDeConhecimentoViewSet,
    NivelDeDificuldadeViewSet,
    QuestaoViewSet
)
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

urlpatterns = []
urlpatterns += router.urls
