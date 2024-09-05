from django.db import models

# Create your models here.

class Sellable(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    is_Reserved = models.BooleanField(default=False)
    photo_Url = models.TextField()
    is_bought = models.BooleanField(default=False)

    def __str__(self):
        return f'name: {self.title}, description: {self.description}'
