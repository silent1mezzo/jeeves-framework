from jeeves.conf import settings

def pop_message(lst, item):
    index = lst.index(item)
    lst.pop(index)
    return lst
'''
    Parses a given message directed at the bot.

    e.g. you: botname <command> query (In a public channel)
    e.g. you: <command> query (In a private channel with the bot)

    Returns:
        Nickame (Optional) - Bots nickname (not needed in private channel)
        Command - Command used for a given plugin
        Query - Passed to the plugin
'''
def parse_message(message, commands):
    nick = settings.NICKNAME.lower()
    plugin_command = None
    tokenized_msg = message.lower().split()

    if nick == tokenized_msg[0] or '%s:' % nick == tokenized_msg[0]:
        nickname = nick
        try:
            tokenized_msg = pop_message(tokenized_msg, nick)
        except ValueError:
            # Happens when users calls bot with `BotName: msg`
            tokenized_msg = pop_message(tokenized_msg, '%s:' % nick)
    else:
        nickname = None

    for command in commands:
        if command.lower() == tokenized_msg[0]:
            plugin_command = command
            tokenized_msg = pop_message(tokenized_msg, command.lower())

    message = ' '.join(tokenized_msg)
    return (nickname, plugin_command, message)
