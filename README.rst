Jeeves Framework
================
The Jeeves Framework is a Python IRC library that makes creating and running IRC bots. A few of the core principles were borrowed from `Django <http://djangoproject.com>`_. The basic idea came when I read about Jessamyn Smith's `Talk Balk Bot <https://github.com/jessamynsmith/talkbackbot>`_.  

Prerequisites
+++++++++++++

* `Twisted  <http://twistedmatrix.com/trac/>`_

Usage
+++++
The following four commands will get a basic IRC bot up and running. Default plugins are in the works for future releases.

* \`pip install git+git://github.com/silent1mezzo/jeeves-framework.git`
* \`jeeves-admin.py startbot <name>`
* \`cd <name>`
* \`python bot.py runbot`

Upcoming Features
+++++++++++++++++
Here's an idea dump for upcoming features

* Admin plugin (Basic IRC administration commands)
* Google plugin (Link shortening, search)