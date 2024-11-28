# urls.py em cadastro_usuario
from django.urls import path
from . import views

urlpatterns = [
    
    path('instalacao/', views.instalacao, name='instalacao'),
    path('cadastro_projeto/', views.cad_projetos, name='cad_projetos'),
    

    
]
