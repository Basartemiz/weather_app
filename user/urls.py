from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:city>/', views.GetWeather.as_view(), name='get_weather'),  
    path('queries/', views.GetQueries.as_view(), name='get_queries'),  
]