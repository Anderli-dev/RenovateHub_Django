from django.test import TestCase, Client
from django.urls import reverse
from repairs.models import RepairRequest

class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_get_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_valid_form_htmx(self):
        data = {
            'name': 'Іван',
            'phone': '1234567890',
            'device_type': 'laptop',
            'description': 'Не вмикається',
        }
        response = self.client.post(
            self.url,
            data,
            HTTP_HX_REQUEST='true',
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('Заявку прийнято!', response.content.decode())
        self.assertEqual(RepairRequest.objects.count(), 1)

    def test_post_invalid_form_htmx(self):
        data = {
            'name': '',
            'phone': '',
            'device_type': '',
            'description': '',
        }
        response = self.client.post(
            self.url,
            data,
            HTTP_HX_REQUEST='true',
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('Форма містить помилки.', response.content.decode())
        self.assertEqual(RepairRequest.objects.count(), 0)

    def test_post_valid_form_non_htmx(self):
        data = {
            'name': 'Олег',
            'phone': '1111111111',
            'device_type': 'phone',
            'description': 'Розбитий екран',
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, '/')
        self.assertEqual(RepairRequest.objects.count(), 1)
