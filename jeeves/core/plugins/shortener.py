from jeeves.conf import settings
from jeeves.core.plugin import CommandPlugin
from jeeves.core import exceptions
import unicodedata

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise ImportError("You need to have a json parser, easy_install simplejson")

import requests

VALID_BACKENDS = [
    'google',
    'bitly',
    'isgd',
]

"""
    Shorten Plugin.
    A basic Jeeves plugin that displays help messages for the user. T
"""
class ShortenPlugin(CommandPlugin):
    name = 'Shorten Plugin'
    command = ['shorten', '-s']

    def __init__(self, *args, **kwargs):
        backend = getattr(settings, 'SHORTENER_BACKEND', None)
        if not backend:
            raise exceptions.ImproperlyConfigured(
                "You need to specify SHORTENER_BACKEND in settings.py. Valid backends include: %s" % ', '.join(VALID_BACKENDS)
            )
        elif backend not in VALID_BACKENDS:
            raise exceptions.ImproperlyConfigured(
                "You must specify a valid backend. Valid backends include: %s" % ', '.join(VALID_BACKENDS)
            )
        else:
            self.backend = backend

        if backend == 'bitly' and not getattr(settings, 'SHORTENER_LOGIN', None) and not getattr(settings, 'SHORTENER_API_KEY', None):
            raise exceptions.ImproperlyConfigured(
                "You need to specify SHORTENER_LOGIN and SHORTENER_API_KEY when using bit.ly"
            )

        super(ShortenPlugin, self).__init__(self.name, self.command, *args, **kwargs)

    def handle_message(self, channel, nickname, message, command):
        tokenized_msg = message.split()
        if len(tokenized_msg) != 1:
            self.say(nickname, "%s: %s" % (nickname, self.help_text))
        else:
            short_url = None
            if self.backend == 'google':
                # Grab shortened URL from Google.
                short_url = shorten_google(tokenized_msg[0])
            elif self.backend == 'bitly':
                short_url = shorten_bitly(tokenized_msg[0])
            elif self.backend == 'isgd':
                short_url = shorten_isgd(tokenized_msg[0])

            if short_url:
                self.say(nickname, "%s" % short_url)
            else:
                self.say(nickname, "There was an error shortening your link")

    @property
    def help_text(self):
        help_text = [
            "usage: Jeeves: [shorten|-s] <link>",
        ]

        return help_text

def normalize_unicode(text):
    return unicodedata.normalize('NFKD', text).encode('ascii','ignore')

def shorten_bitly(url):
    long_url = "https://api-ssl.bitly.com/v3/shorten"
    login = getattr(settings, 'SHORTENER_LOGIN', None)
    api_key = getattr(settings, 'SHORTENER_API_KEY', None)
    data = {'login': login, 'apiKey': api_key, 'longUrl': url, 'format': 'json'}

    results = requests.post(long_url, data=data)
    results = json.loads(results.text)

    short_url = results.get('data', None)
    if short_url:
        return normalize_unicode(short_url.get('url'))
    else:
        return None

def shorten_isgd(url):
    long_url = "http://is.gd/create.php"

    data = {'format': 'json', 'url': url}
    results = requests.post(long_url, data=data)

    results = json.loads(results.text)
    short_url = results.get('shorturl', None)
    if short_url:
        return normalize_unicode(short_url)
    else:
        return None

def shorten_google(url):
    long_url = "https://www.googleapis.com/urlshortener/v1/url"

    headers = {'content-type': 'application/json'}
    results = requests.post(long_url, json.dumps(dict(longUrl=url)), headers=headers)

    results = json.loads(results.text)
    short_url = results.get('id', None)
    if short_url:
        return normalize_unicode(short_url)
    else:
        return None
