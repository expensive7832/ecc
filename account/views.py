from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import userSerializer, loginSerializer
# Create your views here.
@api_view(['POST'])
def Signup(request):
    
    newuser = userSerializer(data=request.data)

    if newuser.is_valid():
        newuser.save()
        res = {
            "message": "signup successful"
        }
        return Response(data=res)
    else:
        res = {
            "message": "error",
            "info": newuser.errors
        }
        return Response(data=res)
    


@api_view(['POST'])
def Login(request):
    data = request.data
    
    serializer = loginSerializer(data)

    user = serializer.checkInfo(serializer.data)

    if user is None:
        res ={
            "message": "error"
        }
        return Response(data=res)

    else:
        res = {
            "message": "success",
            "info": user
        }
        return Response(data=res)

        