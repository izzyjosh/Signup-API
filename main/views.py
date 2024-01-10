#django import 
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#rest_framework import 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view

#my import 
from .serializers import UserSerializer


class UserList(APIView):

    def get(self,request:Request,format=None):
        userlist = User.objects.all()
        serializer = UserSerializer(userlist,many=True,context={"request":request})

        return Response(serializer.data,status=status.HTTP_200_OK)


class UserDetail(APIView):

    def get_object(self,pk):
        try:
            user = get_object_or_404(User,pk=pk)
        except user.DoesNotExist:
            return HttpResponse(status="404 Not Found")

    def get(self,request:Request,pk,format=None):
        user = self.get_object(pk)

        serializer = UserSerializer(user)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request:Request,pk,format=None):

        user = self.get_object(pk)

        serializer = UserSerializer(user,request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


class Signup(APIView):
    def post(self,request:Request,format=None):
        user = UserSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HHTP_400_BAD_REQUEST)

@api_view(["POST"])
def signin(request):
    
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username,password)

    if user is not None:
        return Response(status=status.HTTP_200_OK)
