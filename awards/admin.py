from django.contrib import admin
from .models import  Profile, Image, Projects

# Register your models here.

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Projects)