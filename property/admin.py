from django.contrib import admin
from .report_admin import generate_property_report
from reportlab.platypus import Table




from .models import Property
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'location')
    actions = [generate_property_report]
    
admin.site.register(Property, PropertyAdmin)





# Register your models here.
