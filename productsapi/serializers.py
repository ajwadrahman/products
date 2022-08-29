from rest_framework import serializers
from productsapi.models import Products

class ProductsSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()

    #
    # def validate(self,data):
    #     price=data.get("price")
    #     if price<0:
    #         raise serializers.ValidationError("invalid price")
    #     return data

class ProductsModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        fields = "__all__"     #  for importing all products





