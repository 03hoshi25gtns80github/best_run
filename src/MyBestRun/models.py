from django.db import models
from accounts.models import CustomUser

class BestRun(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    video = models.FileField(upload_to='videos/')  # ファイルアップロード用のフィールド
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