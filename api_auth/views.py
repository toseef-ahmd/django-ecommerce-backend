from django.contrib.auth.hashers import make_password
from .models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from . import serializers


class AuthTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_object(self):
        if self.kwargs['pk'] == 'me':
            return self.request.user
        else:
            return super().get_object()

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        return super(UserViewSet, self).get_permissions()

    def perform_create(self, serializer):
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            username = self.request.data['email']
            serializer.save(password=password, username=username)
        else:
            serializer.save()

    def perform_update(self, serializer):
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()
