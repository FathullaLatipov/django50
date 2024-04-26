from django.contrib import admin

from products.models import CategoryModel, ProductsModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['category_name', 'id', 'created_at']
    list_filter = ['created_at']
    list_display = ['id', 'category_name', 'created_at']
    ordering = ['-id']


@admin.register(ProductsModel)
class ProductsModelAdmin(admin.ModelAdmin):
    search_fields = ['product_name', 'id', 'created_at']
    list_filter = ['created_at']
    list_display = ['id', 'product_name', 'created_at']
    ordering = ['-id']

# admin.site.register(ProductsModel)
