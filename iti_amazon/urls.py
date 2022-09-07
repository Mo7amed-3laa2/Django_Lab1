from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # getting url for amazon from amazon/urls.py file
    path('amazon/', include("amazon.urls")),


]
