from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produto

def index(request):
    print(dir(f"User: {request.user}"))

    if str(request.user) == 'AnonymousUser': #transformando em string
        teste = 'Usuario não Logado'
    else:
        teste = 'Usuario logado'

    produtos = Produto.objects.all()

    context = {
        'curso': 'Hello Word',
        'logado': teste,
        'produtos': produtos
    }

    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
   #prod = Produto.objects.get(id=id)

    prod = get_object_or_404(Produto, id=id)

    context = {
        'produto': prod,
    }

    return render(request, 'produto.html', context)

def error404(request, ex):
    tempate = loader.get_template('404.html')
    return HttpResponse(content=tempate.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    tempate = loader.get_template('404.html')
    return HttpResponse(content=tempate.render(), content_type='text/html; charset=utf8', status=500)
