from django.contrib import admin
from notes.models import Country, Person
from dal_admin_filters import AutocompleteFilter


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


class CountryFilter(AutocompleteFilter):
    title = 'Country from'
    parameter_name = 'from_country'
    autocomplete_url = 'country-autocomplete'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    class Media:
        pass

    list_filter = [CountryFilter]
