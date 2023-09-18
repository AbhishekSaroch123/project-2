from django.urls import path

from . import views
app_name = "project2"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('<str:username>_complete_information/', views.user_information, name='user_information'),
]
