from django.shortcuts import render

from .models import Product


# Create your views here.
def index(request):
    element_list = Product.objects.order_by('element')
    return render(request, 'Elements/index.html', {'element_list': element_list})
