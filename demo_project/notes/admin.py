from django.contrib import admin
from dal_admin_filters import AutocompleteFilter
from dal import forward

from notes.models import Country, Person, Asset


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


class CountryFilter(AutocompleteFilter):
    title = 'Country from'
    field_name = 'from_country'
    autocomplete_url = 'country-autocomplete'


class CountryPlaceholderFilter(AutocompleteFilter):
    title = 'Country from'
    field_name = 'from_country'
    autocomplete_url = 'country-autocomplete'
    is_placeholder_title = True


class CountryCustomPlaceholderFilter(AutocompleteFilter):
    title = 'Country from'
    parameter_name = 'from_country'
    autocomplete_url = 'country-autocomplete'
    widget_attrs = {
        'data-placeholder': 'Filter by country name'
    }


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    class Media:
        pass

    list_filter = [CountryFilter]


class PersonFilter(AutocompleteFilter):
    autocomplete_url = 'person-autocomplete'
    title = 'Owner'
    field_name = 'owner'
    forwards = [
        forward.Field(
            'from_country__id__exact',  # Field name of filter input
            'country_id'  # Field name passed to the autocomplete_url endpoint
                          # Read more at https://django-autocomplete-light.readthedocs.io/en/master/tutorial.html#filtering-results-based-on-the-value-of-other-fields-in-the-form
        )
    ]


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    class Media:
        pass

    list_filter = [CountryFilter, PersonFilter]
