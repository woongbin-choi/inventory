from django.db import models
from django.contrib.auth.models import User

class Management(models.Model):
    product_name = models.CharField(max_length=128)
    purity = models.CharField(max_length=32)
    quantity = models.IntegerField()
    residual_quantity = models.IntegerField()
    manufacturer = models.CharField(max_length=32)
    storage_location = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    partname = models.CharField(max_length=32)
    division = models.CharField(max_length=32)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    registration_date = models.DateField()
    xpiration_date = models.DateField()
    comment = models.CharField(max_length=128, null=True, blank=True)
    msds = models.FileField(blank=True, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.product_name