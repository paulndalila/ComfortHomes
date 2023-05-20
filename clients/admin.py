from django.contrib import admin


from .models import Clients,PropertyInquiry

# class ClientsAdmin(admin.ModelAdmin):
#     list_display = ( 'name', 'property', 'email', 'clients_date')
#     search_fields = ('name', 'email', 'property')
#     list_per_page = 25

admin.site.register(Clients)


class PropertyInquiryAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'property', 'email')
    search_fields = ('name', 'email', 'property')
#     list_per_page = 25

admin.site.register(PropertyInquiry,PropertyInquiryAdmin)