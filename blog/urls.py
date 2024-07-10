from django.urls import path
from .views import UploadViewSet,get_items
from django.conf import settings
from django.conf.urls.static import static




from django.urls import path, include
from rest_framework import routers
from .views import UploadViewSet

router = routers.DefaultRouter()
router.register(r'filter', UploadViewSet, basename="filter")

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
    path("data/",get_items)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)