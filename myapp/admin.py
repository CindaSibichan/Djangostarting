from django.contrib import admin
from . models import Products,Musician,Album

# Register your models here.
admin.site.register(Products)
admin.site.register(Musician)
admin.site.register(Album)
