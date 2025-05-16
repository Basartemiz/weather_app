from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.CreateUser.as_view(), name='create_user'),  
    path('queries/', views.GetQueries.as_view(), name='get_queries'),  
]