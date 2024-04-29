from django.shortcuts import render, redirect

from products.models import ProductsModel, CategoryModel


def home_page(request):
    products = ProductsModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, template_name='index.html', context=context)


def search_products(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')

        try:
            exact_product = ProductsModel.objects.get(product_name__icontains=get_product)
            print(f'Yeeeah we found for you this product {exact_product}')
            return redirect(f'product/{exact_product.id}')
        except:
            print('Not Found')
            return redirect('/')
