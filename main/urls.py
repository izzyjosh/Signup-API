#rest_framework import 
from rest_framework.urlpatterns import format_suffix_patterns

#django import 
from django.urls import path

#my import 
from . import views


urlpatterns = [
        path("",views.UserList.as_view(),name="userlist"),
        path("user/<int:pk>/",views.UserDetail.as_view(),name="user-detail"),
        path("signup/",views.Signup.as_view(),name="signup"),
        path("signin/",views.signin,name="signin"),
        ]

urlpatterns = format_suffix_patterns(urlpatterns)
