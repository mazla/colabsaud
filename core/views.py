from django.shortcuts import render
from hub.models import Topico

def homepage(request):
    # Coleta todos os tópicos armazenados no banco de dados
    todos_topicos = Topico.objects.all()
    
    # Envia os tópicos diretamente para a tela visual index.html
    return render(request, 'index.html', {'topicos': todos_topicos})