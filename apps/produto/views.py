from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto


def inicio(request):
    return render(request, 'produto/inicio.html')

def index_loja(request):

    produtos = Produto.objects.filter(tipo='mercado', estoque__gt=0)
    return render(request, 'produto/index_loja.html', {'produtos': produtos})


def index_estoque(request):

    produtos = Produto.objects.filter(tipo='estoque')
    return render(request, 'produto/index_estoque.html', {'produtos': produtos})

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '')
        preco = request.POST.get('preco', 0)
        estoque = request.POST.get('estoque', 0)
        tipo = request.POST.get('tipo', 'mercado')

        try:
            preco_val = float(preco)
        except ValueError:
            preco_val = 0.0

        try:
            estoque_val = int(estoque)
        except ValueError:
            estoque_val = 0

        Produto.objects.create(
            nome=nome,
            preco=preco_val,
            estoque=estoque_val,
            tipo=tipo
        )

        if tipo == 'mercado':
            return redirect('produto:index_loja')
        else:
            return redirect('produto:index_estoque')

    return render(request, 'produto/cadastrar.html')

def editar(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        produto.nome = request.POST.get('nome', '')

        try:
            produto.preco = float(request.POST.get('preco', 0))
        except ValueError:
            produto.preco = 0.0

        try:
            produto.estoque = int(request.POST.get('estoque', 0))
        except ValueError:
            produto.estoque = 0

        produto.tipo = request.POST.get('tipo', 'mercado')
        produto.save()

        if produto.tipo == 'mercado':
            return redirect('produto:index_loja')
        else:
            return redirect('produto:index_estoque')

    return render(request, 'produto/editar.html', {'produto': produto})


def excluir(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    tipo = produto.tipo  
    produto.delete()

    if tipo == 'mercado':
        return redirect('produto:index_loja')
    else:
        return redirect('produto:index_estoque')
