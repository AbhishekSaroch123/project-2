from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view

# api view helps tah our create_user function will only make post requests
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()  # Fetch all user objects from the database
    serializer = UserSerializer(users, many=True)  # Serialize the queryset of users
    return Response(serializer.data)  # Return the serialized data as a JSON response
    


  



    











