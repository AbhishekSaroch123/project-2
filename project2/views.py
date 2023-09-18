from django.http import HttpResponse
from django.views import generic
from .models import *
from django.shortcuts import render
class IndexView(generic.ListView):
    template_name = "project2/index.html"
    context_object_name = "latest_users_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return User.objects.all()
    


def user_information(request, username):
    try:
        user = User.objects.get(name=username)
    except User.DoesNotExist:
        # Handle the case where the user does not exist
        # You can raise a 404 error or display an appropriate message
        pass

    return render(request, 'user_information.html', {'user': user})