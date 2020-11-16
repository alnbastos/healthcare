from django import forms
from django.forms import fields
from core.models import ClinicaProfile, Especialidade, MedicoProfile


# Create your forms here.

class CadastroUsuarioForm(forms.Form):
    SEXO_CHOICES = (
        (u'F', u'Feminino'),
        (u'M', u'Masculino')
    )
    nome = forms.CharField(max_length=100, label='Nome')
    cpf = forms.CharField(max_length=11, label='CPF')
    data_nasc = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, label='Sexo')
    telefone = forms.CharField(max_length=11, label='Telefone')
    endereco = forms.CharField(max_length=100, label='Endereço')
    email = forms.EmailField(max_length=100, label='E-mail')
    pass_user = forms.CharField(widget=forms.PasswordInput, label='Senha')


class CadastroMedicoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    crm = forms.IntegerField(label='CRM')
    telefone = forms.CharField(max_length=11, label='Telefone')
    especialidade = forms.ModelMultipleChoiceField(queryset=Especialidade.objects.all())
    cidade = forms.CharField(max_length=100, label='Cidade')
    clinica = forms.ModelChoiceField(queryset=ClinicaProfile.objects.all(), empty_label="Selecione uma clinica", label='Clinica')
    email = forms.EmailField(max_length=100, label='E-mail')
    pass_user = forms.CharField(widget=forms.PasswordInput, label='Senha')


class CadastroClinicaForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    cnpj = forms.IntegerField(label='CNPJ')
    cep = forms.IntegerField(label='CEP')
    endereco = forms.CharField(max_length=100, label='Endereço')
    cidade = forms.CharField(max_length=100, label='Cidade')
    telefone = forms.CharField(max_length=11, label='Telefone')
    email = forms.EmailField(max_length=100, label='E-mail')
    pass_user = forms.CharField(widget=forms.PasswordInput, label='Senha')
