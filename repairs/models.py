from django.db import models

class RepairRequest(models.Model):
    DEVICE_CHOICES = [
        ('phone', 'Смартфон'),
        ('laptop', 'Ноутбук'),
        ('tablet', 'Планшет'),
        ('tv', 'Телевізор'),
        ('other', 'Інше'),
    ]

    name = models.CharField(max_length=100, verbose_name="Ім'я")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    device_type = models.CharField(max_length=20, choices=DEVICE_CHOICES, verbose_name="Тип техніки")
    description = models.TextField(verbose_name="Опис проблеми")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачі")
    is_processed = models.BooleanField(default=False, verbose_name="Опрацьовано")

    def __str__(self):
        return f"{self.name} - {self.device_type}"
