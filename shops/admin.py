from django.contrib import admin
from .models import *


class categs(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']


admin.site.register(Categ, categs)


class prods(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'price', 'stock', 'img']
    list_editable = ['price', 'stock', 'img']


admin.site.register(product, prods)
from django.contrib import admin

# Register your models here.
