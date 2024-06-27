
from django.contrib import admin
from django.urls import path
from .import views

app_name = "geralpistache"
urlpatterns = [
    path('',views.index,name='index'),
    path('addProdutos/',views.addProdutos,name='add'),
    path('addProdutos2/',views.addProdutos2,name='add_produto'),
    path('addReceita/',views.addReceita,name='add_receita'),
    path('lista_produto/',views.lista_produto,name='lista_produto'),
    path('lista_receita/',views.lista_receita,name='lista_receita'),
]


