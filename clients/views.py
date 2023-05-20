from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from property.models import Property
from .models import PropertyInquiry




@login_required
def inquiry(request, property_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
          messages.warning(request, 'Please login first to make an inquiry.')
          return redirect('login')

        property = Property.objects.get(id=property_id)
        user = request.user
        message = "Property Inquiry - " + property.title + ": " + request.POST['message']
        phone = request.POST['phone']
        email = request.POST['email']
        username = request.POST['name']
        inquiry = PropertyInquiry(property=property, phone=phone, email=email, name=username, message=message)
        inquiry.save()

        messages.success(request, 'Your inquiry has been submitted. The property owner will contact you soon.')
        return redirect('/property/' + str(property_id))

    return redirect('propertys/property.html')

