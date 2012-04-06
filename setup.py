import os

from distutils.core import setup
from jeeves import VERSION
# Dynamically calculate the version based on jeeves.VERSION.

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

jeeves_dir = 'jeeves'
packages = []
for dirpath, dirnames, filenames in os.walk(jeeves_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))

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
    packages=packages,
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
