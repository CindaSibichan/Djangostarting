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

    class Meta:
        db_table = "Product_table"

    def __str__(self) -> str:
        return self.name
    
class  Musician(models.Model):
    f_name = models.CharField(max_length=50,null=False,blank = False)
    l_name = models.CharField(max_length=50,null = False,blank = False)
    instrument = models.CharField(max_length=100,null = False,blank = False)

    def __str__(self) -> str:
        return self.f_name
    

class Album(models.Model):
    artist = models.ForeignKey(Musician,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    released_date = models.DateField()

    def __str__(self) -> str:
        return self.name


