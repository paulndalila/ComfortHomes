from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import User,Customer, Owner


admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Owner)


# Register your mode


class CustomerAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view
    list_display = ('first_name', 'last_name', 'email', 'phone', 'user_link')

    def user_link(self, obj):
        # Generate a link to the user admin page
        url = reverse('admin:auth_user_change', args=[obj.user.id])
        return format_html('<a href="{}">{}</a>', url, obj.user.username)
    user_link.short_description = 'User'

    # Define a function to generate the PDF report
    def generate_report(self, request, queryset):
        return generate_report(request, queryset)

    # Add the function to the list of actions
    actions = [generate_report]

