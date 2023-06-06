from django.urls import path
from apps.galeria.views import index, imagem, buscar, nova_imagem, deletar_imagem, editar_imagem, filtro

urlpatterns = [
        path('', index, name = 'index'), ## faz a requisição usando a função em views
        path('imagem/<int:foto_id>', imagem, name = 'imagem'), ## faz a requisição usando a função imagem em views, name = a gente consegue encaminhar para a url codando direto no html
        path("buscar", buscar, name="buscar"),
        path('nova-imagem', nova_imagem, name='nova_imagem'),
        path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
        path('deletar-imagem/<int:foto_id> ', deletar_imagem, name='deletar_imagem'),
        path('filtro/<str:categoria>', filtro, name='filtro'),
        

] 
