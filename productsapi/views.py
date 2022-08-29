from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from productsapi.models import Products
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from productsapi.serializers import ProductsSerializer
from productsapi.serializers import ProductsModelSerializer

class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        if "rating" in request.query_params:
            qs=qs.filter(rating=request.query_params.get("rating"))
        if "name" in request.query_params:
            qs=qs.filter(name__contains=request.query_params.get("name"))
        serializer=ProductsSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=ProductsSerializer(data=request.data)
        if serializer.is_valid():
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors)

class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=ProductsSerializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        product.delete()
        return Response({"msg":"deleted"})

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.filter(id=id)
        serializer=ProductsSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            # print(serializer.validated_data)
            qs.update(**serializer.validated_data)
            # qs.name=serializer.validated_data.get("name")
            # qs.category= serializer.validated_data.get("category")
            # qs.price = serializer.validated_data.get("price")
            # qs.rating = serializer.validated_data.get("rating")
            # qs.save()
            return Response({"msg":"updated"})
        else:
            return Response(data=serializer.errors)

class ProductModelView(APIView):
    def get(self,*args,**kwargs):
        qs=Products.objects.all()
        serializer=ProductsModelSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=ProductsModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductDetailModelView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=ProductsModelSerializer(qs)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        serializer=ProductsModelSerializer(instance=product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.data)












#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         instance=Products.objects.filter(id=id)
#         serializer=ProductsSerializer(data=request.data)
#         if serializer.is_valid():
#             # instance.name=serializer.validated_data.get("name")
#             # instance.category = serializer.validated_data.get("category")
#             # instance.price = serializer.validated_data.get("price")
#             # instance.rating= serializer.validated_data.get("rating")
#             #
#             # instance.save()
#             instance.update(**serializer.validated_data)
#             return Response(data=serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         instance=Products.objects.get(id=id)
#         serializer=ProductsSerializer(instance)
#         instance.delete()
#         return Response({"msg":"deleted"},status=status.HTTP_404_NOT_FOUND)
#
#
# class ProductModelView(APIView):
#     def get(self,request,*args,**kwargs):
#         qs=Products.objects.all()
#         if "category" in request.query_params:
#             qs = qs.filter(category__contains=request.query_params.get("category"))
#         if "price_gt" in request.query_params:
#             qs=qs.filter(price__gt=request.query_params.get("price_gt"))
#
#         serializer=ProductsModelSerializer(qs,many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)
#     def post(self,request,*args,**kwargs):
#         serializer=ProductsModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class ProductDetailModelView(APIView):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         qs=Products.objects.get(id=id)
#         serializer=ProductsModelSerializer(qs)
#         return  Response(data=request.data,status=status.HTTP_200_OK)
#
#     def put(self,request,*args,**kwargs):
#         id = kwargs.get("id")
#         object = Products.objects.get(id=id)
#         serializer=ProductsModelSerializer(data=request.data,instance=object)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
#
#
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#
#         instance=Products.objects.get(id=id)
#         serializer=ProductsSerializer(instance)
#         instance.delete()
#         return Response(data=serializer.data)
#
# class ProductViewsetView(ViewSet):
#     def list(self,request,*args,**kwargs):
#         qs=Products.objects.all()
#         serializer=ProductsModelSerializer(qs,many=True)
#         return Response(data=serializer.data)
#
#     def create(self,requet,*args,**kwargs):
#         serializer=ProductsModelSerializer(data=requet.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#     def retrive(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         qs=Products.objects.get(id=id)
#         seriaizer=ProductsModelSerializer(qs)
#         return Response(data=seriaizer.data)
#
#     def update(self,request,*args,**kwargs):
#         id = kwargs.get("pk")
#         object = Products.objects.get(id=id)
#         serializer=ProductsModelSerializer(instance=object,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#     def destroy(self,request,*args,**kwargs):
#         id = kwargs.get("pk")
#         instance = Products.objects.get(id=id)
#         instance.delete()
#         return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
#
# class ProductModelViewSetView(ModelViewSet):
#     serializer_class = ProductsModelSerializer
#     queryset=Products.objects.all
#
