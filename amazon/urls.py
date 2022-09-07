from django.contrib import admin
from django.urls import path
from amazon.views import aboutUs, amazonProducts , contactUs

urlpatterns = [

    # create amazon.views urls

    path('aboutus', aboutUs),
    path('contactus', contactUs),
    path('products', amazonProducts)
 
]
