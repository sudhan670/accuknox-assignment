import threading

from django.core.management.base import BaseCommand

from thread_demo.models import ThreadEmployee


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        print("Question 2: Same Thread Check")
        print(f"Caller Thread ID: {threading.get_ident()}")

        ThreadEmployee.objects.create(
            name="Thread User"
        )
        print(f"Caller Thread ID: {threading.get_ident()}")
