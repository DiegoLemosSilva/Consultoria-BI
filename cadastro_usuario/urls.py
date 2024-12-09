# urls.py em cadastro_usuario
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('checkin/', views.checkin, name='checkin'),
    path('cadastro_projeto/', views.cad_projetos, name='cad_projetos'),
    path('cadastro_campanha/', views.cad_campanha, name='cad_campanha'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('uploadPlanoAcao/', views.upload_excel_plano_acao, name='upload_excel_plano_acao'),
    path('bancoprecos/', views.bancoprecos, name='Banco_Precos'),
    
]
# Servir arquivos de mídia em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
