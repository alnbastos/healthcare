from django import forms


# Create your forms here.
class CadastroUsuarioForm(forms.Form):
    SEXO_CHOICES = (
        (u'F', u'Feminino'),
        (u'M', u'Masculino')
    )
    nome = forms.CharField(max_length=100, label='Nome')
    data_nasc = forms.DateField(label='Data de Nascimento', widget=forms.SelectDateWidget)
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, label='Sexo')
    cpf = forms.CharField(max_length=11, label='CPF')
    endereco = forms.CharField(max_length=100, label='Endereço')
    telefone = forms.CharField(max_length=11, label='Telefone')
    email = forms.EmailField(max_length=100, label='E-mail')
    pass_user = forms.CharField(widget=forms.PasswordInput, label='Senha')
