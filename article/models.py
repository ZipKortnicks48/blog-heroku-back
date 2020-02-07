from django.db import models

# Create your models here.
from rest_framework import filters

# Контент
class Content(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    body=models.TextField()
    file=models.FileField()
    date=models.DateField()
    subactegory=models.ForeignKey('Subcategory', related_name='content_have_subcategory', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
#Подкатегория 
class Subcategory(models.Model):
    name=models.CharField(max_length=40)
    category=models.ForeignKey('Category',related_name='subcategory_have_category',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
#Категория
class Category(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name