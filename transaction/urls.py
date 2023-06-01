from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('transactions', TransactionDetailViewSet, "transactions")
router.register('expenses', TransactionExpenseViewSet, 'expenses')
router.register('income', TransactionIncomeViewSet, 'income')

urlpatterns = [
    path('', include(router.urls)),
]
