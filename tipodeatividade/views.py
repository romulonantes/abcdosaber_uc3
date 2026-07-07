from django.shortcuts import render, redirect
from tipodeatividade.models import TipoDeAtividade


def listar(request):

    lista_tiposdeatividade = TipoDeAtividade.objects.all()

    contexto = {
        'tiposdeatividade': lista_tiposdeatividade
    }

    return render(
        request,
        'tipodeatividade/listarTiposAtividade.html',
        context=contexto
    )


def cadastrar(request):

    if request.method == 'POST':

        descricao = request.POST.get('descricao')

        TipoDeAtividade.objects.create(
            descricao=descricao
        )

        return redirect('tipodeatividade:listar')

    return render(
        request,
        'tipodeatividade/cadastroTipoAtividade.html'
    )


def carregar(request, codigo):

    tipodeatividade = TipoDeAtividade.objects.get(pk=codigo)

    if request.method == 'POST':

        tipodeatividade.descricao = request.POST.get('descricao')
        tipodeatividade.save()

        return redirect('tipodeatividade:listar')

    contexto = {
        'tipodeatividade': tipodeatividade
    }

    return render(
        request,
        'tipodeatividade/cadastroTipoAtividade.html',
        contexto
    )


def excluir(request, codigo):

    try:
        tipodeatividade = TipoDeAtividade.objects.get(pk=codigo)
        tipodeatividade.delete()

    except TipoDeAtividade.DoesNotExist:
        pass

    return redirect('tipodeatividade:listar')