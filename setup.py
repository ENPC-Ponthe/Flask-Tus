"""
Flask-Tus
-------------

Implements the tus.io server-side file-upload protocol
visit http://tus.io for more information

"""
from setuptools import setup


setup(
    name='Flask-Tus-Ponthe',
    version='1.0.0',
    url='https://github.com/PhilippeFerreiraDeSousa/Flask-Tus',
    license='MIT',
    author='Philippe Ferreira De Sousa',
    author_email='philippe@fdesousa.fr',
    description='TUS protocol implementation fork for ENPC club Ponthe',
    long_description=__doc__,
    py_modules=['flask_tus_ponthe'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
		'Redis'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
