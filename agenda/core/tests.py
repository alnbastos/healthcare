from django.test import TestCase, RequestFactory
from core import views
from core.models import User, ClienteProfile, MedicoProfile, ClinicaProfile, Especialidade


class ClienteProfileModelTest(TestCase):
    def test_to_string(self):
        cliente = ClienteProfile(
            nome='nome',
            data_nasc='1900-01-01',
            sexo='M',
            cpf='12345678901',
            endereco='',
            telefone='',
            email='1234',
            user=User())
        self.assertEqual(str(cliente), 'nome')


class MedicoProfileModelTest(TestCase):
    def test_to_string(self):
        medico = MedicoProfile(
            nome='nome',
            email='1234',
            crm=123456,
            telefone='',
            cidade='')
        self.assertEqual(str(medico), 'nome')


class ClinicaProfileModelTest(TestCase):
    def test_to_string(self):
        clinica = ClinicaProfile(
            nome='nome',
            email='1234',
            cnpj='',
            telefone='',
            endereco='',
            cidade='',
            cep='',
            user=User(),
        )
        self.assertEqual(str(clinica), 'nome')


class EspecialidadeModelTest(TestCase):
    def test_to_string(self):
        especialidade = Especialidade(
           descricao='especialidade'
        )
        self.assertEqual(str(especialidade), 'especialidade')


class CadastroClienteViewTest(TestCase):
    def test_cadastro_cliente_get_test(self):
        # teste de requisição
        request = RequestFactory().get('/cadastro/cliente/')
        response = views.cadastro_cliente(request)
        self.assertEqual(response.status_code, 200)

    def test_cadastro_cliente_post_test(self):
        # valida o cadastro de cliente e que foi redirecionado
        data = {
            'nome': 'Aline',
            'data_nasc': '1900-01-01',
            'sexo': 'F',
            'cpf': '12345678901',
            'endereco': 'Rua Astronauta',
            'telefone': '99999-9999',
            'email': 'aline@gmail.com',
            'pass_user': '1234',
        }
        request = RequestFactory().post('/cadastro/cliente/', data=data)
        response = views.cadastro_cliente(request)

        cliente = ClienteProfile.objects.get(cpf='12345678901')
        self.assertTrue(cliente)
        self.assertEqual(response.status_code, 302)
