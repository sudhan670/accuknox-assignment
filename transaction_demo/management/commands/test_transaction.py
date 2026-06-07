from django.core.management.base import BaseCommand
from django.db import transaction

from transaction_demo.models import TransactionEmployee


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        try:
            with transaction.atomic():

                TransactionEmployee.objects.create(
                    name="John"
                )

        except Exception as e:
            print(e)

        print(
            "Count:",
            TransactionEmployee.objects.filter(
                name="John"
            ).count()
        )