import os

from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='dal_admin_filters',
    version='1.1.0',
    description='Django autocomplete light filters for django admin',
    author='Maxim Musayev',
    author_email='shamanu4@gmail.com',
    url='https://github.com/shamanu4/dal_admin_filters',
    packages=['dal_admin_filters'],
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='django autocomplete admin filters',
    install_requires=[
        'django-autocomplete-light'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
