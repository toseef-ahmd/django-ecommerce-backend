from rest_framework import serializers
from .models import Product, Order, OrderItem, ShippingAddress, Review
from api_auth.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user')
    image = serializers.ImageField(default="images/sample.jpg")

    class Meta:
        model = Product
        fields = ['id', 'user', 'name', 'brand', 'category', 'description', 'rating', 'numReviews', 'price', 'countInStock', 'image', 'createdAt']


class ReviewsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user')

    class Meta:
        model = Review
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderItems(self, obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data

    def get_shippingAddress(self, obj):
        try:
            address = ShippingAddressSerializer(
                obj.shippingaddress, many=False).data
        except:
            address = False
        return address


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = '__all__'