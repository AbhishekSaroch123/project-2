from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import *
from model_bakery import baker
from .models import User
from .serializers import *
from rest_framework.test import APITestCase
from rest_framework.response import Response



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
       
        education = baker.make(
            Education,
            user=user,
            educational_institute_name="UIT Shimla",
            educational_institute_type="ECE",
            type="Bachelor's Degree", time_period="2020-2024",
            grade="A"
            )
        skills = baker.make(
            Skills,
            user=user,
            skill_name="Python"
            )
        
        # Generate URL For My EndPoint
        url = reverse('project2:get_users_api')
        # makes a get request for my url
        response = self.client.get(url)
        # perform an assertion to check whether status is 200 is or not
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # serialized the user instance 
        expected_data_user = UserSerializer(user).data
        expected_data_education = EducationSerializer(education).data
        expected_data_skills = SkillsSerializer(skills).data

        self.assertIn('name', response.data[0])
        self.assertIn('education_set', response.data[0])  # Check for related education data
        self.assertIn('skills_set', response.data[0])
        return Response({
        'user': expected_data_user,
        'education': expected_data_education,
        'skills': expected_data_skills,
         })
       
     
      





 
