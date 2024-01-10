#django import 
from django.contrib.auth.models import User

#rest framework import
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url","username","email")
