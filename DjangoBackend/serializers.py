from rest_framework import serializers
from .models import Items, Posts

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['item_id', 'image','name', 'price', 'description']


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['post_id','user_id','title','datetime','message', 'reaction']