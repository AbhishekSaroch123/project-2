# @api_view(['GET'])
# def index(request):
#     userData=User.objects.all()
#     serializer=UserSerializer(userData)
#     print(serializer.data)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')



# class IndexView(generic.ListView):
#     template_name = "project2/index.html"
#     context_object_name = "latest_users_list"
#     def get_queryset(self):
#         return User.objects.all()



     
    

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