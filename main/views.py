from django.shortcuts import render
from .models import Sales, VerifyPhone, Color, ProductColor, Size, ProductSize, Product, ProductImage, ProductVideo, \
    District, Order, OrderItem
from .serializers import SaleSerializer, VerifyPhoneSerializer, ProductSerializer, ColorSerializer, \
    ProductColorSerializer, SizeSerializer, ProductImageSerializer, ProductVideoSerializer, DistrictSerializer, \
    OrderSerializer, OrderItemSerializer, ProductSizeSerializer
from rest_framework import generics


class SaleList(generics.ListAPIView):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer


class VerifyPhoneList(generics.ListAPIView):
    queryset = VerifyPhone.objects.all()
    serializer_class = VerifyPhoneSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ColorList(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ProductColorList(generics.ListAPIView):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer


class SizeList(generics.ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ProductSizeList(generics.ListAPIView):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class ProductImageList(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductVideoList(generics.ListAPIView):
    queryset = ProductVideo.objects.all()
    serializer_class = ProductVideoSerializer


class DistrictList(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemList(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
