# http
# network
# file system
# path
from .network.ip import getIp
from .network.mac import getMac
from .network.ping import ping
from .network.help import networkHelp
from .shell.clear import clearTerminal
from .path.pwd import currentPath
from .help import showCommandsSection

path = {
    # get current path
    'pwd':''
}

filesystem = {
    # list of file and folders
    'ls':'',
    'cat':'',
    'tail':'',
    'rm':''
}

network = {
}

commands = {
    'help':showCommandsSection,

    # shell
    'cls':clearTerminal,
    'clear':clearTerminal,

    # network help menu
    'network':networkHelp,
    'network -h':networkHelp,
    'network --help':networkHelp,
    'ip':getIp,
    'ifconfig':getIp,
    'mac':getMac,
    'ping':'has_params',
    
    # path
    'pwd':currentPath
}

commands_has_params = {
    'ping':ping
}