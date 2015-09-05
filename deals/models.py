from django.db import models

class CustomerQuery(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=30)
    key1 = models.CharField(max_length=5)
    key2 = models.CharField(max_length=5)
    key3 = models.CharField(max_length=5)
    key4 = models.CharField(max_length=5)
    key5 = models.CharField(max_length=5)