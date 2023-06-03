from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework.response import Response
from rest_framework import status, serializers

from ..models import Transaction
from django.db import transaction as dj_transaction
from finance_app.models import Category

from decimal import Decimal


class TransactionDetailSerializer(ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ("transaction_type", "wallet", "amount", "description", 
                  "category_id", "transaction_date")


class TransactionExpenseSerializer(ModelSerializer):
    
    TRANSACTION_TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    transactions_type = serializers.ChoiceField(choices=TRANSACTION_TYPE_CHOICES, default='expense')
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), 
                                                     source='category', write_only=True)

    class Meta:
        model = Transaction
        fields = ("transactions_type", "wallet", "amount", "description", "category_id")

    def validate(self, attrs):
        data = super().validate(attrs)
        wallet = self.context["user"].wallets.first()

        if wallet is None:
            raise ValidationError("User does not have any wallet")
        
        self._wallet = wallet
        
        if wallet.wallet_balance < Decimal(self.initial_data["amount"]):
            raise ValidationError("Insufficient balance.")
        elif Decimal(self.initial_data["amount"]) <= 0:
            raise ValidationError("Improperly value.")
        return data
    
    def create_transaction(self, validated_data):
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(pk=category_id)
        wallet = self._wallet

        with dj_transaction.atomic():
            transaction = Transaction.objects.create(
                wallet=wallet,
                category=category,
                amount=validated_data['amount'],
                description=validated_data.get('description', '')
            )

            wallet.wallet_balance -= transaction.amount
            wallet.save()

        return transaction


class TransactionIncomeSerializer(ModelSerializer):

    TRANSACTION_TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    transactions_type = serializers.ChoiceField(choices=TRANSACTION_TYPE_CHOICES, default='income')
    class Meta:
        model = Transaction
        fields = ("transactions_type", "wallet", "amount", "description")

    def validate(self, attrs):
        data = super().validate(attrs)
        wallet = self.context["user"].wallets.first()

        if wallet is None:
            raise ValidationError("User does not have any wallet")
        
        self._wallet = wallet
        
        if Decimal(self.initial_data["amount"]) <= 0:
            raise ValidationError("Inproperly value.")
        return data
    
    def create_transaction(self, validated_data):

        wallet = self._wallet

        transaction = Transaction.objects.create(
            wallet=wallet,
            amount=validated_data['amount'],
            description=validated_data.get('description', '')
        )

        wallet.wallet_balance += transaction.amount
        wallet.save()

        return transaction
