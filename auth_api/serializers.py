from auth_api.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        """
        Saving username to token
        """
        token = super().get_token(user)
        token["username"] = user.username
        return token


class UserSerializer(serializers.ModelSerializer):
    def validate_email(self, value: str) -> str:
        """
        Convert email to lowercase
        """
        return value.lower()

    def validate_username(self, value: str) -> str:
        """
        Convert username to lowercase
        """
        return value.lower()

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(raw_password=password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ("id", "first_name", "email", "password", "username")
        extra_kwargs = {"password": {"write_only": True}}
