from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from rest_framework.documentation import include_docs_urls
from usuario.views import UsuarioObtainAuthToken
from django.template import loader
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@require_GET
def app_js(request):
    template = loader.get_template(os.path.join(BASE_DIR + '/templates/app.js'))
    return HttpResponse(template.render({}, request), content_type="text/javascript", charset="utf-8")


@require_GET
def manifest_json(request):
    template = loader.get_template(os.path.join(BASE_DIR + '/templates/manifest.json'))
    return HttpResponse(template.render({}, request), content_type="text/json", charset="utf-8")


@require_GET
def offline(request):
    template = loader.get_template(os.path.join(BASE_DIR + '/templates/offline.html'))
    return HttpResponse(template.render({}, request), content_type="text/html", charset="utf-8")


@require_GET
def robots_txt(request):
    template = loader.get_template(os.path.join(BASE_DIR + '/templates/robots.txt'))
    return HttpResponse(template.render({}, request), content_type="text/html", charset="utf-8")


@require_GET
def sw_js(request):
    template = loader.get_template(os.path.join(BASE_DIR + '/templates/serviceworker.js'))
    return HttpResponse(template.render({}, request), content_type="text/javascript", charset="utf-8")


@require_GET
def sitemap_xml(request):
    template = loader.get_template(os.path.join(BASE_DIR + '/templates/sitemap.xml'))
    return HttpResponse(template.render({}, request), content_type="text/xml", charset="utf-8")


@require_GET
def csrf(request):
    template = loader.get_template(os.path.join(BASE_DIR + '/templates/csrf.html'))
    return HttpResponse(template.render({}, request), content_type="text/json", charset="utf-8")


urlpatterns = [

    path('api/docs/', include_docs_urls(title='BQM: APIs Docs', public=False)),
    re_path('app.js', app_js),
    re_path('offline/', offline),
    path('manifest.json', manifest_json),
    path('sw.js', sw_js),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap_xml),
    path('api/v1/token/csrf/', csrf),
    path('api/v1/token/', UsuarioObtainAuthToken.as_view()),
    path('admin/', admin.site.urls),
    path('', include('questao.urls')),
    path('', include('usuario.urls')),
    path('', include('inicio.urls')),
    path('', include('upload.urls')),
    path('auth/', include('rest_framework.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
