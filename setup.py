import os

from setuptools import setup


# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as file_:
        return file_.read()


setup(
    name='dal_admin_filters',
    description='Django autocomplete light filters for django admin',
    author='Maxim Musayev <shamanu4@gmail.com>, Olivier Dormond <olivier.dormond@pix4d.com>',
    url='https://github.com/Pix4D/dal_admin_filters',
    packages=['dal_admin_filters'],
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.rst'),
    license='MIT',
    keywords='django autocomplete admin filters',
    install_requires=[
        'django-autocomplete-light'
    ],
    setup_requires=[
        'setuptools_scm',
        'wheel',
    ],
    use_scm_version=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
