from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, WalletViewSet

router = routers.DefaultRouter()
router.register("category", CategoryViewSet, "category")
router.register("wallet", WalletViewSet, "wallet")

urlpatterns = [
    path('', include(router.urls))
]
