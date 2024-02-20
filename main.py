from src.commands import commands

# while True:

try:
    while True:
        user = input('> ')

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
    
