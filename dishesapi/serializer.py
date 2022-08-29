from rest_framework import serializers
from dishesapi.models import Dishes

class DishSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    category=serializers.CharField()
    rating=serializers.IntegerField()

class DishesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        field = "__all__"