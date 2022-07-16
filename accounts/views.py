from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    logout as logout_user,
    login as login_user)
from .models import User


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user=user)
            return redirect('/')
        else:
            messages.success(request, 'Wrong username or password')
            return redirect('/accounts/login')
    return render(request, 'accounts/login.html')


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/signup.html', {'form': form})

# Logout


@login_required
def logout(request):
    if request.method == 'GET':
        logout_user(request)
    return redirect('/accounts/login')

# Profile Display


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'accounts/profile.html', {'user': user})

# Profile Update


@login_required
def profile_update(request):
    form = EditProfileForm(instance=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', kwargs={'username': form.cleaned_data['username']}))

    return render(request, 'accounts/profile-update.html', {'form': form})

# Profile Picture Update


@login_required
def update_profile_picture(request):
    if request.method == 'POST':
        user = request.user
        picture = request.FILES.get('profile_picture')
        clear_picture = request.POST.get('clear-pp')

        if picture:
            user.profile_picture.delete(save=True)
            user.profile_picture = request.FILES['profile_picture']
            user.save()
        elif clear_picture == 'on':
            user.profile_picture.delete(save=True)

        return redirect('/accounts/edit')
