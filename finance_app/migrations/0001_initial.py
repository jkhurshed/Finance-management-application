# Generated by Django 4.2.1 on 2023-05-21 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Заголовок')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='finance_app.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250, verbose_name='Wallet description')),
                ('currency', models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('GBP', 'British Pound'), ('JPY', 'Japanese Yen'), ('RUB', 'Russian rubl'), ('SMN', 'Tajik somoni'), ('SOM', 'Uzbek som'), ('SUM', 'Kazakh sum'), ('YUAN', 'Chinesse yuan')], max_length=10, verbose_name='Currency list')),
                ('wallet_balance', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Wallet balance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('expense', 'Expense'), ('income', 'Income')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.TextField(blank=True, verbose_name='Description')),
                ('transaction_date', models.DateTimeField(auto_now_add=True, verbose_name='Transaction date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='finance_app.category', verbose_name='User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
