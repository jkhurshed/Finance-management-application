from rest_framework.serializers import ModelSerializer

from ..models import Wallet

class WalletFullSerializer(ModelSerializer):

    class Meta:
        model = Wallet
        fields = ["id", "title", "user", "description", "currency", "wallet_balance"]
