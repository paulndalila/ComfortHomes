from django.shortcuts import render
from property.models import Property
from .models import PropertyViews

def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    views, created = PropertyViews.objects.get_or_create(property=property)
    views.view_count += 1
    views.save()
    return render(request, 'property/property_detail.html', {'property': property, 'views': views})


# Create your views here.
