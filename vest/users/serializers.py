from rest_framework import serializers
from users.models import VestUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VestUser
        fields = (
            'username'
        )
