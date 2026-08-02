from rest_framework import serializers

from .models import User
from .services import register_user


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User

        fields = (
            "email",
            "username",
            "password",
            "confirm_password",
        )

    def validate_email(self, value):

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )

        return value.lower()

    def validate(self, attrs):

        if attrs["password"] != attrs["confirm_password"]:

            raise serializers.ValidationError(
                {
                    "confirm_password":
                    "Passwords do not match."
                }
            )

        return attrs

    def create(self, validated_data):

        validated_data.pop("confirm_password")

        return register_user(
            email=validated_data["email"],
            username=validated_data.get("username"),
            password=validated_data["password"],
        )