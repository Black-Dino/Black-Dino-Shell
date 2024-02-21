import socket
from ..styles.colors import colors

def getIp():
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    ip_with_styles = colors['WHITE'] + IPAddr + colors['CYAN'] 
    temp = f"""
+-----------------+
| {ip_with_styles} |
+-----------------+
    """
    print(colors['CYAN'],temp,end='')
    