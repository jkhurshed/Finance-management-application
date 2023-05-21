from django.db import models
from django.contrib.auth.models import User

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, 
        verbose_name="User")
    description = models.CharField("Wallet description", max_length=250)
    currency = models.CharField("Currency list", choices=CURRENCY_CHOICES, max_length=10)
    wallet_balance = models.DecimalField("Wallet balance", max_digits=8, decimal_places=2)
