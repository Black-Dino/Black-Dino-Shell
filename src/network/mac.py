from getmac import get_mac_address as gma
from ..styles.colors import  colors

def getMac():
    mac_with_styles = colors['WHITE'] + gma() + colors['CYAN'] 
    temp = f"""
+-------------------+
| {mac_with_styles} |
+-------------------+
    """
    print(colors['CYAN'] + temp,end='')

