from django.contrib import admin
from django.contrib.auth.models import Group
from finance_app.models import Category, Wallet

admin.site.unregister(Group)

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):

    model = Wallet
    list_display = ("id", "title", "user", "description", "currency", "wallet_balance")
    list_filter = ("user",)
    search_fields = ("user",)
    list_display_links = ("user",)
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ("id", "title", "parent")
    list_display_links = ("title",)
