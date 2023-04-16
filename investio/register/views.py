from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegisterForm


# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()

    context = {
        "form": form
    }
    return render(request=request, template_name="register.html", context=context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request=request, template_name="login.html", context=context)

def logout_user(request):
    logout(request)
    return redirect("main:home")

def user_profile(request):
    context = {
        'user': request.user,
    }
    return render(request=request, template_name="login.html", context=context)