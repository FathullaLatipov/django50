from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from products.views import home_page, search_products, single_product, MyFormView, MyLoginFormView, logout, LogoutEnter, \
    category_page, add_product_to_cart, user_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('search', search_products),
    path('product/<int:id>', single_product),
    path('category/<int:id>', category_page),
    path('register', MyFormView.as_view()),
    path('login', MyLoginFormView.as_view()),
    path('logout', logout),
    path('logout-enter', LogoutEnter.as_view()),
    path('add_to_cart/<int:id>', add_product_to_cart),
    path('user_cart', user_cart),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
