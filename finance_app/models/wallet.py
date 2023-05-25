from django.db import models
from django.conf import settings

class Wallet(models.Model):
    
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('JPY', 'Japanese Yen'),
        ('RUB', 'Russian rubl'),
        ('SMN', 'Tajik somoni'),
        ('SOM', 'Uzbek som'),
        ('SUM', 'Kazakh sum'),
        ('YUAN', 'Chinesse yuan'),
    ]

    title = models.CharField("Wallet title", max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
        verbose_name="User")
    description = models.CharField("Wallet description", max_length=250, blank=True)
    currency = models.CharField("Currency list", choices=CURRENCY_CHOICES, max_length=10)
    wallet_balance = models.DecimalField("Wallet balance", max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.title
