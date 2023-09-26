# serializers.py
from rest_framework import serializers
from .models import User, Education, Skills, PeopleYouMayKnow, PeopleAlsoViewed, Interests, Analytics

class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = ['name','description','followers']

class PeopleAlsoViewedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleAlsoViewed
        fields = ['name','college','connections']

class PeopleYouMayKnowSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleYouMayKnow
        fields = ['name','description','mutual_connections']

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['skill_name']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['educational_institute_name','educational_institute_type','type','time_period','grade']

class UserSerializer(serializers.ModelSerializer):
    interests_set = InterestsSerializer(many=True,read_only=True)
    peoplealsoviewed_set = PeopleAlsoViewedSerializer(many=True,read_only=True)
    peopleyoumayknow_set = PeopleYouMayKnowSerializer(many=True,read_only=True)
    skills_set = SkillsSerializer(many=True,read_only=True)
    education_set = EducationSerializer(many=True,read_only=True)

    class Meta:
        model = User
        fields = ['name','role','location','connections','profile_language','public_profile_url','interests_set','peoplealsoviewed_set','peopleyoumayknow_set','skills_set','education_set']

    


