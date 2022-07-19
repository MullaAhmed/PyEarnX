from django.http import HttpResponse
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


class VideoListAllApiView(generics.ListAPIView):
    serializer_class=VideoSerializer
    permission_classes=(permissions.IsAuthenticated,)
    
    
    def get_queryset(self):
        return Video.objects.filter()


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

        username=self.request.user
        user=UserProfile.objects.filter(wallet_address=username)
        
        like_history=list(user.values('like_history'))[0]['like_history']
        like_history.append(str(uid))
        user.update(like_history=like_history)
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

        username=self.request.user
        user=UserProfile.objects.filter(wallet_address=username)
        like_history=list(user.values('like_history'))[0]['like_history']
        like_history.remove(str(uid))
        user.update(like_history=like_history)

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

        username=self.request.user
        user=UserProfile.objects.filter(wallet_address=username)
        vote_history=list(user.values('vote_history'))[0]['vote_history']
        vote_history.append(str(uid))
        user.update(vote_history=vote_history)
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


        username=self.request.user
        user=UserProfile.objects.filter(wallet_address=username)
        watch_history=list(user.values('watch_history'))[0]['watch_history']
        watch_history.append(str(uid))
        user.update(watch_history=watch_history)
        return(data)


class VideoCheckApiView(APIView):
    serializer_class=VideoSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('video_name')

    def get(self,request,video_name,format=None):
        uid = self.kwargs.get(self.lookup_field)
        data= Video.objects.filter(video_name=uid)
      
        result={}
        username=self.request.user
        print(username)
     
        user=UserProfile.objects.filter(wallet_address=username)
        print(user)
        watch_history=list(user.values('watch_history'))[0]['watch_history']
        if str(uid) in watch_history:
            result['watch_histroy']=(True)
        else:
             result['watch_histroy']=(False)
        vote_history=list(user.values('vote_history'))[0]['vote_history']
        if str(uid) in vote_history:
             result['vote_histroy']=(True)
        else:
             result['vote_histroy']=(False)
        like_history=list(user.values('like_history'))[0]['like_history']
        if str(uid) in like_history:
             result['like_histroy']=(True)
        else:
             result['like_histroy']=(False)
        
        print(result)
        return Response(result,status=status.HTTP_200_OK)
