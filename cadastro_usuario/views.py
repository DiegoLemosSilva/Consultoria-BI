# views.py
from django.shortcuts import render, redirect
from .models import model_db_CheckinI,model_db_cardapio,upload_photo_chekin
from .forms import PhotoFormCheckin
from django.contrib import messages  # Importando o sistema de mensagens
from django.http import HttpResponse

def checkin (request):

    

    if request.method == 'GET':

        tipo = request.GET.get('tipo', '')
        tipo_servico = request.GET.get('nome_tipo_servico', '')
        nome_canal = request.GET.get('canal', '')
        ListCheckinI = model_db_CheckinI.get_by_instalacao(tipo,tipo_servico,nome_canal,'','')
        campanhas = ListCheckinI.values('nome_campanha').distinct()
                
           
        nome_campanha = request.GET.get('nome_campanha', 'default')
        produto = request.GET.get('produto', '')
            

        if produto == 'All' :           
            chekin = model_db_CheckinI.get_by_instalacao(tipo,tipo_servico,nome_canal,nome_campanha,'')
        else:
            chekin = model_db_CheckinI.get_by_instalacao(tipo,tipo_servico,nome_canal,nome_campanha,produto)
                # Obtém todos os registros do modelo Escrito

        context = {
            'ListCheckinI':ListCheckinI,
            'tipo_servico':tipo_servico,
            'chekin': chekin,
            'nome_campanha':nome_campanha,
            'nome_produto':produto,
            'campanhas':campanhas,
            'tipo':tipo,
            'nome_canal':nome_canal
            
            
            }
        return render(request, 'Instalacao.html', context)

def cad_projetos(request):
    # Verifica o valor do botão avançar
    btn_avancar = int(request.POST.get('Avancar', 1))
    todos_os_cardapios = model_db_cardapio.objects.all()
    pecas = todos_os_cardapios.values('peca').distinct()
    total = 1
    # Contexto inicial
    context = {
        'btn_avancar': btn_avancar,
        'todos_os_cardapios':todos_os_cardapios,
        'pecas':pecas,
    }

    if request.method == 'POST':
        if btn_avancar == 1:
            # Etapa 2: Recebe dados e atualiza o contexto
            nome_projeto = request.POST.get('nome_projeto', '')
            canal_selecionado = request.POST.get('canal', '')
            redes_selecionadas = request.POST.getlist('list')
            

            context.update({
                'nome_projeto': nome_projeto,
                'canal_selecionado': canal_selecionado,
                'redes_selecionadas': redes_selecionadas,
                'todos_os_cardapios':todos_os_cardapios,
                'pecas':pecas,
            })
            return render(request, 'Cadastro_Projeto.html', context)
        
        elif btn_avancar == 2:
            # Etapa 2: Recebe dados e atualiza o contexto
            nome_projeto = request.POST.get('nome_projeto', '')
            canal_selecionado = request.POST.get('canal', '')
            redes_selecionadas = request.POST.getlist('list')
            materiais = request.POST.getlist('materiais')
            context.update({
                'nome_projeto': nome_projeto,
                'canal_selecionado': canal_selecionado,
                'redes_selecionadas': redes_selecionadas,
                'todos_os_cardapios':todos_os_cardapios,
                'materiais':materiais,
            })
            return render(request, 'Cadastro_Projeto.html', context)

        
    
    # Se o método não for POST ou não cair em nenhuma condição
    return render(request, 'Cadastro_Projeto.html', context)
        

def cad_campanha(request):
    # Verifica o valor do botão avançar
    btn_avancar = int(request.POST.get('Avancar', 1))
    todos_os_cardapios = model_db_cardapio.objects.all()
    pecas = todos_os_cardapios.values('peca').distinct()
    # Contexto inicial
    context = {
        'btn_avancar': btn_avancar,
        'todos_os_cardapios':todos_os_cardapios,
        'pecas':pecas,
    }

    if request.method == 'POST':
        if btn_avancar == 1:
            # Etapa 2: Recebe dados e atualiza o contexto
            nome_projeto = request.POST.get('nome_projeto', '')
            canal_selecionado = request.POST.get('canal', '')
            redes_selecionadas = request.POST.getlist('list')
            

            context.update({
                'nome_projeto': nome_projeto,
                'canal_selecionado': canal_selecionado,
                'redes_selecionadas': redes_selecionadas,
                'todos_os_cardapios':todos_os_cardapios,
                'pecas':pecas,
            })
            return render(request, 'Cadastro_Campanha.html', context)
        
        elif btn_avancar == 2:
            # Etapa 2: Recebe dados e atualiza o contexto
            nome_projeto = request.POST.get('nome_projeto', '')
            canal_selecionado = request.POST.get('canal', '')
            redes_selecionadas = request.POST.getlist('list')
            materiais = request.POST.getlist('materiais')
            context.update({
                'nome_projeto': nome_projeto,
                'canal_selecionado': canal_selecionado,
                'redes_selecionadas': redes_selecionadas,
                'todos_os_cardapios':todos_os_cardapios,
                'materiais':materiais,
            })
            return render(request, 'Cadastro_Campanha.html', context)        
    
    # Se o método não for POST ou não cair em nenhuma condição
    return render(request, 'Cadastro_Campanha.html', context)          
        

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoFormCheckin(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = PhotoFormCheckin()
    return render(request, 'uploadcheckin.html', {'form': form})     
        
            

        

        

            
    
    """ if 'form1' in request.GET:
        context = {
            'form': form,
            'chekin': chekin,
            'nome_campanha':nome_campanha,
            'nome_produto':produto,
            'active':status,
            }
        return render(request, 'Instalacao.html', context)
    elif 'form2' in request.GET:
        # Lógica para o Formulário 2
        pass """
        
        


    

   