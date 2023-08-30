from django.db import models

class Profile(models.Model):
    bio = models.TextField()

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Group(models.Model):
    name = models.CharField(max_length=255)

class User_groups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    comments = models.ManyToManyField(Comment)


