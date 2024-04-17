from django.db import models
from django.contrib.auth.models import User

class BestRun(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    video_url = models.URLField()
    description = models.TextField()

"""
class Calendar(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)  # 日付の名前を保存するフィールド

    def __str__(self):
        return f"{self.name} ({self.date})"

class FriendComments(models.Model):
    best_run = models.ForeignKey(BestRun, on_delete=models.CASCADE)
    text = models.TextField()

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    friend_user = models.ForeignKey(User, related_name='friend_user', on_delete=models.CASCADE)
"""