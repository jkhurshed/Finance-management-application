from rest_framework import mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from transaction.serializers import TransactionSerializer
from transaction.models import Transaction

from finance_app.serializers import WalletFullSerializer
from finance_app.models import Wallet


class TransactionViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        wallet_id = kwargs.get('wallet_id')
        try:
            wallet = Wallet.objects.get(pk=wallet_id)
        except Wallet.DoesNotExist:
            return Response({'error': 'Wallet not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data['amount']
        
        if wallet.balance < amount:
            return Response({'error': 'Insufficient balance.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a transaction and update account balance
        transaction = Transaction.objects.create(
            wallet=wallet,
            amount=amount,
            description=serializer.validated_data.get('description', ''),
        )
        wallet.balance -= amount
        wallet.save()
        
        return Response({'success': 'Transaction created successfully.'}, status=status.HTTP_201_CREATED)