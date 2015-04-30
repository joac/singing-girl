#! -*- coding: utf8 -*-
from distutils.core import setup

setup(
    name='singing-girl',
    version='0.0.3',
    description=u'Library to convert number literals, to spanish equivalent text strings',
    long_description=open('README.rst').read(),
    author=u'Joaquín Sorianello',
    url='https://github.com/joac/singing-girl',
    packages=['singing_girl'],
    license='LICENSE.md',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Localization',
        'Topic :: Utilities'
    ],
)
