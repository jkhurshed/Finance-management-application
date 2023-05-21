from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):

    TRANSACTION_TYPE_CHOICES = (
        ('expense', 'Expense'),
        ('income', 'Income'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, 
        verbose_name="User")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField("Description", blank=True)
    transaction_date = models.DateTimeField("Transaction date", auto_now_add=True)
    category = models.ForeignKey("finance_app.category", on_delete=models.CASCADE, 
        related_name="user", verbose_name="User")