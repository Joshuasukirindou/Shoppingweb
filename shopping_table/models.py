# Create your models here.
# from django.conf import settings
from django.db import models
# from django.utils import timezone
# from django.urls import reverse

class Alcohol(models.Model):
    id = models.BigAutoField()
    product_id = models.IntegerField()
    product_name = models.TextField()
    product_price = models.IntegerField()
    product_country = models.TextField()
    product_size = models.DecimalField(max_digits=4, decimal_places=3)
    product_ABV = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f'{self.id}, {self.product_id}, {self.product_name}, {self.product_price}, {self.product_country}, {self.product_size}, {self.product_ABV}'




from django.db import models

# Create your models here.
