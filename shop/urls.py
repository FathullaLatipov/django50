from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from products.views import home_page, search_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('search', search_products, name='search-product')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
