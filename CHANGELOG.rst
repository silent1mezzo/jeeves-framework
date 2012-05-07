CHANGELOG
---------

0.4.0 (2012-05-07)
++++++++++++++++++

* Adds cache support (local memory and memcached)
* Adds TicketBot Plugin
* Moved ShortenerPlugin from jeeves.core to jeeves.contrib (BACKWARDS INCOMPATIBILITY)

0.3.1 (2012-04-19)
++++++++++++++++++

* Fixed bug with example plugins.
* No longer supports Python2.5 due to python-requests

0.3.0 (2012-04-16)
++++++++++++++++++

* Bots can now log in to private channels
* Bots can now connect over SSL
* `Requests <>`_ is now an official requirement
* Added basic documentation

0.2.1 (2012-04-12)
++++++++++++++++++

* Fixed URL shortening bug

0.2.0 (2012-04-12)
++++++++++++++++++

* Help Plugin now displays help in a private message
* Plugin isolation
* Jeeves now handles its own nickname changes (`#16 <https://github.com/silent1mezzo/jeeves-framework/issues/16>`_)

0.1.2 (2012-04-09)
++++++++++++++++++

* Help Plugin (`#8 <https://github.com/silent1mezzo/jeeves-framework/issues/8>`_)
* Plugins can now manage multiple commands (`#12 <https://github.com/silent1mezzo/jeeves-framework/issues/12>`_)
* Tests are now passing on `Travis-CI <http://travis-ci.org/#!/silent1mezzo/jeeves-framework>`_

0.1.1 (2012-04-09)
++++++++++++++++++

* Plugins can now have help text (`#9 <https://github.com/silent1mezzo/jeeves-framework/issues/9>`_)
* Fixed bug where commands would run even if they weren't exact. (`#10 <https://github.com/silent1mezzo/jeeves-framework/issues/10>`_)

0.1.0 (2012-04-06)
++++++++++++++++++

* Conception (Initial idea from https://github.com/jessamynsmith/talkbackbot)
