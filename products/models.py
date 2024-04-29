from django.db import models


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductsModel(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ManyToManyField(CategoryModel)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    image = models.FileField(upload_to='product_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'