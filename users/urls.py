from django.urls import path
from .views import UsersListCreateApiView



urlpatterns = [
    path('user/', UsersListCreateApiView.as_view()),

]