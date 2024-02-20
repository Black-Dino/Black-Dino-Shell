from src.commands import commands
from src.banner import banner
from src.styles.colors import colors, initColors

# init colors
initColors()
try:
    banner() # show banner
    while True:
        # get commands from user
        print()
        user = input(colors['RED']+'> '+colors['WHITE'])

        # exit shell
        if user == 'exit':
            print("Bye :D")
            break

        try:
            # run commands
            commands[user]()
        except:
            print("wrong commands")

# when user tapped CTRL + C this line of code will running
except KeyboardInterrupt:
    print('')
    
