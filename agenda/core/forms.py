from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.contrib.admin import widgets
from core.models import ClinicaProfile, Especialidade, MedicoProfile, Agenda


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


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ('data_agenda', 'especialidade', 'clinica', 'medico')
        widgets = {
            'data_agenda': forms.widgets.DateTimeInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['clinica'].queryset = ClinicaProfile.objects.none()
        self.fields['medico'].queryset = MedicoProfile.objects.none()
        if 'especialidade' in self.data:
            try:
                especialidade_id = int(self.data.get('especialidade'))
                medicos = MedicoProfile.objects.filter(especialidade__id=especialidade_id)
                self.fields['clinica'].queryset = ClinicaProfile.objects.filter(pk__in=medicos.values_list('clinica__clinicaprofile__cnpj'))
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['clinica'].queryset = self.instance.clinica
        if 'clinica' in self.data:
            try:
                especialidade_id = int(self.data.get('especialidade'))
                clinica_id = int(self.data.get('clinica'))
                medicos = MedicoProfile.objects.filter(especialidade__id=especialidade_id, clinica__clinicaprofile__cnpj=clinica_id)
                self.fields['medico'].queryset = medicos
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['medico'].queryset = self.instance.medico
