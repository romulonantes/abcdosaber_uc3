from django.shortcuts import render
from .models import Aluno

# Create your views here.
def cadastrar_aluno(request):
    return render(request, 'aluno/cadastroAluno.html')

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/listarAlunos.html', {'alunos': alunos})