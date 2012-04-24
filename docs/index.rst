.. Jeeves Framework documentation master file, created by
   sphinx-quickstart on Fri Apr 13 14:22:22 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Jeeves Framework: IRC Bots made easy
============================================

Release v\ |version|. (:ref:`Installation <install>`)

The Jeeves Framework is a Python IRC library that makes creating and running IRC bots. A few of the core principles were borrowed from `Django <http://djangoproject.com>`_. The basic idea came when I read about Jessamyn Smith's `Talk Back Bot <https://github.com/jessamynsmith/talkbackbot>`_.  

You can easily geta bot up and running in seconds:

::

    $ pip install jeeves-framework
    $ jeeves-admin.py startbot examplebot
    $ cd examplebot
    $ python bot.py runbot

Now you'll have a bot that connects to IRC. You can add your own plugins to customize how the bot interacts with different commands.

User Guide
----------

.. toctree::
   :maxdepth: 2

   user/installation
   user/quickstart
   user/plugins
   user/contribute

Included Plugins
----------------

.. toctree::
    :maxdepth: 1

    plugins/admin
    plugins/shortener