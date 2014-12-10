# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.paginator import Page, Paginator


class FormSetPage(Page):
    """``Page`` subclass that has additional attributes from queryset that are
    required by ``BaseModelFormset`` functions.
    """
    def __init__(self, *args, **kwargs):
        super(FormSetPage, self).__init__(*args, **kwargs)
        self.db = None

    def mimic_queryset(self, queryset):
        """Add attributes from the queryset that are required by
        ``BaseModelFormset``."""

        # ``db`` attribute is required only if you use Django < 1.7. After
        # changes in the commit ``efb0100ee6`` this attribute is not required,
        # but to make things simple, we always add it.
        self.db = queryset.db


class FormSetPaginator(Paginator):
    """Paginator that returns a ``FormSetPage`` object instead of a
    standard ``Page``.
    """
    def _get_page(self, *args, **kwargs):
        return FormSetPage(*args, **kwargs)

