
from django.urls import path, include
from .views import ProductViewSet, OrderViewSet, OrderItemViewSet, ReviewsViewSet, ShippingAddressViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


api_router = routers.DefaultRouter()
api_router.register('products', ProductViewSet)
api_router.register('orders', OrderViewSet)
api_router.register('order-items', OrderItemViewSet)
api_router.register('shipping-address', ShippingAddressViewSet)
api_router.register('reviews', ReviewsViewSet)

urlpatterns = [
    path('users/', include('api_auth.urls')),
    path('', include(api_router.urls)),
]
