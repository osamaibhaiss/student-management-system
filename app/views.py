from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import Course
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard.html')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard.html')  # Replace 'adminpage' with your actual admin page URL name
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def course_search(request):
    query = request.GET.get('query')
    if query:
        courses = Course.objects.filter(code__icontains=query) | Course.objects.filter(name__icontains=query) | Course.objects.filter(instructor__name__icontains=query)
    else:
        courses = []
    return render(request, 'course_search.html', {'courses': courses})


def dashBoard(request):
    return render(request, 'dashboard.html')
def osama_view(request):
    return render(request, 'base.html')