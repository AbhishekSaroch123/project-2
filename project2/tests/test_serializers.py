from django.test import TestCase
from ..models import User
from ..serializers import UserSerializer

class UserSerializerTest(TestCase):
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

    def test_user_serializer(self):
        # Serialize the test user instance
        serializer = UserSerializer(instance=self.user)

        # Define the expected serialized data
        expected_data = {
            "name": "Test User",
            "role": "Tester",
            "location": "Test City",
            "connections": 5,
            "profile_language": "English",
            "public_profile_url": "http://example.com/testuser",
        }

        # Compare the serialized data with the expected data
        self.assertEqual(serializer.data, expected_data)

    def tearDown(self):
        # Clean up after the test
        User.objects.all().delete()
