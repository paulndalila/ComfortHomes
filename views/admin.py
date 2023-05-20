
from django.contrib import admin
from .models import PropertyViews

class PropertyViewsAdmin(admin.ModelAdmin):
    list_display = ('id',  'property',)
    list_display_links = ('id', 'property')
    search_fields = ('property','id')
    

admin.site.register(PropertyViews,PropertyViewsAdmin)

# Register your models here.
