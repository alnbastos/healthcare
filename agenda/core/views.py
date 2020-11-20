from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.models import User, ClienteProfile, MedicoProfile, ClinicaProfile
from django.contrib import messages
from core.forms import CadastroUsuarioForm, CadastroMedicoForm, CadastroClinicaForm


# Create your views here.

# telas para apresentar apenas textos
def home_page(requisicao):
    return render(requisicao, 'index.html')


def quem_somos(requisicao):
    return render(requisicao, 'quem_somos.html')


def agendamento(requisicao):
    return render(requisicao, 'agendamento.html')


# telas para receber requisições
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
    return render(requisicao, 'cadastro_cliente.html', context={'form': form})  # se for GET


def cadastro_medico(requisicao):
    if requisicao.POST:
        form = CadastroMedicoForm(requisicao.POST)
        if form.is_valid():
            nome = requisicao.POST.get('nome')
            crm = requisicao.POST.get('crm')
            telefone = requisicao.POST.get('telefone')
            cidade = requisicao.POST.get('cidade')
            email = requisicao.POST.get('email')
            pass_user = requisicao.POST.get('pass_user')
            email_existe = User.objects.filter(username=email).exists()
            crm_existe = MedicoProfile.objects.filter(crm=crm).exists()
            especialidade = form.cleaned_data['especialidade']
            clinica = form.cleaned_data['clinica'].user
            if email_existe:
                messages.error(requisicao, 'E-mail já cadastrado.')
            if crm_existe:
                messages.error(requisicao, 'CRM já cadastrado.')
            if not email_existe and not crm_existe:
                user = User(username=email, password=pass_user, is_medico=True)  # criar usuário
                user_profile = MedicoProfile(nome=nome,
                                             email=email,
                                             crm=crm,
                                             telefone=telefone,
                                             cidade=cidade,
                                             user=user,
                                             clinica=clinica)

                user.save()
                user_profile.save()

                for es in especialidade:
                    user_profile.especialidade.add(es.id)

                return HttpResponse('Médico salvo')
    else:
        form = CadastroMedicoForm()
    return render(requisicao, 'cadastro_medico.html', context={'form': form})  # se for GET


def cadastro_clinica(requisicao):
    if requisicao.POST:
        nome = requisicao.POST.get('nome')
        cnpj = requisicao.POST.get('cnpj')
        cep = requisicao.POST.get('cep')
        endereco = requisicao.POST.get('endereco')
        cidade = requisicao.POST.get('cidade')
        telefone = requisicao.POST.get('telefone')
        email = requisicao.POST.get('email')
        pass_user = requisicao.POST.get('pass_user')
        form = CadastroClinicaForm(requisicao.POST)
        if form.is_valid():
            email_existe = User.objects.filter(username=email).exists()
            cnpj_existe = ClinicaProfile.objects.filter(cnpj=cnpj).exists()
            if email_existe:
                messages.error(requisicao, 'E-mail já cadastrado.')
            if cnpj_existe:
                messages.error(requisicao, 'CNPJ já cadastrado.')
            if not email_existe and not cnpj_existe:
                user = User(username=email, password=pass_user, is_clinica=True)  # criar usuário
                user_profile = ClinicaProfile(nome=nome,
                                              cnpj=cnpj,
                                              cep=cep,
                                              endereco=endereco,
                                              cidade=cidade,
                                              telefone=telefone,
                                              email=email,
                                              user=user)
                user.save()
                user_profile.save()
                return HttpResponse('Foi salvo')
    else:
        form = CadastroClinicaForm()
    return render(requisicao, 'cadastro_clinica.html', context={'form': form})  # se for GET


def select_user(requisicao):
    return render(requisicao, 'select_user.html')


def login_cliente(requisicao):
    return render(requisicao, 'login_cliente.html')


def servicos(requisicao):
    return render(requisicao, 'servicos.html')


def agendar(requisicao):
    return render(requisicao, 'agendar.html')
