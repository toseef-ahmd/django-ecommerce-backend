from django.db.models import signals
from django.dispatch import receiver
from .models import *
from backend.settings import BASE_URL, MEDIA_URL
from algoliasearch.search_client import SearchClient
from .serializers import ProductSerializer

'''
client = SearchClient.create('L2OFO6L85D', '8a52566fcd99f5fbfa71cf89890d548a')
index = client.init_index('proshop_products')
index2 = client.init_index('proshop_product_categories')


# post_save method
@receiver(signals.post_save, sender=Product)
def create_product(sender, instance, *args, **kwargs):
    serializer = ProductSerializer(instance)

    image = str(serializer.data["image"])
    if image == "None":
        image = "/images/sample.jpg"

    category = Category.objects.get(pk=serializer.data["category"])
    brand = Brand.objects.get(pk=serializer.data["brand"])

    print(category.name)

    product = [
        {
            'objectID': serializer.data["id"],
            'name': serializer.data["name"],
            'brand': brand,
            'categories': category,
            'description': serializer.data["description"],
            'rating': float(serializer.data["rating"]),
            'numReviews': float(serializer.data["numReviews"]),
            'price': float(serializer.data["price"]),
            'countInStock': int(serializer.data["countInStock"]),
            'image': BASE_URL + image,
            'createdAt': serializer.data["createdAt"]
        }
    ]

    #print(product)
    index.save_objects(product, {'autoGenerateObjectIDIfNotExist': True})'''

