from django.http import JsonResponse, HttpResponse,request
from django.views import generic
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import User
from .forms import UserCreationForm
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# api view helps tah our create_user function will only make post requests
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class IndexView(generic.ListView):
#     template_name = "project2/index.html"
#     context_object_name = "latest_users_list"
#     def get_queryset(self):
#         return User.objects.all()


def index(request):
    userData=User.objects.all()
    data= {
        "Users":list(userData.values())
    }
    return JsonResponse(data)

     
    

# class UserInformationView(generic.DetailView):

#     model = User
#     template_name = 'project2/user_information.html'  # Create a user_information.html template
#     context_object_name = 'user'  # The name to use in the template for the user object

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.get_object()  # Get the user object
#         # Retrieve data from related models and add it to the context
#         context['analytics'] = Analytics.objects.filter(user=user).first()
#         context['resources'] = Resources.objects.filter(user=user)
#         context['education'] = Education.objects.filter(user=user)
#         context['skills'] = Skills.objects.filter(user=user)
#         context['interests'] = Interests.objects.filter(user=user)
#         context['people_also_viewed'] = PeopleAlsoViewed.objects.filter(user=user)
#         context['people_you_may_know'] = PeopleYouMayKnow.objects.filter(user=user)

#         return context

 

# def create_user(request):
#          if request.method == 'POST':
#           form = UserCreationForm(request.POST)
#           if form.is_valid():
#            form.save()  # Save the user data to the database
#            return redirect('project2:index')  # Redirect to the index page after user creation
#          else:
#           form = UserCreationForm()

#          return render(request, 'project2/create_user.html', {'form': form})

  


# def create_user(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             # ... (rest of your code for creating a user)
#             user = User.objects.create(
#                 name=data['name'],
#                 role=data['role'],
#                 location=data['location'],
#                 connections=data['connections'],
#                 profile_language=data['profile_language'],
#                 public_profile_url=data['public_profile_url']
#             )
#             user.save()
#             response_data = {'message': 'User created successfully', 'userData':user}
#             return JsonResponse(response_data, status=201)
#         except json.JSONDecodeError:
#             error_response = {'error': 'Invalid JSON data,Hitting On this line'}
#             return JsonResponse(error_response, status=400)
#     elif request.method == 'GET':
#         # Handle GET request by rendering a form or returning a response
#         return render(request, 'project2/user_creation_form.html')
#     else:
#         return HttpResponse(status=405)  # Method Not Allowed for other HTTP methods
    











