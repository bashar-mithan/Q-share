#!/usr/bin/env python
import os, sys, logging
from enums import Location
from logger import logger

def build(system: sys) -> None:
    if (system == 'linux'):
        makeLinux()
    elif (system == 'windows'):
        pass



def makeLinux() -> None:
    bin_path = os.path.join(Location.home.value, 'bin')
    commandName = 'qshare'

    # Creating the bin directory at the home folder. home/USERNAME/bin
    if (not os.path.isdir(bin_path)):
        os.mkdir(bin_path)

    # creating a bash file named qshare (the command on terminal) at home/USERNAME/bin
    with open(os.path.join(bin_path, commandName), 'w') as commandFile:
        commandFile.write(f"python3 \"{Location.main.value}\" $1")
    
    # Making it excutable.
    os.system(f'chmod +x $HOME/bin/{commandName}')
    os.system('. ~/.profile')

def makeWindows() -> None:
    pass

try:
    build(system=sys.platform)
except:
    pass
else:
    logger.info("The project has been built sucessfully.")