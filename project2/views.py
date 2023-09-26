from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import *
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_instance = user_serializer.save()  # Save the user instance

            education_data = request.data.get('education_set', [])
            education_serializer = EducationSerializer(data=education_data, many=True)
            if education_serializer.is_valid():
                education_serializer.save(user=user_instance)
            else:
                return Response(education_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

          
            skills_data = request.data.get('skills_set', [])
            skills_serializer = SkillsSerializer(data=skills_data, many=True)
            if skills_serializer.is_valid():
                skills_serializer.save(user=user_instance)
            else:
                return Response(skills_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            interests_data = request.data.get('interests_set', [])
            interests_serializer = InterestsSerializer(data=interests_data, many=True)
            if interests_serializer.is_valid():
                interests_serializer.save(user=user_instance)
            else:
                return Response(interests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            people_also_viewed_data = request.data.get('peoplealsoviewed_set',[])
            people_also_viewed_serializer = PeopleAlsoViewedSerializer(data=people_also_viewed_data, many=True)
            if people_also_viewed_serializer.is_valid():
                people_also_viewed_serializer.save(user=user_instance)
            else:
                return Response(people_also_viewed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            people_you_may_know_data = request.data.get('peopleyoumayknow_set', [])
            people_you_may_know_serializer = PeopleYouMayKnowSerializer(data=people_you_may_know_data, many=True)
            if people_you_may_know_serializer.is_valid():
                people_you_may_know_serializer.save(user=user_instance)
            else:
                return Response(people_you_may_know_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API FOR GETTING THE USER
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()  # Fetch all user objects from the database
    serializer = UserSerializer(users, many=True)  # Serialize the queryset of users
    return Response(serializer.data)  # Return the serialized data as a JSON response
    


  



    











