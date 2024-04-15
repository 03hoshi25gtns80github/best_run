from django.db import models
from django.contrib.auth.models import User

class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

class BestRun(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    video_url = models.URLField()
    description = models.TextField()

class FriendComments(models.Model):
    best_run = models.ForeignKey(BestRun, on_delete=models.CASCADE)
    text = models.TextField()

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    friend_user = models.ForeignKey(User, related_name='friend_user', on_delete=models.CASCADE)