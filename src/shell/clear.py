import subprocess
import os

def clearTerminal():
    subprocess.call('cls' if os.name == 'nt' else 'clear',shell=True)