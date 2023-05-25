from django.contrib import admin
from transaction.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ("id", "wallet", "transaction_type", "amount", "description", 
                    "transaction_date", "category")

