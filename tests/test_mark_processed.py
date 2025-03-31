from django.test import TestCase, Client
from django.urls import reverse
from repairs.models import RepairRequest

class MarkProcessedViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.repair_request = RepairRequest.objects.create(
            name='Петро',
            phone='9876543210',
            device_type='Монітор',
            description='Не працює екран'
        )
        self.url = reverse('mark_processed', args=[self.repair_request.pk])

    def test_post_marks_as_processed(self):
        self.assertFalse(self.repair_request.is_processed)
        response = self.client.post(self.url)
        self.repair_request.refresh_from_db()
        self.assertTrue(self.repair_request.is_processed)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Опрацьовано', response.content.decode())

    def test_get_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)  # Method Not Allowed
