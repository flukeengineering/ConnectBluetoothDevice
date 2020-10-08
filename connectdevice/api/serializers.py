from rest_framework import serializers
from connectdevice.models import ConnectDevice
from django.contrib.auth.models import User

class ConnectDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectDevice
        fields = ('__all__')

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user