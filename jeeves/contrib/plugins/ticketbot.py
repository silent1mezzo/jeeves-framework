"""
The following code has been modified from https://github.com/idangazit/django-ticketbot/.
"""

"""
Copyright (c) 2011 Idan Gazit and Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyrigh
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.

    3. Neither the name of this project nor the names of its contributors may
       be used to endorse or promote products derived from this software without
       specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from jeeves.conf import settings
from jeeves.core.plugin import GenericPlugin
from jeeves.core import exceptions

import re

ticket_re = re.compile(r'(?<!build)(?:^|\s)#(\d+)')

changeset_re = re.compile(r'\br(\d+)\b')
changeset_re2 = re.compile(r'(?:^|\s)\[(\d+)\]')

changeset_regit = re.compile(r'\b[0-9a-f]{7,40}\b')

class TicketBotPlugin(GenericPlugin):
    name = 'TicketBot Plugin'
    help_text = 'This is the help text for a generic plugin.'

    def __init__(self, *args, **kwargs):
        self.ticket_url = getattr(settings, 'TICKETBOT_TICKET_URL', None)
        if not self.ticket_url:
            raise exceptions.ImproperlyConfigured(
                "You need to specify TICKETBOT_TICKET_URL in settings.py."
            )

        self.changeset_url = getattr(settings, 'TICKETBOT_CHANGESET_URL', None)
        if not self.changeset_url:
            raise exceptions.ImproperlyConfigured(
                "You need to specify TICKETBOT_CHANGESET_URL in settings.py."
            )

        super(TicketBotPlugin, self).__init__(self.name, *args, **kwargs)

    def handle_message(self, channel, nickname, message):
        """This will get called when the bot receives a message."""
        tickets = ticket_re.findall(message)
        changesets = changeset_re.findall(message)
        changesets.extend(changeset_re2.findall(message))
        changesets.extend(changeset_regit.findall(message))

        # Check to see if they're sending me a private message
        if channel == nickname:
            target = nickname
        else:
            target = channel

        if message.startswith(settings.NICKNAME) and not tickets and not changesets:
            self.say(nickname, "Hi, I'm Django's ticketbot. I know how to linkify tickets like \"#12345\", and changesets like \"r12345\" or \"[12345]\".")
            return

        for ticket in set(tickets):
            self.say(target, self.ticket_url % ticket)
        for changeset in set(changesets):
            self.say(target, self.changeset_url % changeset)
        return
