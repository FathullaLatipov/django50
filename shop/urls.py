from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from products.views import home_page, search_products, single_product, MyFormView, MyLoginFormView, logout, LogoutEnter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('search', search_products),
    path('product/<int:id>', single_product),
    path('register', MyFormView.as_view()),
    path('login', MyLoginFormView.as_view()),
    path('logout', logout),
    path('logout-enter', LogoutEnter.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
