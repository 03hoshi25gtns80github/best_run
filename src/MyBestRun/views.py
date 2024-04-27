from django.shortcuts import render, redirect
from .forms import BestRunForm, InquiryForm
from django.views.generic.detail import DetailView
from .models import BestRun
import datetime
from django.views import generic
from . import mixins

def front(request):
    return render(request, 'front.html')

class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm

class FormCalendar(mixins.MonthCalendarMixin, generic.CreateView):
    """フォームに飛べる月間カレンダー"""
    template_name = 'formcalendar.html'
    model = BestRun
    date_field = 'date'
    form_class = BestRunForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        month_calendar_context = self.get_month_calendar()
        context.update(month_calendar_context)
        return context

    def form_valid(self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
          
        # 指定された日付で既存のデータを検索
        existing_runs = BestRun.objects.filter(date=date, user=self.request.user)
        # 既存のデータがあれば削除
        existing_runs.delete()
        
        best_run = form.save(commit=False)  # 小文字で始める変数名に修正
        best_run.date = date  # カレンダーで選択した日付を設定
        best_run.user = self.request.user  # ログインユーザーをBestRunインスタンスに関連付け
        best_run.video_url = best_run.video.url  # Azure StorageにアップロードされたファイルのURLを保存
        url_parts = best_run.video_url.split('/')
        url_parts.insert(-1, 'videos')
        best_run.video_url = '/'.join(url_parts)
        best_run.save()
        return redirect('MyBestRun:formcalendar')
    
    
class MyCalendar(mixins.MonthWithBestrunMixin, generic.ListView):
    template_name = 'mycalendar.html'
    model = BestRun
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context

class BestRunDetailView(DetailView):
    model = BestRun
    template_name = 'bestrun_detail.html'
    context_object_name = 'bestrun'
    