from django.test import TestCase
from repairs.forms import RepairRequestForm

class RepairRequestFormTests(TestCase):
    def test_valid_form(self):
        form = RepairRequestForm(data={
            'name': 'Ірина',
            'phone': '0999999999',
            'device_type': 'laptop',
            'description': 'Гріється',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = RepairRequestForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
