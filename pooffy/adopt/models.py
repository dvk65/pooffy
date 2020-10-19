from django.db import models

# Create your models here.
class Destination(models.Model):
    breed= models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='images')
    desc= models.TextField()
    age= models.DecimalField(max_digits=2, decimal_places=1)
    #offer: models.BooleanField(default=False)