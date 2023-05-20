from django.shortcuts import render
from django.http import HttpResponse
from property.choice import price_choices, bedroom_choices, county_choices 

from property.models import Property
from accounts.models import Owner

def index(request):
    propertys = Property.objects.order_by('-list_date')

    context = {
        'propertys': propertys,
        'county_choices': county_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
   owners = Owner.objects.order_by('-date_joined')

    # Get MVP
   mvp_owners = Owner.objects.all().filter(is_mvp=True)

   context = {
        'owners': owners,
        'mvp_owners': mvp_owners
    }

   return render(request, 'pages/about.html', context)


# Create your views here.
