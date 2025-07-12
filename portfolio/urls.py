from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('proyectos/', views.listaProyectos,name='listaProyectos'),
    path('proyectos/crear/', views.crear_proyectos, name='crear_proyecto'),
    path('proyectos/editar/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'),

]
