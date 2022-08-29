from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita


# from django.http import HttpResponse # importar HttpResponse

def index(request):
    # return HttpResponse('<h1>TESTE</h1>') #  Cada view é responsável por devolver um objeto HttpResponse.
    receitas = Receita.objects.all()

    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)  # renderizar index.html (exibir uma página web)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }

    return render(request, 'receita.html', receita_a_exibir)
