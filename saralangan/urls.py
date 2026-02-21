from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaralanganViewSet

router = DefaultRouter()
router.register(r'', SaralanganViewSet)

urlpatterns = [path('', include(router.urls))]