from django.urls import path

from . import views

urlpatterns = [
   path('inquiry/<int:property_id>/', views.inquiry, name='inquiry')

] 