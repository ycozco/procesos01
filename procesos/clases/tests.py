from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    databases = {'test'}  # Especifica qué base de datos utilizar para las pruebas

    def setUp(self):
        self.username = 'yosetcozco'
        self.password = '581321yoset'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_con_credenciales_validas(self):
        # Realiza una solicitud POST al view de login con las credenciales válidas
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})

        # Verifica que la respuesta redireccione a la página de perfil (o a donde lo hayas configurado en tu view)
        self.assertRedirects(response, reverse('perfil'))

    def test_login_con_credenciales_invalidas(self):
        # Realiza una solicitud POST al view de login con credenciales inválidas
        response = self.client.post(reverse('login'), {'username': 'usuario_invalido', 'password': 'contraseña_invalida'})

        # Verifica que la respuesta no sea una redirección y que el template de login se muestre con un mensaje de error
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Credenciales inválidas. Inténtalo de nuevo.')
