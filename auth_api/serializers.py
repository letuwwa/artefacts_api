from auth_api.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
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
