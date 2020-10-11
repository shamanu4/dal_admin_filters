# -*- encoding: utf-8 -*-
from dal import autocomplete, forward
from django import forms
from django.contrib.admin.filters import SimpleListFilter
from django.forms.widgets import Media, MEDIA_TYPES, media_property


class AutocompleteFilter(SimpleListFilter):
    template = "dal_admin_filters/autocomplete-filter.html"
    title = ''
    field_name = ''
    field_pk = 'id'
    use_pk_exact = True
    autocomplete_url = ''
    is_placeholder_title = False
    widget_attrs = {}
    forwards = []

    class Media:
        css = {
            'all': (
                'dal_admin_filters/css/select2.min.css',
                'autocomplete_light/select2.css',
                'dal_admin_filters/css/autocomplete-fix.css'
            )
        }
        js = (
            'admin/js/jquery.init.js',
            'autocomplete_light/jquery.init.js',
            'dal_admin_filters/js/forward-fix.js',
            'dal_admin_filters/js/select2.full.min.js',
            'autocomplete_light/autocomplete.init.js',
            'autocomplete_light/forward.js',
            'autocomplete_light/select2.js',
            'dal_admin_filters/js/querystring.js',
        )

    def __init__(self, request, params, model, model_admin):
        if self.parameter_name is None:
            self.parameter_name = self.field_name
            if self.use_pk_exact:
                self.parameter_name += '__{}__exact'.format(self.field_pk)
        super(AutocompleteFilter, self).__init__(request, params, model, model_admin)

        widget = self.get_widget(request)

        self._add_media(model_admin, widget)

        field = forms.ModelChoiceField(
            queryset=self.get_queryset_for_field(model, self.field_name),
            widget=widget
        )

        attrs = self.widget_attrs.copy()
        attrs['id'] = 'id-%s-dal-filter' % self.field_name
        if self.is_placeholder_title:
            attrs['data-placeholder'] = self.title
        self.rendered_widget = field.widget.render(
            name=self.parameter_name,
            value=self.used_parameters.get(self.parameter_name, ''),
            attrs=attrs
        )

    def get_queryset_for_field(self, model, name):
        return getattr(model, name).get_queryset()

    def _add_media(self, model_admin, widget):

        if not hasattr(model_admin, 'Media'):
            model_admin.__class__.Media = type('Media', (object,), dict())
            model_admin.__class__.media = media_property(model_admin.__class__)

        def _get_media(obj):
            return Media(media=getattr(obj, 'Media', None))

        media = _get_media(model_admin) + widget.media + _get_media(AutocompleteFilter) + _get_media(self)

        for name in MEDIA_TYPES:
            setattr(model_admin.Media, name, getattr(media, "_" + name))

    def get_forwards(self):
        return tuple(
            forward.Field(field, field) if isinstance(field, str) else field
            for field in self.forwards
        ) or None

    def get_widget(self, request):
        widget = autocomplete.ModelSelect2(
            url=self.get_autocomplete_url(request),
            forward=self.get_forwards(),
        )
        return widget

    def get_autocomplete_url(self, request):
        return self.autocomplete_url

    def has_output(self):
        return True

    def lookups(self, request, model_admin):
        return ()

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(**{self.parameter_name: self.value()})
        else:
            return queryset
