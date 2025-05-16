from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
import requests, os
from .models import UserQuery
from .serializers import UserQuerySerializer


# Create your views here.
class GetWeather(APIView):
    permission_classes=[IsAuthenticated] #if the user is authenticated

    def get(self,request,city):

        user = request.user # get the user

    # caching to check if the weather is in the cache or not
        key = f"weather_{city.lower()}"
        data = cache.get(key) 

        if not data:
            api_key = os.getenv('OPENWEATHER_API_KEY')
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url) #get response
            

            if response.status_code != 200:
                return Response(response, status=response.status_code)
        
            data = response.json()
            cache.set(key, data, timeout=600)  #add to cache
        try:
            user_query=UserQuery(user=user,user_query=city)
            user_query.save() #save to the database
        except:
            pass #query already saved 

        return Response(data)
    
class GetQueries(APIView):
    permission_classes=[IsAuthenticated] #if the user is authenticated

    def get(self,request):

        user = request.user # get the user
        queries = UserQuery.objects.filter(user=request.user)
        serializer = UserQuerySerializer(queries, many=True)
        return Response(serializer.data)

      
        

        
