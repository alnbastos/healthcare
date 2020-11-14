from django.db import models


# Create your models here.
class UserProfile(models.Model):
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
    user = models.OneToOneField('auth.User', unique=True, on_delete=models.CASCADE)

