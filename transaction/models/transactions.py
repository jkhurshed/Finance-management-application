from django.db import models
from ..choices import TRANSACTION_TYPE_CHOICES

class Transaction(models.Model):

    wallet = models.ForeignKey("finance_app.wallet", on_delete=models.CASCADE, 
        verbose_name="wallet")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField("Description", blank=True)
    transaction_date = models.DateTimeField("Transaction date", auto_now_add=True)
    category = models.ForeignKey("finance_app.category", on_delete=models.CASCADE, 
        related_name="catefory", verbose_name="Category")
    
    class Meta:
        ordering = ["wallet"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
    
    def __str__(self) -> str:
        return f"Transaction {self.id} {self.description}"
    