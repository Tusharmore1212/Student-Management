from django.contrib import admin
from myapp.models import Image

# Register your models here.
class imageadmin(admin.ModelAdmin):
    list_display = ('image1','date')

admin.site.register(Image, imageadmin)


