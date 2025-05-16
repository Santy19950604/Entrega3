from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('crear_autor/', views.crear_autor),
    path('crear_categoria/', views.crear_categoria),
    path('crear_post/', views.crear_post),
    path('buscar_post/', views.buscar_post),
]