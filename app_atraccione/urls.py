from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_atraccion, name='agregar_atraccion'),
    path('editar/<int:id>/', views.editar_atraccion, name='editar_atraccion'),
    path('borrar/<int:id>/', views.borrar_atraccion, name='borrar_atraccion'),
]