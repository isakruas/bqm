from rest_framework.routers import SimpleRouter

from .views import (
    UploadViewSet
)

router = SimpleRouter()
router.register('api/v1/upload', UploadViewSet)

urlpatterns = []
urlpatterns += router.urls
