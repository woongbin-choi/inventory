from django.db import models
from django.contrib.auth.models import User

class Takeout(models.Model):
    carry_day = models.DateField()
    carry_team = models.CharField(max_length=16)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    receive_company = models.CharField(max_length=32)
    receive_tel = models.CharField(max_length=16)
    receive_user = models.CharField(max_length=16)
    material_name = models.CharField(max_length=64)
    material_info = models.CharField(max_length=64)
    purpose = models.CharField(max_length=64)
    pack_date = models.DateField()
    production_capacity = models.CharField(max_length=32)
    carry_capacity = models.CharField(max_length=32)
    residual_quantity = models.CharField(max_length=32)
    delivery = models.CharField(max_length=16)
    note = models.TextField(null=True, blank=True)
    modify_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.material_name