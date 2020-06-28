from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import *
from movies.models import Emotion
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ProfileUpdateForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:first_page')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form = form.save()
            auth_login(request, form, backend="django.contrib.auth.backends.ModelBackend",)
            return redirect('movies:first_page')
    else:
        form = CustomUserCreationForm()
    context ={
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:first_page')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:first_page')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    user = request.user
    emotions = Emotion.objects.all()
    for emotion in emotions:
        a = emotion.emotion.all()
        if user in a:
            emotion.emotion.remove(user)
    auth_logout(request)
    return redirect('movies:movie_list')


@login_required
def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def profile_update(request, username):   # 마이페이지 작성 페이지 앤 수정
    profile = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)

        if form.is_valid():
            updateform = form.save(commit=False)
            updateform.user = request.user
            updateform.profile = profile
            updateform.save()
            return redirect('accounts:profile', username)
    else:
        form = ProfileUpdateForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'accounts/profile_update.html', context)


@login_required
def follow(request, username):
    me = request.user
    user = get_object_or_404(get_user_model(), username=username)
    if user != request.user:
        if user.followers.filter(pk=me.pk).exists():
            user.followers.remove(me)
        else:
            user.followers.add(me)
    return redirect('accounts:profile', username)