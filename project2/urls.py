from django.urls import path
from . import views
app_name = "project2"

urlpatterns = [
     path('api/create_user/', views.create_user, name='create_user_api'), 
     path('api/users/', views.get_users, name='get_users_api'),
]
