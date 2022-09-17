from django.contrib.auth import logout
from django.shortcuts import redirect, render


def log_out(request):
    logout(request)
    return redirect("listing_app:index")
