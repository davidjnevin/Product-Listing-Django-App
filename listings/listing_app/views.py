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
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("listing_app:all_listings")

    context = {"form": form}
    return render(request, "listing_app/new_listing.html", context)


def detail(request, detail_id):
    detail = ListingsApp.objects.get(id=detail_id)
    context = {"detail": detail}
    return render(request, "listing_app/detail.html", context)


def my_listings(request):
    my_listings = request.user.listingsApp_set.order_by("-list_date")
    context = {"my_listings": my_listings}
    return render(request, "listing_app/my_listings.html", context)


def edit_listing(request, edit_id):
    listing = ListingsApp.objects.get(id=edit_id)

    if request.method != "POST":
        form = ListingForm(instance=listing)
    else:
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid:
            form.save()
            return redirect("listing_app:all_listings")

    context = {"listing": listing, "form": form}
    return render(request, "listing_app/edit_listing.html", context)


def delete_listing(request, delete_id):
    listing = ListingsApp.objects.get(id=delete_id)
    if request.method == "POST":
        listing.delete()
        return redirect("listing_app:my_listings")
    context = {"listing": listing}
    return render(request, "listing_app/delete_listing.html", context)
