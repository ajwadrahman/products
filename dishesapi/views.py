from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from dishesapi.models import Dishes
from rest_framework.viewsets import ViewSet
# Create your views here.
from dishesapi.serializer import DishSerializer
from dishesapi.serializer import DishesModelSerializer

class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        if "name" in request.query_params:
            qs=qs.filter(name__contains=request.query_params.get("name"))
        if "category" in request.query_params:
            qs=qs.filter(category=request.query_params.get("category"))
        serializer=DishSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=DishSerializer(data=request.data)
        if serializer.is_valid():
            Dishes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class DishesDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Dishes.objects.get(id=id)
        serializer=DishSerializer(qs)
        return Response(data=serializer.data)

    def delete(self,*args,**kwargs):
        id=kwargs.get("id")
        dish=Dishes.objects.get(id=id)
        dish.delete()
        return Response({"msg":"deleted"})

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Dishes.objects.filter(id=id)
        serializer=DishSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            qs.update(**serializer.validated_data)
            return Response({"msg":"updated"})
        else:
            return Response(data=serializer.errors)


