from django.shortcuts import render
from product.models import Product
# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'web/home.html', {'products': products})


