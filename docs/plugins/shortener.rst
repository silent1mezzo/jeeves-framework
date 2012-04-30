.. _shortener_plugin:

:title: Shortener Plugin

Shortener Plugin
================

The shortener plugin allows you to shorten any link that you want.

Usage
+++++

To shorten a link you use the `shorten` or `-s` command and provide the link that you wish to shorten. Jeeves will the privately message you the shortened link.

::

    > <bot name> shorten example.org
    > <bot name> -s example.org

Settings
++++++++

SHORTENER_BACKEND
~~~~~~~~~~~~~~~~~

Default: 'google'

The shortener backend to use. The built-in backends are:

* ``'google'``
* ``'isgd'``
* ``'bitly'``

SHORTENER_LOGIN
~~~~~~~~~~~~~~~

Default: None

The username needed to authenticate with a shortening service. Required for 'bitly' backend.

SHORTENER_API_KEY
~~~~~~~~~~~~~~~~~

Default: None

The key or password needed to authenticate with a shortening service. Required for 'bitly' backend.
