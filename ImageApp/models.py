from django.db import models

# Create your models here.
class AddImage(models.Model):
    Product=models.CharField(max_length=255,null=True)
    Price=models.IntegerField()
    Quantity=models.IntegerField()
    Image=models.ImageField(upload_to="image/",null=True)