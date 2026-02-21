from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReklamaViewSet, IlovalarViewSet

router = DefaultRouter()
router.register(r'reklama', ReklamaViewSet)
router.register(r'ilova', IlovalarViewSet)

urlpatterns = [path('', include(router.urls))]