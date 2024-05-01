from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from products.views import home_page, search_products, single_product, MyFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('search', search_products),
    path('product/<int:id>', single_product),
    path('register', MyFormView.as_view())
    # login
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
