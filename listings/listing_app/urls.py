from django.urls import path

from . import views

app_name = "listing_app"

urlpatterns = [
    # Homepage
    path("", views.index, name="index"),
    # Listings page
    path("all_listings/", views.all_listings, name="all_listings"),
    # New Listings
    path("new_listing/", views.new_listing, name="new_listing"),
    # Individual Item Listing
    path("all_listings/<detail_id>", views.detail, name="detail"),
    # My_listings Page
    path("my_listings/", views.my_listings, name="my_listings"),
    # Edit Listings
    path("edit_listing/<edit_id>/", views.edit_listing, name="edit_listing"),
    # Delete Listings
    path("delete_listing/<delete_id>/", views.delete_listing, name="delete_listing"),
]
