from distutils.core import setup

# Dynamically calculate the version based on jeeves.VERSION.
version = __import__('jeeves').get_version()

setup(
    name = "jeeves-framework",
    version = version,
    license="BSD",
    url = 'http://procrastinatingdev.com/jeeves/',
    author = 'Adam McKerlie',
    author_email = 'adammckerlie@gmail.com',
    description = 'A Python IRC Bot Framework. Easily create IRC bots with a single command',
    long_description = open('README.rst').read(),
    download_url = '',
    scripts = ['jeeves/bin/jeeves-admin.py'],

    install_requires = [
        "rapidsms",
        "django-uni-form"
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
