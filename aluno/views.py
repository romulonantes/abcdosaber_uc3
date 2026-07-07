from django.shortcuts import render, redirect, get_object_or_404

from .models import Aluno


def cadastrar_aluno(request):

    if request.method == "POST":

        nome = request.POST.get("nome")

        Aluno.objects.create(
            nome=nome
        )

        return redirect("listar_alunos")

    return render(request, 'aluno/cadastroAluno.html')



def listar_alunos(request):

    alunos = Aluno.objects.all()

    return render(request, 'aluno/listarAlunos.html', {
        'alunos': alunos
    })



def editar_aluno(request, id):

    aluno = get_object_or_404(Aluno, pk=id)

    if request.method == "POST":

        aluno.nome = request.POST.get("nome")
        aluno.save()

        return redirect("listar_alunos")


    return render(request, 'aluno/cadastroAluno.html', {
        'aluno': aluno
    })



def excluir_aluno(request, id):

    aluno = get_object_or_404(Aluno, pk=id)

    aluno.delete()

    return redirect("listar_alunos")