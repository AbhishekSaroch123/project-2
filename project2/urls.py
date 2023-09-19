from django.urls import path
from . import views
app_name = "project2"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('user/<int:pk>/', views.UserInformationView.as_view(), name='user-information'),
    path('create_user/', views.create_user, name='create-user'),
]