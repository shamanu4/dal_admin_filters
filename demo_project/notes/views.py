from dal import autocomplete

from notes.models import Country, Person


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Country.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class PersonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        country_id = self.forwarded.get('country_id', None)
        if country_id:
            qs = qs.filter(from_country_id=country_id)

        return qs
