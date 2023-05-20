from django.db import models
from datetime import datetime
from property.models import Property
from accounts.models import Customer




class Clients(models.Model):
    property = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    clients_date = models.DateTimeField(default=datetime.now)
   
    
    def __str__ (self):
        return self.name

# Create your models here.


class PropertyInquiry(models.Model):
    property = models.ForeignKey('property.Property', on_delete=models.DO_NOTHING, related_name='inquiries')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    message = models.TextField()
   
    
    

    def __str__(self):
        return f"Inquiry for {self.property.title} by {self.name}"
