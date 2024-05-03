from django.shortcuts import render, redirect

from products.models import ProductsModel, CategoryModel


def home_page(request):
    products = ProductsModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, template_name='index.html', context=context)


def search_products(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')  # То что искал пользователь iphone

        try:
            exact_product = ProductsModel.objects.get(product_name__icontains=get_product)
            print(f'Yeeeah we found for you this product {exact_product}')
            return redirect(f'product/{exact_product.id}')  # 5
        except:
            print('Not Found')
            return redirect('/')


#  Function Based View - FBV
def single_product(request, id):
    product = ProductsModel.objects.get(id=id)  # 5
    context = {'product': product}
    return render(request, 'single-product.html', context=context)


# RegisterForm
# LoginForm

from django.views.generic import FormView, CreateView
from products.forms import RegisterForm, LoginForm


class MyFormView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login'


# Login html logina
class MyLoginFormView(CreateView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'
