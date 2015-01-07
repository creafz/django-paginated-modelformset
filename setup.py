#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__),
                       'paginated_modelformset', '__init__.py')) as init_file:
    init = init_file.read()
    author = re.search("__author__ = '([^']+)'", init).group(1)
    author_email = re.search("__email__ = '([^']+)'", init).group(1)
    version = re.search("__version__ = '([^']+)'", init).group(1)

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-paginated-modelformset',
    version=version,
    packages=['paginated_modelformset'],
    include_package_data=True,
    license='MIT License',
    description='An attempt to add pagination to Django Model Formsets.',
    long_description=README,
    keywords='django,form,formset,modelformset,pagination',
    url='https://github.com/creafz/django-paginated-modelformset',
    download_url=
    'https://github.com/creafz/django-paginated-modelformset/tarball/{0}'
    .format(version),
    author='Alex Parinov',
    author_email='creafz@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=["django>=1.6"],
)