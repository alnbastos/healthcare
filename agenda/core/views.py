from django.http import HttpResponse
from django.shortcuts import render
from core.models import User, ClienteProfile, MedicoProfile, ClinicaProfile
from django.contrib import messages
from core.forms import CadastroUsuarioForm, CadastroMedicoForm


# Create your views here.


def cadastro_cliente(requisicao):
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
        print(data_nasc)
        if form.is_valid():
            email_existe = User.objects.filter(username=email).exists()
            cpf_existe = ClienteProfile.objects.filter(cpf=cpf).exists()
            if email_existe:
                messages.error(requisicao, 'E-mail já cadastrado.')
            if cpf_existe:
                messages.error(requisicao, 'CPF já cadastrado.')
            if not email_existe and not cpf_existe:
                user = User(username=email, password=pass_user, is_cliente=True)  # criar usuário
                user_profile = ClienteProfile(nome=nome,
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


def cadastro_medico(requisicao):
    if requisicao.POST:
        form = CadastroMedicoForm(requisicao.POST)
        nome = requisicao.POST.get('nome')
        crm = requisicao.POST.get('crm')
        especialidade = requisicao.POST.get('especialidade')
        telefone = requisicao.POST.get('telefone')
        cidade = requisicao.POST.get('cidade')
        clinica = form.cleaned_data['clinica'].user
        email = requisicao.POST.get('email')
        pass_user = requisicao.POST.get('pass_user')
        if form.is_valid():
            email_existe = User.objects.filter(username=email).exists()
            crm_existe = MedicoProfile.objects.filter(crm=crm).exists()
            if email_existe:
                messages.error(requisicao, 'E-mail já cadastrado.')
            if crm_existe:
                messages.error(requisicao, 'CRM já cadastrado.')
            if not email_existe and not crm_existe:
                user = User(username=email, password=pass_user, is_medico=True)  # criar usuário
                user_profile = MedicoProfile(nome=nome,
                                             email=email,
                                             crm=crm,
                                             especialidade=especialidade,
                                             telefone=telefone,
                                             cidade=cidade,
                                             user=user,
                                             clinica=clinica)
                user.save()
                user_profile.save()
                return HttpResponse('Foi salvo')
    else:
        form = CadastroMedicoForm()
    return render(requisicao, 'cadastro_medico.html', context={'form': form})  # se for GET
