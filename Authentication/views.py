from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework import response,status,permissions
from django.contrib.auth import authenticate
# Create your views here.

class AuthUserAPIView(GenericAPIView):

    permission_classes=(permissions.IsAuthenticated,)

    def get(self,request):
        user=request.user
        serializer=RegisterSerializer(user)
        return response.Response({'user':serializer.data})

class RegisterAPIView(GenericAPIView):
    authentication_classes=[]
    serializer_class=RegisterSerializer

    def post(self,request):
        
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(GenericAPIView):
    authentication_classes=[]
    serializer_class=LoginSerializer

    def post(self,request):
        username=request.data.get('username',None)
        password="Pass@123"
        print(list(request.data.values())[0])

        user=authenticate(username=username,password=password)

        if user:
            serializer=self.serializer_class(user)
            return response.Response(serializer.data,status=status.HTTP_200_OK)
        else:
            # request_register(list(request.data.values())[0])
            # return HttpResponse(User.objects.filter())
            return response.Response({'message':'Invalid credentials try again'},status=status.HTTP_401_UNAUTHORIZED)

            

def request_register(username):
    import http.client
    import json

    conn = http.client.HTTPSConnection("127.0.0.1", 8000)
    payload = json.dumps({
    "username": username
    })
    headers = {
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/register/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return(data.decode("utf-8"))