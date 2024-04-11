from typing import Any
from django.db import models
# Create your models here.

    
                               

class Flowers(models.Model):
    sepal_length=models.FloatField()
    sepal_width=models.FloatField()
    petal_length=models.FloatField()
    petal_width=models.FloatField()
    def __str__(self):
        return self.petal_length   

