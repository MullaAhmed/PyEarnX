from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from rest_framework import viewsets,filters,generics,permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser
import json
# Create your views here.


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

    def get_queryset(self):
        return ProjectForm.objects.filter()

class ProjectFormDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ProjectFormSerializer
    
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field=('project_name')
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        # print(ProjectForm.objects.all())
        return ProjectForm.objects.filter(project_name=uid)
