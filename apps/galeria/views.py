from django.shortcuts import render, get_object_or_404, redirect ## renderiza na tela
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForms


def index(request): ## função que faz a requisição do que ira aparecer na tela
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) ## Só vai colocar na tela inicial os items que tem a configuração true no banco de dados
    
    return render(request, 'galeria/index.html', {"cards" : fotografias}) ## usamos a função para direcionar ao arquivo que contem o html (no caso o nosso está dentro da pasta templates)

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) ## Metôdo do django que se não encontrar retorna o erro 404
    return render(request, 'galeria/imagem.html', {"fotografia" : fotografia}) ## Faz a requisição para retornar a imagem que foi clicada

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')


    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance = fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form' : form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})