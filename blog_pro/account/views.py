from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . forms import LoginForm, EditForm



def user_login (request):
    if request.user.is_authenticated:
        return redirect('home:home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_register(request):
    context = {'errors': []}

    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            context['errors'].append('your passwords are not same')
            return render(request, 'account/register.html', context)

        user = User.objects.create(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home:home')
    return render(request, 'account/register.html', {})


def user_logout(request):
    logout(request)
    return redirect('home:home')

def user_edit(request):
    user = request.user
    form = EditForm(instance=user)
    if request.method == "POST":
        form = EditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return  render(request, 'account/edit.html', {'form': form})