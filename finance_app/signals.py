from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Wallet

@receiver(post_save, sender=Wallet)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Wallet.objects.create(user=instance)
