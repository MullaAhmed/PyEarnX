from re import I
from django.urls import path
from Authentication import views 
urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(),name="Register"), # Creates Users
    path('login/', views.LoginAPIView.as_view(),name="Login"), # Creates toekn
    path('user/', views.AuthUserAPIView.as_view(),name="User"), # Returns token
]
