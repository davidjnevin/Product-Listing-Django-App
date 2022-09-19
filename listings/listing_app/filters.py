import django_filters

from .models import ListingsApp


class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = ListingsApp
        fields = ["condition", "city", "state"]
