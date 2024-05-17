from django.urls import path
from .views import SizeList, ProductList, OrderList, DistrictList, OrderItemList, SaleList, \
    ProductImageList, ProductVideoList, ColorList, ProductColorList, VerifyPhoneList

urlpatterns = [
    path('size/', SizeList.as_view(), name='size-list'),
    path('product/', ProductList.as_view(), name='product-list'),
    path('order/', OrderList.as_view(), name='order-list'),
    path('district/', DistrictList.as_view(), name='district-list'),
    path('product-image/', ProductImageList.as_view(), name='product-image-list'),
    path('product-video/', ProductVideoList.as_view(), name='product-video-list'),
    path('color/', ColorList.as_view(), name='color-list'),
    path('product-color/', ProductColorList.as_view(), name='product-color-list'),
    path('verifyphone/', VerifyPhoneList.as_view(), name='verifyphone-list'),
    path('order-image/', OrderItemList.as_view(), name='order-image-list'),
    path('sale/', SaleList.as_view(), name='sale-list'),

]

