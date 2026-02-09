from django.urls import path
from .views import SaralanganListCreateApiView



urlpatterns = [
    path('saralangan/', '  SaralanganListCreateApiView'.as_view()),

]