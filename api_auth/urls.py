
from django.urls import path, include
from rest_framework import routers

from .views import AuthTokenObtainPairView, UserViewSet

get_users = routers.DefaultRouter()
get_users.register('', UserViewSet)

urlpatterns = [
    path('login/', AuthTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(get_users.urls)),

]
