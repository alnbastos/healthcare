from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from core.models import UserProfile
from django.contrib import messages
from core.forms import CadastroUsuarioForm
# Create your views here.


def cadastro_user(requisicao):
    if requisicao.POST:
        nome = requisicao.POST.get('nome')
        data_nasc = requisicao.POST.get('data_nasc')
        sexo = requisicao.POST.get('sexo')
        cpf = requisicao.POST.get('cpf')
        endereco = requisicao.POST.get('endereco')
        telefone = requisicao.POST.get('telefone')
        email = requisicao.POST.get('email')
        pass_user = requisicao.POST.get('pass_user')
        form = CadastroUsuarioForm(requisicao.POST)
        if form.is_valid():
            email_existe = User.objects.filter(username=email).exists()
            cpf_existe = UserProfile.objects.filter(cpf=cpf).exists()
            if email_existe:
                messages.error(requisicao, 'E-mail já existente.')
            if cpf_existe:
                messages.error(requisicao, 'CPF já existente.')
            if not email_existe and not cpf_existe:
                user = User.objects.create_user(email, '', pass_user)  # criar usuário
                user_profile = UserProfile(nome=nome,
                                           data_nasc=data_nasc,
                                           sexo=sexo,
                                           cpf=cpf,
                                           endereco=endereco,
                                           telefone=telefone,
                                           email=email,
                                           user=user)
                user.save()
                user_profile.save()
                return HttpResponse('Foi salvo')
    else:
        form = CadastroUsuarioForm()
    return render(requisicao, 'cadastramento.html', context={'form': form})  # se for GET
