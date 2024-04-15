from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponse

def front(request):
    return render(request, 'front.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # ログインページへリダイレクト
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})