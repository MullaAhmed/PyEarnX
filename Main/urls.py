from django.urls import path,include
from .views import *
from rest_framework import routers


urlpatterns = [

    path("userprofile/",UserProfileApiView.as_view()),
    path("listuserprofile/",UserProfileListApiView.as_view()),
    path("userprofile/<slug:wallet_address>/",UserProfileDetailApiView.as_view()),

    path("projectform/",ProjectFormApiView.as_view()),
    path("listprojectform/<slug:wallet_address>/",ProjectFormListApiView.as_view()),
    path("projectform/<slug:project_name>/",ProjectFormDetailApiView.as_view()),

    path("video/",VideoApiView.as_view()),
    path("listvideos/<slug:project_name>/",VideoListApiView.as_view()),
    path("video/<slug:video_name>/",VideoDetailApiView.as_view()),

    path("video/like/<slug:video_name>/",VideoLikeApiView.as_view()),
    path("video/dislike/<slug:video_name>/",VideoDisLikeApiView.as_view()),
    path("video/vote/<slug:video_name>/",VideoVoteApiView.as_view()),
    path("video/views/<slug:video_name>/",VideoViewsApiView.as_view()),
    
    path("video/check/<slug:video_name>/",VideoCheckApiView.as_view()),

    ]