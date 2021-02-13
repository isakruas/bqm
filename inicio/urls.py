from django.urls import path
from .views import Inicio, Política_de_privacidade, Sobre, Ir_para, Redirecionar

urlpatterns = [
	
	path('', Inicio.as_view(), name='inicio'),
	
	path('politica_de_privacidade/', Política_de_privacidade.as_view(), name='politica_de_privacidade'),
	
	path('sobre/', Sobre.as_view(), name='sobre'),
	
	path('ir_para/', Ir_para.as_view(), name='ir_para'),
	
		path('redirect/entrar/',Redirecionar.para_entrar, name='ir_para_entrar'),
		path('redirect/criar_conta/',Redirecionar.para_criar_conta, name='ir_para_criar_conta'),
		path('redirect/redefinicao_de_senha/',Redirecionar.para_redefinicao_de_senha, name='ir_para_redefinicao_de_senha'),
]