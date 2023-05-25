from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from ..serializers import *
from ..models import Wallet


class WalletViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin
                    ):
    
    queryset = Wallet.objects.all()
    serializer_class = WalletFullSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'patch', 'post']

    '''def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return CategoryCreateSerializer
        if self.action == 'list':
            return CategoryShortSerializer
        if self.action == 'retrieve':
            return CategoryFullSerializer
        if self.action == 'subcategories':
            return CategoryChildsSerializer
        return self.serializer_class'''
    