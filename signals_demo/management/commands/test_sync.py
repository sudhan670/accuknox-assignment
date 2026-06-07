import time

from django.core.management.base import BaseCommand

from signals_demo.models import Employee


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        start = time.time()

        Employee.objects.create(name="John")

        end = time.time()

        print("Question 1: Synchronous Signal")
        print(f"Execution Time: {end - start:.2f} seconds")