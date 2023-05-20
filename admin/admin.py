from django.contrib import admin
from owners.models import Owner

class OwnerAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the admin interface
    list_display = ('id', 'name', 'created_at', 'updated_at')
    
admin.site.register(Owner, OwnerAdmin)
