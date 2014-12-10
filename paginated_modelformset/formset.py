# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.paginator import PageNotAnInteger, EmptyPage
from django.forms.models import BaseModelFormSet

from paginated_modelformset.paginator import FormSetPaginator


class PaginatedModelFormSet(BaseModelFormSet):
    """ModelFormSet class with pagination support."""
    def __init__(self, per_page=10, page_num=1, *args, **kwargs):
        super(PaginatedModelFormSet, self).__init__(*args, **kwargs)
        self.per_page = per_page
        self.page_num = page_num
        self.page = None

    def get_queryset(self):
        if not hasattr(self, '_queryset'):
            # Pass a queryset to the ``BaseModelFormSet`` for
            # the initial processing.
            qs = super(PaginatedModelFormSet, self).get_queryset()

            # Use the standard pagination pattern described at
            # https://docs.djangoproject.com/en/dev/topics/pagination/
            paginator = FormSetPaginator(qs, self.per_page)
            try:
                items = paginator.page(self.page_num)
            except PageNotAnInteger:
                items = paginator.page(1)
            except EmptyPage:
                items = paginator.page(paginator.num_pages)

            # Copy all required queryset attributes to the ``FormSetPage``
            # object.
            items.mimic_queryset(qs)

            # Use a ``FormSetPage`` object instead of queryset for all
            # methods. This looks ugly and hacky, but it seems that it is
            # the most simple way to make it work without rewriting the whole
            # ``BaseModelFormSet`` class.
            self._queryset = items

            # Explicitly add a ``FormSetPage`` object as a ``page`` attribute
            # so it can be used in templates to displaying the pagination
            # information.
            self.page = items
        return self._queryset