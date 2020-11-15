from django import forms
from django.forms import fields
from core.models import ClinicaProfile, Especialidade


# Create your forms here.
class CadastroUsuarioForm(forms.Form):
    SEXO_CHOICES = (
        (u'F', u'Feminino'),
        (u'M', u'Masculino')
    )
    nome = forms.CharField(max_length=100, label='Nome')
    data_nasc = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, label='Sexo')
    cpf = forms.CharField(max_length=11, label='CPF')
    endereco = forms.CharField(max_length=100, label='Endereço')
    telefone = forms.CharField(max_length=11, label='Telefone')
    email = forms.EmailField(max_length=100, label='E-mail')
    pass_user = forms.CharField(widget=forms.PasswordInput, label='Senha')
