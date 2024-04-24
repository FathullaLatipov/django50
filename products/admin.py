from django.contrib import admin

from products.models import CategoryModel, ProductsModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['category_name', 'id', 'created_at']
    list_filter = ['created_at']
    list_display = ['id', 'category_name', 'created_at']
    ordering = ['-id']


admin.site.register(ProductsModel)