import os

from distutils.core import setup
from jeeves import VERSION

setup(
    name = "jeeves-framework",
    version = VERSION,
    license="BSD",
    url = 'http://procrastinatingdev.com/jeeves/',
    author = 'Adam McKerlie',
    author_email = 'adammckerlie@gmail.com',
    description = 'A Python IRC Bot Framework. Easily create IRC bots with a single command',
    long_description = open('README.rst').read(),
    download_url = '',
    scripts = ['jeeves/bin/jeeves-admin.py'],

    install_requires = [
        "twisted",
    ],
    packages=[
        'jeeves',
        'jeeves/bin',
        'jeeves/core',
        'jeeves/conf',
        'jeeves/plugins',
        'jeeves/tests',
        'jeeves/utils',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
   ],
)
