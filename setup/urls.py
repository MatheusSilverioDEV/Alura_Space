from django.contrib import admin
from django.urls import path, include ## include usado para incluir outro arquivo para executar a função
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.galeria.urls')), # inclui a urls.py dentro da galeria para melhores praticas 
    path('', include('apps.usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ## adiciona um caminho para imagens para abrir os documentos do computador
 
