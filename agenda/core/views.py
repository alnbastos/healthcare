from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
# from django.contrib.sessions import
from django.contrib.auth.decorators import login_required
from core.models import User, ClienteProfile, MedicoProfile, ClinicaProfile, Agenda
from core.forms import CadastroUsuarioForm, CadastroMedicoForm, CadastroClinicaForm, AgendaForm


# Create your views here.

# telas para apresentar apenas textos
def home_page(requisicao):
    return render(requisicao, 'index.html')


def quem_somos(requisicao):
    return render(requisicao, 'quem_somos.html')


def agendamento(requisicao):
    return render(requisicao, 'agendamento.html')


def servicos(requisicao):
    return render(requisicao, 'servicos.html')


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
                user.set_password(pass_user)  # criptografria da senha
                user.save()
                user_profile.save()
                return redirect('/cadastro/cliente/ok/')
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

                user.set_password(pass_user)  # criptografria da senha
                user.save()
                user_profile.save()

                for es in especialidade:
                    user_profile.especialidade.add(es.id)

                return redirect('/cadastro/medico/ok/')
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
                user.set_password(pass_user)  # criptografria da senha
                user.save()
                user_profile.save()
                return redirect('/cadastro/clinica/ok/')
    else:
        form = CadastroClinicaForm()
    return render(requisicao, 'cadastro_clinica.html', context={'form': form})  # se for GET


def ok_cliente(requisicao):
    return render(requisicao, 'poscad_cliente.html')


def ok_medico(requisicao):
    return render(requisicao, 'poscad_medico.html')


def ok_clinica(requisicao):
    return render(requisicao, 'poscad_clinica.html')


def login_user(requisicao):
    return render(requisicao, 'login_user.html')


def logout_user(requisicao):
    return redirect('/')


def submit_user(requisicao):
    if requisicao.POST:
        email = requisicao.POST['email']
        pass_user = requisicao.POST['pass_user']
        usuario = authenticate(username=email, password=pass_user)
        if usuario is not None:
            login(requisicao, usuario)
            if usuario.is_cliente:
                return redirect('/perfil/cliente/')
            elif usuario.is_medico:
                return redirect('/perfil/medico/')
            elif usuario.is_clinica:
                return redirect('/perfil/clinica/')
            else:
                return redirect('/')
        else:
            messages.error(requisicao, 'Usuário ou senha invállido.')
            return render(requisicao, 'login_user.html')


def perfil_cliente(requisicao):
    usuario = requisicao.user
    nome = ClienteProfile.objects.get(user=usuario)
    dados = {'nome': nome.nome}
    return render(requisicao, 'perfil_cliente.html', dados)


def perfil_medico(requisicao):
    return render(requisicao, 'perfil_medico.html')


def perfil_clinica(requisicao):
    return render(requisicao, 'perfil_clinica.html')


@login_required(login_url='/login/')
def agendar(requisicao):
    return render(requisicao, 'agendar.html')

#
# def load_medico(requisicao):
#     medico_id = requisicao.GET.get('medico')
#
#     return render(requisicao, 'agendar.html', {'clinicas': clinicas})
#


def load_clinica(requisicao):
    #especialidade_id = requisicao.GET.get('especialidade_id')
    especialidade_id = 1
    medicos = MedicoProfile.objects.filter(especialidade__id=especialidade_id)
    clinicas = ClinicaProfile.objects.filter(pk__in=medicos.clinica_id)
    return render(requisicao, 'options_clinica.html', {'clinicas': clinicas})
