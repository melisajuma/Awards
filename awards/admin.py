from django.contrib import admin
from .models import Image, Projects, Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Projects)