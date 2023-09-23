from rest_framework import serializers
from .models import *



class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    education_set = EducationSerializer(many=True)  # Serialize related Education instances
    skills_set = SkillsSerializer(many=True)  # Serialize related Skills instances
    class Meta:
        model = User
        fields = '__all__'
