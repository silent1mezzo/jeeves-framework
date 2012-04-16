# Jeeves settings


HOST = 'irc.freenode.net'
PORT = 6667 # 6697 for SSL
SSL = False 
SERVER_PASSWORD = None
PASSWORD = None
NICKNAME = 'Jeeves'
REALNAME = 'Jeeves Bot: A Framework for creating IRC Bots'

CHANNEL = '#jeeves'

PLUGINS = (
    #It is strongly recommended that you don't remove these jeeves.* plugins
    'jeeves.core.plugins.admin.HelpPlugin',
    'jeeves.core.plugins.shortener.ShortenPlugin',

    #Here you can add any of the plugins that you create.
    #'plugins.example.ExampleGenericPlugin',
    #'plugins.example.ExampleCommandPlugin',
)

"""
    Possible settings used for ShortenerPlugin
"""
# Backend shortening service. Defaults to google
SHORTENER_BACKEND = 'google'
# Login account. Defaults to None
SHORTENER_LOGIN = None
# API Key. Defaults to None
SHORTENER_API_KEY = None
