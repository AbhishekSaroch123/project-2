from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Education)
admin.site.register(PeopleAlsoViewed)
admin.site.register(PeopleYouMayKnow)
admin.site.register(Skills)
admin.site.register(Interests)
admin.site.register(Analytics)
admin.site.register(Resources)
