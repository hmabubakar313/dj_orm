from django.contrib import admin
from .models import Profile, User, Group, User_groups, Comment, BlogPost

Mymodels = [Profile, User, Group, User_groups, Comment, BlogPost]
admin.site.register(Mymodels)
