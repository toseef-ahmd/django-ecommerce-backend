from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import serializers
from . import models
from django_filters.rest_framework import DjangoFilterBackend
import django_filters


class ProductFilter(django_filters.FilterSet):
    rating = django_filters.NumberFilter(field_name="rating", lookup_expr='gte')
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = models.Product
        fields = ['name', 'brand', 'category', 'rating', 'min_price', 'max_price']


class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    #search_fields = ['name', 'category', 'brand']

    '''def post(self, request):
        if request.method == 'POST':
            update()'''


class OrderViewSet(ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        order_items = self.request.data['orderItems']
        user = self.request.user
        data = self.request.data

        if order_items:
            order = serializer.save(user=user, delivery_address=data['shipping_address'])

            # Save Shipping Address
            shipping = models.ShippingAddress.objects.create(
                order=order,
                address=data['shipping_address'],
                city=data['shipping_city'],
                postalCode=data['shipping_postcode'],
                country=data['shipping_country'],
                shippingCost=self.request.data['shipping_cost']
            )

            # Save Order Item
            for item in order_items:
                product = models.Product.objects.get(id=item['product'])
                order_item = models.OrderItem.objects.create(
                    product=product,
                    order=order,
                    name=item['name'],
                    quantity=item['qty'],
                    price=item['price'],
                    image=item['image']
                )

                product.countInStock -= order_item.quantity
                product.save()

    def get_queryset(self):
        user = self.request.user
        print(user)
        full_access = user.is_superuser or user.is_staff
        if not full_access:
            return models.Order.objects.filter(user=user.id)
        return models.Order.objects.all()


class OrderItemViewSet(ModelViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer


class ShippingAddressViewSet(ModelViewSet):
    queryset = models.ShippingAddress.objects.all()
    serializer_class = serializers.ShippingAddressSerializer


class ReviewsViewSet(ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewsSerializer

