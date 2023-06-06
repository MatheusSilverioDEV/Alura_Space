from django.contrib import admin

from apps.galeria.models import Fotografia 

class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada",) ## Para melhor vizualização na tela adm
    list_display_links = ("id", "nome",) ## Para poder clicar no atributo e acessar o objeto
    search_fields = ("nome",) ## adiciona os campos que quiser pesquisar, tem que colocar virgula no final.
    list_filter = ("categoria", "usuario") ## adiciona categorias
    list_per_page = 10
    list_editable = ("publicada",) ## ativa a checkbox direto para a função publicada

admin.site.register(Fotografia, ListandoFotografia) ## Importando banco de dados para tela admin

# Register your models here.
