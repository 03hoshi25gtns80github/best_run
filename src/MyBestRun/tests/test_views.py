from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import BestRun
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.date = datetime.date.today()
        self.best_run = BestRun.objects.create(
            date=self.date,
            user=self.user,
            video_url='http://example.com/video.mp4'
        )


class TestMyCalendarView(CustomTestCase):
    def test_my_calendar_view(self):
        response = self.client.get(reverse('MyBestRun:mycalendar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mycalendar.html')

class TestBestRunDetailView(CustomTestCase):
    def test_best_run_detail_view(self):
        url = reverse('MyBestRun:bestrun_detail', kwargs={'pk': self.best_run.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bestrun_detail.html')
        self.assertEqual(response.context['bestrun'], self.best_run)