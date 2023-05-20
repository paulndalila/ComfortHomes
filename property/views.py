from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choice import price_choices, bedroom_choices, county_choices 

from .models import Property


def index(request):
    propertys = Property.objects.order_by('-property_date')
    paginator = Paginator(propertys, 6)
    page = request.GET.get('page')
    paged_property = paginator.get_page(page)

    context = {
        'propertys': paged_property
        
    }

    return render(request, 'propertys/propertys.html', context)


def property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)

    context = {
        'property': property
    }

    return render(request, 'propertys/property.html', context)


def search(request):
    queryset_list = Property.objects.order_by('-property_date')

    # KEYWORDS
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # CITY
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            queryset_list = queryset_list.filter(location__iexact=location)

    # STATE
    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            queryset_list = queryset_list.filter(county__iexact=county)

    # BEDROOMS
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # PRICE
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'county_choices': county_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'propertys': queryset_list,
        'values': request.GET
    }

    return render(request, 'propertys/search.html', context)


# Create your views here.
