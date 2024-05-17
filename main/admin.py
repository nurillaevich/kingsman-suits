from django.contrib import admin
from .models import Sales, VerifyPhone, Color, ProductColor, Size, ProductSize, Product, ProductImage, ProductVideo, \
    District, Order, OrderItem

admin.site.register(ProductImage)
admin.site.register(Sales)
admin.site.register(VerifyPhone)
admin.site.register(Color)
admin.site.register(ProductColor)
admin.site.register(Size)
admin.site.register(ProductSize)
admin.site.register(Product)
admin.site.register(ProductVideo)
admin.site.register(District)
admin.site.register(Order)
admin.site.register(OrderItem)


