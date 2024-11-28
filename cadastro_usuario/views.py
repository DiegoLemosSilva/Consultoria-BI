# views.py
from django.shortcuts import render, redirect
from .forms import CheckinI,model_db_campanha,model_db_cardapio
from django.contrib import messages  # Importando o sistema de mensagens
from django.http import HttpResponse

def instalacao (request):

    

    if request.method == 'GET':

        tipo = request.GET.get('tipo', '')
        
        campanha = model_db_campanha.get_by_campanha(tipo)         
            
        nome_campanha = request.GET.get('nome_campanha', '')
        produto = request.GET.get('produto', '')
            

        if produto == 'All':           
            chekin = CheckinI.get_by_instalacao('INSTALAÇÃO',nome_campanha,'')
        else:
            chekin = CheckinI.get_by_instalacao('INSTALAÇÃO',nome_campanha,produto)
                # Obtém todos os registros do modelo Escrito

        context = {
            'chekin': chekin,
            'nome_campanha':nome_campanha,
            'nome_produto':produto,
            'campanha':campanha,
            'tipo':tipo,
            
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
        'total':total,
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
                'total':total,
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
                'total':total,
                'todos_os_cardapios':todos_os_cardapios,
                'materiais':materiais,
            })
            return render(request, 'Cadastro_Projeto.html', context)

        elif btn_avancar == 3:
            pass
    
    # Se o método não for POST ou não cair em nenhuma condição
    return render(request, 'Cadastro_Projeto.html', context)
        

          
        

        
        
            

        

        

            
    
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
        
        


    

   