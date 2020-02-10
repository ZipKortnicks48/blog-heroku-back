from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Content,Subcategory,Category
# Register your models here.
admin.site.register(Content)
admin.site.register(Subcategory)
admin.site.register(Category)