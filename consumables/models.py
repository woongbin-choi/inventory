from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    item_code = models.IntegerField()
    product_name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    storage_location = models.CharField(max_length=64)
    team_name = models.CharField(max_length=16)
    quantity = models.IntegerField()
    category = models.CharField(max_length=32)
    safety_stock = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.product_name