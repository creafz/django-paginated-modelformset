=============================
django-paginated-modelformset
=============================

.. image:: https://pypip.in/version/django-paginated-modelformset/badge.svg
    :target: https://pypi.python.org/pypi/django-paginated-modelformset/
    :alt: Latest Version

.. image:: https://travis-ci.org/creafz/django-paginated-modelformset.svg?branch=master
    :target: https://travis-ci.org/creafz/django-paginated-modelformset

.. image:: https://coveralls.io/repos/creafz/django-paginated-modelformset/badge.png?branch=master
    :target: https://coveralls.io/r/creafz/django-paginated-modelformset?branch=master

An attempt to add pagination to Django Model Formsets.

Requirements
------------
* Python 2.6+ or Python 3
* Django 1.6+


Usage
-----
::

    from django.forms.models import modelformset_factory
    from paginated_modelformset import PaginatedModelFormSet
    from myapp.models import MyModel

    MyModelFormSet = modelformset_factory(MyModel, formset=PaginatedModelFormSet)

    # In addition to standard arguments, provide a number of items per page and a page number.
    formset = MyModelFormSet(per_page=25, page_num=1)


PaginatedModelFormSet uses the same `Paginator <https://docs.djangoproject.com/en/dev/topics/pagination/>`_  class that is used for standard pagination. A `Page <https://docs.djangoproject.com/en/dev/topics/pagination/#page-objects>`_ object is accessible as a page attribute of the formset and you can use it in templates like this:

::

    <div class="pagination">
        <span class="step-links">
            {% if formset.page.has_previous %}
                <a href="?page={{ formset.page.previous_page_number }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ formset.page.number }} of {{ formset.page.paginator.num_pages }}.
            </span>

            {% if formset.page.has_next %}
                <a href="?page={{ formset.page.next_page_number }}">next</a>
            {% endif %}
        </span>
    </div>




Alternatives
------------

See this `StackOverflow question <http://stackoverflow.com/questions/14041381/paginate-django-formset>`_ for an alternative solution.