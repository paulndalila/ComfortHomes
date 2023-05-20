from django.db import models
from property.models import Property

class PropertyViews(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)


# Create your models here.
