from django.db import models
from datetime import datetime

# Create your models here.
class Products(models.Model):
    image = models.ImageField(null=False,blank=False)
    name = models.CharField(max_length=200,null =False,blank=False)
    price = models.DecimalField(null =False,blank = False,max_digits=5,decimal_places =2)
    description = models.TextField()
    is_published = models.BooleanField(default = True)
    created_dat = models.DateTimeField(default = datetime.now,blank = False)

    def __str__(self) -> str:
        return self.name

