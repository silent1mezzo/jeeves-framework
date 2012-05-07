import os
import sys
import jeeves

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

required = ['twisted', 'requests', ]

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

packages = ['tests']
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
jeeves_dir = 'jeeves'

for dirpath, dirnames, filenames in os.walk(jeeves_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))

if sys.argv[-1] == 'publish':
    os.system("git tag -a v%s -m 'version %s'" % (jeeves.__version__, jeeves.__version__))
    os.system('python setup.py sdist upload')
    os.system('git push --tags')
    sys.exit()

if sys.argv[-1] == 'test':
    os.system('python tests/test_jeeves.py')
    sys.exit()

setup(
    name="jeeves-framework",
    version=jeeves.__version__,
    license=open("LICENSE.rst").read(),
    url='http://procrastinatingdev.com/jeeves/',
    author='Adam McKerlie',
    author_email='adammckerlie@gmail.com',
    description='A Python IRC Bot Framework. Easily create IRC bots with a single command',
    long_description=open('README.rst').read(),
    download_url='',
    install_requires=required,
    packages=packages,
    scripts=['jeeves/bin/jeeves-admin.py'],
    classifiers=[
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
