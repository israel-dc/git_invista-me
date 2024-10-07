from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def novo_usuario(request):
    # tipo, validar, informar, salvar
    if request.method == 'POST':  # Criando um novo usuário
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O ususário {
                             usuario} foi criado com sucesso!')
            return redirect('login')
    else:  # Caso seja um novo usuário
        formulario = UserRegisterForm()

    return render(request, "usuarios/registrar.html", {'formulario': formulario})
