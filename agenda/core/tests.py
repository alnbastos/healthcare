from django.test import TestCase, RequestFactory
from core import views


class cadastro_cliente_test(TestCase):
    def test_cadastro_cliente(self):
        # teste de requisição
        request = RequestFactory().get('/cadastro/cliente/')
        response = views.cadastro_cliente(request)
        self.assertEqual(response.status_code, 400)
