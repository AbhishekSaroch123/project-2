from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import User
from ..serializers import UserSerializer

class UserAPITest(TestCase):
    def setUp(self):
        # Create a test user instance
        self.user_data = {
            "name": "Test User",
            "role": "Tester",
            "location": "Test City",
            "connections": 5,
            "profile_language": "English",
            "public_profile_url": "http://example.com/testuser",
        }
        self.user = User.objects.create(**self.user_data)
        self.api_client = APIClient()

    def test_create_user_api(self):
        # Define the data for creating a new user
        new_user_data = {
            "name": "New User",
            "role": "New Tester",
            "location": "New City",
            "connections": 10,
            "profile_language": "Spanish",
            "public_profile_url": "http://example.com/newuser",
        }

        # Send a POST request to create a new user
        response = self.api_client.post("/api/create_user/", new_user_data, format="json")

        # Check if user creation is successful (status code 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the user has been created in the database
        self.assertEqual(User.objects.count(), 2)

    def test_get_users_api(self):
        # Send a GET request to retrieve the list of users
        response = self.api_client.get("/api/users/")

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserialize the response data
        serialized_users = UserSerializer(User.objects.all(), many=True)

        # Compare the serialized data with the data in the response
        self.assertEqual(response.data, serialized_users.data)

    def tearDown(self):
        # Clean up after the test
        User.objects.all().delete()
