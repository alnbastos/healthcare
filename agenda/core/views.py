from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from core.models import UserProfile

# Create your views here.


def cadatro_user(requisicao):
    if requisicao.POST:
        nome = requisicao.POST.get('nome')
        data_nasc = requisicao.POST.get('data_nasc')
        sexo = requisicao.POST.get('sexo')
        cpf = requisicao.POST.get('cpf')
        endereco = requisicao.POST.get('endereco')
        telefone = requisicao.POST.get('telefone')
        email = requisicao.POST.get('email')
        pass_user = requisicao.POST.get('pass_user')
        user = User.objects.create_user(email, '', pass_user)  # criar usuário
        user_profile = UserProfile.objects.create(nome=nome,
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
    return render(requisicao, 'cadastramento.html')
