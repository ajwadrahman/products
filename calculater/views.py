from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class Addview(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response({"msg":res})

class Subview(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        resp=n1-n2

        return Response({"msg":resp})

class Multview(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        respo=n1*n2
        return Response({"msg":respo})

# word count
class Countview(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        words=text.split(" ")
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response(data=wc)
