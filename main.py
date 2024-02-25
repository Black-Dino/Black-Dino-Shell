from src.commands import commands,commands_has_params
from src.banner import banner
from src.styles.colors import colors, initColors
from run_command import runSimpleCommands,runCommandsHasParams

# init colors
initColors()
try:
    banner() # show banner
    while True:
        # get commands from user
        print()
        user = input(colors['RED']+'> '+colors['WHITE']).split(' ')

        # exit shell
        if user == 'exit':
            print("Bye :D")
            break
        
        # some commands has params in here check that
        if runCommandsHasParams(user):
            pass
        else:                    
            runSimpleCommands(user)

# when user tapped CTRL + C this line of code will running
except KeyboardInterrupt:
    print('')
    
