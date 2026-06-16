from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('listar/', views.listar_alunos, name='listar_alunos'),
]