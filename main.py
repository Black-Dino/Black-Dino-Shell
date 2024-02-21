from src.commands import commands,commands_has_params
from src.banner import banner
from src.styles.colors import colors, initColors

def gol(num):
    print('here oomad')
    print(num)

testing = {
    "ping":gol
}

# init colors
initColors()
try:
    banner() # show banner
    while True:
        # get commands from user
        print()
        user = input(colors['RED']+'> '+colors['WHITE']).split(' ')
        print(user)
        print(commands[user[0]])
        # exit shell
        if user == 'exit':
            print("Bye :D")
            break
        
        # some commands has params in here check that
        if commands[user[0]] == 'has_params':
            args = user[1:]
            commands_has_params[user[0]](args)
            break
        
        try:
            # run commands
            commands[user[0]]()
        except:
            print("wrong commands")

# when user tapped CTRL + C this line of code will running
except KeyboardInterrupt:
    print('')
    
