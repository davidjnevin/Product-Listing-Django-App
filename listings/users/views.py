from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import UserForm


def log_out(request):
    logout(request)
    return redirect("listing_app:index")


def register(request):
    if request.method != "POST":
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")

    context = {"form": form}
    return render(request, "registration/register.html", context)
