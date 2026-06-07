from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TransactionEmployee


@receiver(post_save, sender=TransactionEmployee)
def employee_created(sender, instance, **kwargs):
    print("Signal Executed")

    raise Exception("Signal Failed")