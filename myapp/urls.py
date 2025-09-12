from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('mensajes/', views.mensajes_club, name = 'mensajes_club'),
    path('emociones/', views.mensajes_emociones, name = 'mensajes_emociones'),
    path('opinion_personal/', views.opinion_personal, name = 'opinion_personal'),
    path('nuevo/', views.nuevo_mensaje, name='nuevo_mensaje'),
    path('mostrar_mensaje/<int:pk>/', views.mostrar_mensaje, name = 'mostrar_mensaje')
]
