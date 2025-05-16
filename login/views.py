from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group

# Create your views here.
class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)

        
        user = User.objects.create_user(username=username, password=password)

       
        user_group = Group.objects.get(name='user')
        user.groups.add(user_group)

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)