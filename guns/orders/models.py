from django.db import models

# Create your models here.

class Order(models.Model):
    sellable_id = models.ForeignKey('sellable.Sellable', on_delete=models.DO_NOTHING)
    contacts = models.TextField()
    total_price = models.FloatField()



