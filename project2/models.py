from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    connections=models.PositiveBigIntegerField()
    profile_language=models.CharField(max_length=255)
    public_profile_url=models.URLField()

    def __str__(self):
        return self.name
    

class Analytics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_views = models.PositiveIntegerField()
    post_impressions = models.PositiveIntegerField()
    search_appearance = models.PositiveIntegerField()

class Resources(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(primary_key=True, max_length=255)
    status = models.CharField(max_length=255)
    text = models.TextField()

class Education(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    educational_institute_name=models.CharField(max_length=255)
    educational_institute_type=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    time_period=models.CharField(max_length=255)
    grade = models.CharField(max_length=255, blank=True)

class Skills(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    skill_name = models.CharField(primary_key=True, max_length=255)

class Interests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(primary_key=True, max_length=255)
    description = models.TextField()
    followers = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PeopleAlsoViewed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(primary_key=True, max_length=255)
    college = models.CharField(max_length=255)
    connections = models.PositiveIntegerField()

class PeopleYouMayKnow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(primary_key=True, max_length=255)
    description = models.CharField(max_length=255)
    mutual_connections = models.PositiveIntegerField()