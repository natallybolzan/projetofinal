# filename: views.py
from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request,"geralpistache/base.html")

def addProdutos(request):
    return render(request,"geralpistache/addProduto.html")

def addProdutos2(request):
    if request.method=='POST':
        nome=request.POST.get('produto-nome')
        unidade_medida=request.POST.get('unidade-medida')
        quantidade=request.POST.get('quantidade')
        banco = Produto(nome=nome, unidade_medida=unidade_medida, quantidade=quantidade)
        banco.save()
    return render(request,"geralpistache/addProduto.html")

def addReceita(request):
    if request.method=='POST':
        nome=request.POST.get('receita-nome')
        data=request.POST.get('data')
        ingrediente=request.POST.getlist('recipe-ingredients[]')
        quantidade=request.POST.getlist('recipe-quantities[]')
        ingredientes_str = ','.join(ingrediente)
        quantidades_str = ','.join(quantidade)

        Receita.objects.create(nome_receita=nome, ingrediente_Nome=ingredientes_str, qt_ingre=quantidades_str,data=data)
    return render(request,"geralpistache/addProduto.html")


def lista_produto(request):
    produtos = Produto.objects.all()
    return render(request,"geralpistache/lista_produto.html",{'produtos':produtos})
    


def lista_receita(request):
    receitas = Receita.objects.all()
    receitas_completas = []
    for receita in receitas:
        ingredientes_lista = receita.ingrediente_Nome.split(',')
        quantidades_lista = receita.qt_ingre.split(',')
        receitas_completas.append({
            'nome': receita.nome_receita,
            'data': receita.data,
            'ingredientes': zip(ingredientes_lista, quantidades_lista)
        })
        
    return render(request, 'geralpistache/lista_receita.html', {'receitas': receitas_completas})
