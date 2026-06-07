from django.db import models

# Create your models here.
class TransactionEmployee(models.Model):
    name = models.CharField(max_length=100)