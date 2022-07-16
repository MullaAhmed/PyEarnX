from sre_constants import MAX_UNTIL
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):


    class Meta:
        model=User
        fields=('wallet_address','token','is_staff')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):


    class Meta:
        model=User
        fields=('wallet_address','token','is_staff')

        read_only_fields=['token']

