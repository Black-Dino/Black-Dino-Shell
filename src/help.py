from .styles.colors import colors

def showCommandsSection():
    line  = colors['CYAN'] + "------------------------------------" + colors['WHITE']
    helpMenu = f"""
    network:            
        you can use network in this app
        
        showing network help menu by write:
            network -h
            network --help
    {line}
    shell:              
        run shell commands
    {line}
    random:             
        random generator such as(int, uuid, password, string, token)
    {line}
    filesystem:         
        using filesystem such as(read, write, delete, show directory and more...)
    {line}
    """

    print(helpMenu)