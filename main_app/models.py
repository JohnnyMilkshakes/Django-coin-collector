from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(max_length=100)
    metal_type = models.CharField()
    description = models.TextField(max_length=500)
    denomination = models.CharField(max_length=100)
    # country = models.ForeignKey()
    # owner = models.ForeignKey()
    
    def __str__(self):
        return f"Name: {self.name}, Year: {self.year}, metal: {self.metal_type}"
