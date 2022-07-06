from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from .serializers import *
from rest_framework import viewsets,filters,generics,permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser

# Create your views here.

class UserProfileApiView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    

    def post(self,request,format=None):
        serializer= UserProfileSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


class UserProfileListApiView(generics.ListAPIView):
    serializer_class=UserProfileSerializer
    permission_classes=(permissions.IsAuthenticated,)
   
    def get_queryset(self):
        return UserProfile.objects.filter()


class UserProfileDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UserProfileSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('wallet_address')
   
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        return UserProfile.objects.filter(wallet_address=uid)


class ProjectFormApiView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser,FileUploadParser]

    def post(self,request,format=None):
        serializer= ProjectFormSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


class ProjectFormListApiView(generics.ListAPIView):
    serializer_class=ProjectFormSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('wallet_address')
   
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        return ProjectForm.objects.filter(wallet_address=uid)


class ProjectFormDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ProjectFormSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('project_name')
   
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        return ProjectForm.objects.filter(project_name=uid)


class VideoApiView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser,FileUploadParser]
   
    def post(self,request,format=None):    
        serializer= VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    


class VideoListApiView(generics.ListAPIView):
    serializer_class=VideoSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('project_name')
    
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        
        return Video.objects.filter(project_name=uid)


class VideoDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=VideoSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('video_name')
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        return Video.objects.filter(video_name=uid)

class VideoLikeApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=VideoSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('video_name')
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        data= Video.objects.filter(video_name=uid)
        likes=list(data.values('likes'))[0]['likes']
        data.update(likes=likes+1)
        return(data)

class VideoDisLikeApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=VideoSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('video_name')
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        data= Video.objects.filter(video_name=uid)
        likes=list(data.values('likes'))[0]['likes']
        data.update(likes=likes-1)
        return(data)


class VideoVoteApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=VideoSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('video_name')
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        data= Video.objects.filter(video_name=uid)
        votes=list(data.values('votes'))[0]['votes']
        data.update(votes=votes+1)
        return(data)

class VideoViewsApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=VideoSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('video_name')
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        data= Video.objects.filter(video_name=uid)
        views=list(data.values('views'))[0]['views']
        data.update(views=views+1)
        return(data)