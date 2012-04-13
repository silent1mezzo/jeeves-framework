import os
import sys
import jeeves

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system("git tag -a v%s -m 'version %s'" % (jeeves.__version__, jeeves.__version__))
    os.system('python setup.py sdist upload')
    os.system('git push --tags')
    sys.exit()

if sys.argv[-1] == 'test':
    os.system('python tests/test_jeeves.py')
    sys.exit()

required = ['twisted', 'requests', ]
packages = [
    'tests',
    'jeeves',
    'jeeves.bin',
    'jeeves.conf',
    'jeeves.conf.project_template',
    'jeeves.conf.project_template.plugins',
    'jeeves.core',
    'jeeves.core.handlers',
    'jeeves.core.management',
    'jeeves.core.plugins',
    'jeeves.utils',
]

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
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
   ],
)
