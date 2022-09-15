from django import forms

from .models import ListingsApp


class ListingForm(forms.ModelForm):
    class Meta:
        model = ListingsApp
        fields = [
            "title",
            "condition",
            "product_type",
            "sale_type",
            "price",
            "main_photo",
            "photo_1",
            "photo_2",
            "city",
            "state",
            "zipcode",
            "contact_email",
            "list_date",
        ]
