from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, validators
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': _('Invalid Email or Password')
    }

    def validate(self, attrs):
        data = super().validate(attrs)

        return data


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(UserSerializer, self).__init__(*args, **kwargs)

    isAdmin = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(min_length=8, required=False, write_only=True)
    old_password = serializers.CharField(required=False, write_only=True)
    email = serializers.EmailField(required=True, validators=[validators.UniqueValidator(queryset=User.objects.all(), message="Email Address already exists",)])
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'old_password', 'first_name', 'last_name', 'isAdmin', 'avatar']

    def get_isAdmin(self, obj):
        return obj.is_staff

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"error_message": "Current password is not correct"})
        return value

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)

        return value
