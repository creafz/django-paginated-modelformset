# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from datetime import datetime
import unittest

from django.forms.models import modelformset_factory
from django.test import TestCase

from paginated_modelformset import FormSetPaginator, FormSetPage, \
    PaginatedModelFormSet

from .models import Article


class FormSetPageTests(unittest.TestCase):
    def test_formset_paginator_class(self):
        paginator = FormSetPaginator([1, 2, 3], 1)
        page = paginator.page(1)
        self.assertEqual(page.__class__, FormSetPage)


class FormSetPagePaginatorTests(TestCase):
    def setUp(self):
        for x in range(1, 10):
            article = Article(headline='Article %s' % x,
                              pub_date=datetime(2005, 7, 29))
            article.save()

    def test_formsetpage_init(self):
        paginator = FormSetPaginator([1, 2, 3], 1)
        page = paginator.page(1)
        self.assertEqual(page.db, None)

    def test_mimic_queryset(self):
        paginator = FormSetPaginator(Article.objects.all(), 1)
        page = paginator.page(1)
        articles = Article.objects.all()
        page.mimic_queryset(articles)
        self.assertEqual(page.db, "default")


class PaginatedModelFormSetTests(TestCase):

    def _create_formset(self):
        return self.article_form_set(queryset=self.qs, per_page=5, page_num=1)

    def setUp(self):
        for x in range(1, 10):
            article = Article(headline='Article %s' % x,
                              pub_date=datetime(2005, 7, 29))
            article.save()

        self.qs = Article.objects.all()
        self.article_form_set = modelformset_factory(
            Article, formset=PaginatedModelFormSet, fields="__all__", extra=0)

    def test_modelformset_creation(self):
        formset = self._create_formset()
        self.assertEqual(formset.per_page, 5)
        self.assertEqual(formset.page_num, 1)
        self.assertEqual(formset.page, None)
        self.assertEqual(len(formset.forms), 5)

    def test_modelformset_page_attributes(self):
        formset = self.article_form_set(queryset=self.qs, per_page=5,
                                        page_num=1)
        self.assertEqual(formset.get_queryset().db, "default")

    def test_modelformset_page_class(self):
        formset = self._create_formset()
        len(formset.forms)  # Force QuerySet evaluation
        self.assertEqual(formset.page.__class__, FormSetPage)

    def test_modelformset_page_not_an_integer_exception(self):
        formset = self.article_form_set(queryset=self.qs, per_page=5,
                                        page_num="NOT_NUM")
        len(formset.forms)  # Force QuerySet evaluation
        self.assertEqual(formset.page.number, 1)

    def test_modelformset_empty_page_exception(self):
        formset = self.article_form_set(queryset=self.qs, per_page=5,
                                        page_num=100000)
        len(formset.forms)  # Force QuerySet evaluation
        self.assertEqual(formset.page.number, 2)