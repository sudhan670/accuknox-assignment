import threading 

from django.db.models.signals import post_save
from django.dispatch import receiver 

from .models import Employee
@receiver(post_save, sender=Employee)
def employee_created(sender, instance, **kwargs):
    print("Signal Started")
    print(f"Signal Thread ID: {threading.get_ident()}")