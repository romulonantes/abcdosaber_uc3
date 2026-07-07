from django.shortcuts import render, redirect
from instrutor.models import Instrutor
from titulo.models import Titulo


def listar(request):

    lista_instrutores = Instrutor.objects.all()

    contexto = {
        'instrutores': lista_instrutores
    }

    return render(
        request,
        'instrutor/listarInstrutores.html',
        context=contexto
    )


def cadastrar(request):

    titulos = Titulo.objects.all()

    if request.method == 'POST':

        codigo_titulo = request.POST.get('codigoTitulo')

        titulo = None
        if codigo_titulo and codigo_titulo != "0":
            titulo = Titulo.objects.get(pk=codigo_titulo)

        Instrutor.objects.create(
            nome=request.POST.get('nome'),
            rg=request.POST.get('rg'),
            data_nascimento=request.POST.get('dataNascimento'),
            ddd=request.POST.get('ddd'),
            telefone=request.POST.get('telefone'),
            codigo_titulo=titulo
        )

        return redirect('instrutor:listar')

    contexto = {
        'titulos': titulos
    }

    return render(
        request,
        'instrutor/cadastroInstrutor.html',
        contexto
    )


def carregar(request, id):

    instrutor = Instrutor.objects.get(pk=id)
    titulos = Titulo.objects.all()

    if request.method == 'POST':

        codigo_titulo = request.POST.get('codigoTitulo')

        titulo = None
        if codigo_titulo and codigo_titulo != "0":
            titulo = Titulo.objects.get(pk=codigo_titulo)

        instrutor.nome = request.POST.get('nome')
        instrutor.rg = request.POST.get('rg')
        instrutor.data_nascimento = request.POST.get('dataNascimento')
        instrutor.ddd = request.POST.get('ddd')
        instrutor.telefone = request.POST.get('telefone')
        instrutor.codigo_titulo = titulo

        instrutor.save()

        return redirect('instrutor:listar')

    contexto = {
        'instrutor': instrutor,
        'titulos': titulos
    }

    return render(
        request,
        'instrutor/cadastroInstrutor.html',
        contexto
    )


def excluir(request, id):

    try:
        instrutor = Instrutor.objects.get(pk=id)
        instrutor.delete()

    except Instrutor.DoesNotExist:
        pass

    return redirect('instrutor:listar')