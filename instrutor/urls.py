from django.urls import path
from . import views

app_name = 'instrutor'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.cadastrar, name='cadastrar'),
    path('carregar/<int:id>/', views.carregar, name='carregar_instrutor'),
    path('excluir/<int:id>/', views.excluir, name='excluir_instrutor'),
]