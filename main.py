from src.commands import commands
from src.banner import banner
from src.styles.colors import colors, initColors
# while True:

initColors()
try:
    banner()
    while True:
        print()
        user = input(colors['RED']+'> '+colors['WHITE'])

        # exit shell
        if user == 'exit':
            print("Bye :D")
            break

        try:
            commands[user]()
        except:
            print("wrong commands")

# when user tapped CTRL + C this line of code will running
except KeyboardInterrupt:
    print('')
    
