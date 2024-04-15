from django.contrib import admin
from .models import Calendar, BestRun, FriendComments, Friend

# 各モデルを管理サイトに登録します。
admin.site.register(Calendar)
admin.site.register(BestRun)
admin.site.register(FriendComments)
admin.site.register(Friend)