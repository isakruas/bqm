from rest_framework import mixins
from rest_framework import viewsets
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response

from .models import (
    Upload
)

from .serializers import (
    UploadSerializer
)
 
class UploadViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """API Upload V1.0.0"""
    # permission_classes = (UsuarioPermissions,)

    queryset = Upload.objects.all()
    serializer_class = UploadSerializer