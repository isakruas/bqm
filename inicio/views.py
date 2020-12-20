from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

class Inicio(TemplateView):
	template_name = 'inicio.html'

class Redirecionar():
	
	def para_entrar(url):
		return redirect('/usuario/entrar/')

	def para_criar_conta(url):
		return redirect('/usuario/criar_conta/')

	def para_redefinicao_de_senha(url):
		return redirect('/usuario/redefinicao_de_senha/')

class Política_de_privacidade(TemplateView):
	template_name = 'inicio/templates/política_de_privacidade.html'

class Sobre(TemplateView):
	template_name = 'inicio/templates/sobre.html'

class Ir_para(TemplateView):
	template_name = 'inicio/templates/ir_para.html'