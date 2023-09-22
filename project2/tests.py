from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import User
from model_bakery import baker
from .models import User
from .serializers import UserSerializer

# class UserTestCase(TestCase):
#     def setUp(self):
#         # Create some sample user data for testing
#         User.objects.create(name="Test User 1", role="Developer", location="City 1", connections=100, profile_language="English", public_profile_url="https://example.com/testuser1")
#         User.objects.create(name="Test User 2", role="Designer", location="City 2", connections=50, profile_language="Spanish", public_profile_url="https://example.com/testuser2")

#     def test_user_creation(self):
#         # Test user creation via API
#         url = reverse('project2:create_user_api')
#         data = {
#             "name": "New User",
#             "role": "Tester",
#             "location": "City 3",
#             "connections": 10,
#             "profile_language": "French",
#             "public_profile_url": "https://example.com/newuser"
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class UserTestCase1(TestCase):
#     def test_user_model_creation(self):
#         # Create a user instance using Model Bakery
#         user = baker.make(
#             User,
#             name="Abhishek Sharma",
#             role="Developer",
#             location="Shimla",
#             connections=50,
#             profile_language="English",
#             public_profile_url="https://example.com/abhisheksharma"
#         )

#         # Perform assertions to test the user instance
#         self.assertEqual(user.name, "Abhishek Sharma")
#         self.assertEqual(user.role, "Developer")
#         self.assertEqual(user.location, "Shimla")
#         self.assertEqual(user.connections, 50)
#         self.assertEqual(user.profile_language, "English")
#         self.assertEqual(user.public_profile_url, "https://example.com/abhisheksharma")

#     def test_user_serializer(self):
#         # Create a user instance using Model Bakery
#         user = baker.make(
#             User,
#             name="Abhishek Rana",
#             role="Data Scientist",
#             location="Kangra",
#             connections=75,
#             profile_language="English",
#             public_profile_url="https://example.com/abhishekrana"
#         )

#         # Serialize the user instance using the UserSerializer with data
#         serializer = UserSerializer(data=User.objects.filter(id=user.id).values().first())

#         # Validate the serialized data
#         self.assertTrue(serializer.is_valid())
#         self.assertEqual(serializer.data['name'], "Abhishek Rana")
#         self.assertEqual(serializer.data['role'], "Data Scientist")
#         self.assertEqual(serializer.data['location'], "Kangra")
#         self.assertEqual(serializer.data['connections'], 75)
#         self.assertEqual(serializer.data['profile_language'], "English")
#         self.assertEqual(serializer.data['public_profile_url'], "https://example.com/abhishekrana")



from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker
from .models import User  # Import your User model
from .serializers import UserSerializer  # Import your UserSerializer

class UserAPITestCase(APITestCase):
    def test_get_users_api(self):
        user = baker.make(
            User,
            name="Kartik",
            role="Tester",
            location="Summerhill",
            connections=10,
            profile_language="English",
            public_profile_url="https://example.com/Kartik"
        )
        url = reverse('project2:get_users_api')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = UserSerializer(user).data
        self.assertEqual(response.data[0], expected_data)





 
