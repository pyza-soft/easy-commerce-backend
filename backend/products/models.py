from django.db import models
from .utils import get_image_path

class Brand(models.Model):
    name = models.CharField(max_length=64,unique=True)
    description = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    brand = models.ForeignKey('Brand', related_name='category', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    
    def __str__(self):
        return self.name
