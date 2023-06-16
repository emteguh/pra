from django.contrib import admin
from .models import Artikel
# Register your models here.


class Slug(admin.ModelAdmin):
    readonly_fields = [
        "slug",
        "publish",
        "update",
    ]
    
admin.site.register(Artikel, Slug)
