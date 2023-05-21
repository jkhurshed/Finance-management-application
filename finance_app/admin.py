from django.contrib import admin
from django.contrib.auth.models import Group
from finance_app.models import Category, Transaction, Wallet

admin.site.unregister(Group)

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):

    model = Wallet
    list_display = ("id", "user", "description", "currency", "wallet_balance")
    list_filter = ("user",)
    search_fields = ("user",)
    list_display_links = ("user",)
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ("id", "user", "transaction_type", "amount", "note", "transaction_date", "category")
