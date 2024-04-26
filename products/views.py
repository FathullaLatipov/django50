from django.shortcuts import render

from products.models import ProductsModel, CategoryModel


def home_page(request):
    products = ProductsModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, template_name='index.html', context=context)
