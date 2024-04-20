from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import BestRun

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
class BestRunForm(forms.ModelForm):
    class Meta:
        model = BestRun
        fields = ['date', 'video_url', 'description']  # 'date'を一旦ここに含めます

    def __init__(self, *args, **kwargs):
        super(BestRunForm, self).__init__(*args, **kwargs)
        self.fields.pop('date')  # 'date'フィールドをフォームから除外