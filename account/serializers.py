from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .managers import CustomUserManager
from rest_framework import serializers
from .models import CustomUser


class CustomObtainTokenPairSerializer(TokenObtainPairSerializer):
    serializer_class = CustomUserManager

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class CreateUserSerializer(serializers.ModelSerializer):
    """Serializer for user object"""

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def save(self):
        user = CustomUser(
            email=self.validated_data['email'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user