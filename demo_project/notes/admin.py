from django.contrib import admin
from notes.models import Country, Person
from dal_admin_filters import AutocompleteFilter


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


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    class Media:
        pass

    list_filter = [CountryFilter]
