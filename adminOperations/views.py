from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework.permissions import BasePermission
from rest_framework import status
from user.models import UserQuery
from user.serializers import UserQuerySerializer
from .serializers import UserSerializer

# Create your views here.

#class that checks if user is admin
class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='admin').exists()

class GetQueries(APIView):

    permission_classes=[IsAdmin] #only admins can acces this 

    def get(self,request):
     
        queries=UserQuery.objects.all() #get all the user queries
        serializer=UserQuerySerializer(queries,many=True) #serialize all the queries
        return Response(serializer.data,status=status.HTTP_200_OK)
        


class CreateUser(APIView):

    permission_classes=[IsAdmin] #only admins can acces this 

    def post(self,request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        