from rest_framework import serializers
from .models import Sales, VerifyPhone, Color, ProductColor, Size, ProductSize, Product, ProductImage, ProductVideo, \
    District, Order, OrderItem
from account.serializers import CustomUserSerializer


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


class VerifyPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyPhone
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ProductColorSerializer(serializers.ModelSerializer):
    color_id = ColorSerializer()
    product_id = ProductSerializer()

    class Meta:
        model = ProductColor
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ProductSizeSerializer(serializers.ModelSerializer):
    size_id = SizeSerializer()
    product_id = ProductSerializer()

    class Meta:
        model = ProductSize
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductVideoSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()

    class Meta:
        model = ProductVideo
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']


class OrderSerializer(serializers.ModelSerializer):
    user_id = CustomUserSerializer()
    district_id = DistrictSerializer()

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']


class OrderItemSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer()
    product_id = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']

