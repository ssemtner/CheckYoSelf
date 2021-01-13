from django.shortcuts import render, get_object_or_404

from .models import Product


# Create your views here.
def index(request):
    element_list = Product.objects.order_by('number')
    return render(request, 'Elements/index.html', {'element_list': element_list})


def detail(request, element_name):
    obj = get_object_or_404(Product, element=element_name)
    return render(request, 'Elements/detail.html', {'element': obj})
