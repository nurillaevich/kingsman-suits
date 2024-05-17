from django.db import models
from account.models import User


class Sales(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField()
    percent = models.IntegerField()
    discount_name = models.CharField(max_length=50)

    def __str__(self):
        return self.discount_name


class VerifyPhone(models.Model):
    phone = models.CharField(max_length=15)
    code = models.CharField(max_length=15)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)


class ProductColor(models.Model):
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Size(models.Model):
    size_name = models.CharField(max_length=50)


class ProductSize(models.Model):
    size_id = models.ForeignKey(Size, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()


class ProductVideo(models.Model):
    video = models.FileField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class District(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    address = models.TextField()
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
