from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def aboutUs(request):
    return render(request, "amazon/aboutUs.html")

def contactUs(request):
    return render(request, "amazon/contactUs.html")

def amazonProducts(request):
    products= [
        {"id":1, "name":"mobile", "image":"p1.png"},
        {"id":2, "name":"laptop", "image":"p2.png"},
        {"id":3, "name":"ps5", "image":"p3.png"}
    ]

    content = {"products":products}
    # send these data to a template --> to display it
    return render (request, "amazon/products.html", content)