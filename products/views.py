from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.views.generic import FormView, CreateView, TemplateView
from products.forms import RegisterForm, LoginForm
from products.models import ProductsModel, CategoryModel, CartModel


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


class MyFormView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login'


# Login html logina
class MyLoginFormView(CreateView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'


def logout(request):
    auth_logout(request)
    return redirect('/')


class LogoutEnter(TemplateView):
    template_name = 'logout.html'


def category_page(request, id):  # 4
    categories = CategoryModel.objects.get(id=id)  # 4 -> Slaves
    products = ProductsModel.objects.filter(category=categories)  # 4 -> Products

    context = {'categories': categories, 'products': products}
    return render(request, template_name='category_products.html', context=context)


def add_product_to_cart(request, id):
    if request.method == 'POST':
        checker = ProductsModel.objects.get(id=id)  # Один какой то продукт 4
        #         4.20         4.30
        if checker.count >= int(request.POST.get('pr_count')):  # кол-во товара
            CartModel.objects.create(user_id=request.user.id,
                                     user_product=checker,
                                     user_product_quantity=int(request.POST.get('pr_count'))).save()
            return redirect('/user_cart')
        else:
            # Поработать с message
            return redirect('/')

from products.handler import bot

def user_cart(request):
    # Если в таблице Корзина есть пользователь с определенным id от он нам вернет все его данные
    cart = CartModel.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        main_text = 'Новый заказ'

        for i in cart:
            main_text += f'Товар: {i.user_product}\n' \
                         f'Кол-во: {i.user_product_quantity}\n' \
                         f'ID Пользователя: {i.user_id}\n' \
                         f'Цена: {i.user_product.price}\n'
            bot.send_message(-1002089507736, main_text)
            cart.delete()
            return redirect('/')
    else:
        return render(request, 'cart.html', {'cart': cart})
