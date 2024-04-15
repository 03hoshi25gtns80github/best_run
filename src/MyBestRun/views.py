from django.shortcuts import render, redirect
from .forms import SignUpForm, BestRunForm
from django.contrib.auth import authenticate, login

def front(request):
    return render(request, 'front.html')

def signupview(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('front')  # ログイン後はフロントページにリダイレクト
        else:
            # 認証失敗時の処理
            return render(request, 'login.html', {'error': 'ユーザー名またはパスワードが間違っています。'})
    else:
        return render(request, 'login.html')
    
def best_run_form(request):
    if request.method == 'POST':
        form = BestRunForm(request.POST)
        if form.is_valid():
            best_run = form.save(commit=False)
            best_run.user = request.user
            best_run.save()
            return redirect('calendar')  # カレンダーページにリダイレクト
    else:
        form = BestRunForm()
    return render(request, 'best_run_form.html', {'form': form})
    

