from django.shortcuts import redirect, render

from .forms import ListingForm
from .models import ListingsApp


def index(request):
    return render(request, "listing_app/index.html")


def all_listings(request):

    all_listings = ListingsApp.objects.order_by("-list_date")

    context = {"all_listings": all_listings}

    return render(request, "listing_app/all_listings.html", context)


def new_listing(request):
    if request.method != "POST":
        form = ListingForm()
    else:
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listing_app:all_listings")

    context = {"form": form}
    return render(request, "listing_app/new_listing.html", context)


def detail(request, detail_id):
    detail = ListingsApp.objects.get(id=detail_id)
    context = {"detail": detail}
    return render(request, "listing_app/detail.html", context)


def my_listings(request):
    my_listings = ListingsApp.objects.order_by("-list_date")
    context = {"my_listings": my_listings}
    return render(request, "listing_app/my_listings.html", context)
