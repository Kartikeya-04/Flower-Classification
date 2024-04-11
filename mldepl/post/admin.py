from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Flowers
# Register your models here.
@admin.register(Flowers)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('sepal_length', 'sepal_width',)
