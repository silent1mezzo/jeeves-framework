from jeeves.conf import settings
'''
    Parses a given message directed at the bot.

    e.g. you: botname <command> query (In a public channel)
    e.g. you: <command> query (In a private channel with the bot)

    Returns:
        Nickame (Optional) - Bots nickname (not needed in private channel)
        Command - Command used for a given plugin
        Query - Passed to the plugin
'''
def parse_message(msg, commands):
    msg = msg.lower()
    nick = settings.NICKNAME.lower()
    plugin_command = None

    index = msg.find(nick)
    if index != -1:
        nickname = msg[index:len(nick)]
        msg = msg.replace('%s:' % nick, '')
        msg = msg.replace(nick, '')
    else:
        nickname = None

    for command in commands:
        if msg.find(command.lower()) != -1:
            plugin_command = command

    return (nickname, plugin_command, msg)
