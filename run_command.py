from src.commands import commands,commands_has_params


def runSimpleCommands(user):
    try:
        commands[user[0]]()
    except:
        print('wrong pass')


def runCommandsHasParams(user):
    if commands[user[0]] == 'has_params':
        args = user[1:]
        commands_has_params[user[0]](args)
        return True;