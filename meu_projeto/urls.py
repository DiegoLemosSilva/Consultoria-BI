# urls.py em meu_projeto
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro_usuario.urls')),  # Inclui as URLs do app cadastro_usuario
]