from rest_framework import mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from transaction.serializers import (TransactionDetailSerializer, TransactionExpenseSerializer, 
                                     TransactionIncomeSerializer)
from transaction.models import Transaction


class TransactionDetailViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Transaction.objects.all()
    serializer_class = TransactionDetailSerializer


class TransactionExpenseViewSet(GenericViewSet, mixins.CreateModelMixin):
    queryset = Transaction.objects.all()
    serializer_class = TransactionExpenseSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
    
    '''def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.create_transaction()
        
        # Create a transaction and update account balance
        return Response({'success': 'Transaction created successfully.'}, 
                         status=status.HTTP_201_CREATED)'''
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = serializer.create_transaction

        return Response({'success': 'Transaction created successfully.', 'data': serializer.data},
                        status=status.HTTP_201_CREATED)
        

class TransactionIncomeViewSet(GenericViewSet, mixins.CreateModelMixin):
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionIncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = serializer.create_transaction

        return Response({'success': 'Transaction created successfully.', 'data': serializer.data},
                        status=status.HTTP_201_CREATED)