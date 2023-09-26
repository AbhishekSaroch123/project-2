from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import *
from model_bakery import baker
from .models import User
from .serializers import *
from rest_framework.test import APIClient



class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url_create_user = reverse('project2:create_user_api')  # Update with the correct pattern name
        self.url_get_users = reverse('project2:get_users_api')  # Update with the correct pattern name

    def test_create_user(self):
        data = {
            "name": "Naman",
            "role": "Tester",
            "location": "Summerhill",
            "connections": 10,
            "profile_language": "English",
            "public_profile_url": "https://example.com/namansharma"
        }

        response = self.client.post(self.url_create_user, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        # Assuming you have already created a User object in the database
        user = User.objects.create(
            name="Naman",
            role="Tester",
            location="Summerhill",
            connections=10,
            profile_language="English",
            public_profile_url="https://example.com/namansharma"
        )

        response = self.client.get(self.url_get_users)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming you only have one user

        retrieved_user = response.data[0]
        self.assertEqual(retrieved_user['name'], user.name)
        self.assertEqual(retrieved_user['role'], user.role)
        # Add more assertions for other fields as needed


       
     
      





 
