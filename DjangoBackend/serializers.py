from rest_framework import serializers
from .models import Items, User

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['item_id', 'image','name', 'price', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','username', 'passw']