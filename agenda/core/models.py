from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_cliente = models.BooleanField('cliente status', default=False)
    is_medico = models.BooleanField('medico status', default=False)
    is_clinica = models.BooleanField('clinica status', default=False)


class ClienteProfile(models.Model):
    SEXO_CHOICES = (
        (u'F', u'Feminino'),
        (u'M', u'Masculino')
    )
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    sexo = models.CharField(max_length=2, choices=SEXO_CHOICES)
    cpf = models.CharField(max_length=11, primary_key=True)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class MedicoProfile(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    crm = models.IntegerField(primary_key=True)
    especialidade = models.ManyToManyField('Especialidade', through='MedicoEspecialidade')
    telefone = models.CharField(max_length=11)
    cidade = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    clinica = models.ForeignKey(User, related_name='clinica', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class ClinicaProfile(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Especialidade(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descricao


class MedicoEspecialidade(models.Model):
    medico = models.ForeignKey(MedicoProfile, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)


class Agenda(models.Model):
    data_agenda = models.DateTimeField()
    clinica = models.ForeignKey(ClinicaProfile, on_delete=models.SET_NULL, null=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True)
    medico = models.ForeignKey(MedicoProfile, on_delete=models.SET_NULL, null=True)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.medico