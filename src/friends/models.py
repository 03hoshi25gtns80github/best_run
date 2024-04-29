from django.db import models
from accounts.models import CustomUser
from MyBestRun.models import BestRun

class Friend(models.Model):
    user = models.ForeignKey(CustomUser, related_name='friends', on_delete=models.CASCADE)
    friend_user = models.ForeignKey(CustomUser, related_name='friend_users', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.friend_user.username}"

class FriendComment(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    best_run = models.ForeignKey(BestRun, on_delete=models.CASCADE)
    date = models.DateField()
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.friend.user.username} on {self.best_run.date} - {self.text}"