import sys
import os

from twisted.internet import reactor
from distutils.dir_util import copy_tree
from jeeves.utils.importlib import import_module
from jeeves.core.exceptions import InvalidCommand

def create_project(name):
    try:
        import_module(name)
    except ImportError:
        pass
    else:
        raise InvalidCommand("%r conflicts with the name of an existing "
                               "Python module and cannot be used as a "
                               "project name. Please try another name." %
                               name)
    cur_path = '%s/%s' % (os.getcwd(), name)
    encoding = sys.getfilesystemencoding()
    project_template = '%s/../../conf/project_template/' % os.path.dirname(unicode(__file__, encoding))
    if not os.path.exists(cur_path):
        copy_tree(project_template, cur_path)

def run_bot():
    from jeeves.conf import settings
    from jeeves.core.bot import BotFactory
    reactor.connectTCP(
        settings.HOST,
        settings.PORT,
        BotFactory(
            channel=settings.CHANNEL,
            nickname=settings.NICKNAME
        )
    )
    reactor.run()


def execute_from_command_line(argv=None):
    command = argv[0]
    options = argv[1:]

    if command == 'startbot':
        if len(options) == 0:
            sys.stdout.write("You must supply the name of the bot you'd like to create.\n")
        else:
            create_project(options[0])
    elif command == 'runbot':
        run_bot()
    else:
        print "jeeves-admin.py only supports `startbot` and `runbot`"
