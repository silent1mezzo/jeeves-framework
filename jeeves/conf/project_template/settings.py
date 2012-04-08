# Jeeves settings


HOST = 'irc.freenode.net'
PORT = 6667
PASSWORD = None
NICKNAME = 'Jeeves'
REALNAME = 'Jeeves Bot: A Framework for creating IRC Bots'

CHANNEL = '#jeeves'

PLUGINS = (
    #It is strongly recommended that you don't remove these jeeves.* plugins
    'jeeves.plugins.admin.HelpPlugin',

    #Here you can add any of the plugins that you create.
    #'plugins.example.ExampleGenericPlugin',
    #'plugins.example.ExampleCommandPlugin',
)
