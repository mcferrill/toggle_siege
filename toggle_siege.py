#!/usr/bin/env python

import sys
import os

INSTALL_PATH = "D:/Program Files/Steam/steamapps/common/Tom Clancy's Rainbow Six Siege/"
DEFAULT = os.path.join(INSTALL_PATH, 'defaultargs.dll')
UPLAY_BACKUP = os.path.join(INSTALL_PATH, 'defaultargs_uplay.dll')
STEAM_BACKUP = os.path.join(INSTALL_PATH, 'defaultargs_steam.dll')


if __name__ == '__main__':

    option = None
    if sys.argv[-1].lower() in ('uplay', 'steam'):
        option = sys.argv[1].lower()
    elif os.path.exists(STEAM_BACKUP):
        option = 'steam'
    elif os.path.exists(UPLAY_BACKUP):
        option = 'uplay'
    else:
        print('No defaultargs backup found. You\'ll have to rename your '
        'defaultargs.dll to defaultargs_<platform>.dll and run "repair '
        'game" from the other launcher in order to have both DLLs available.')
        raise SystemExit

    if option == 'steam' and os.path.exists(STEAM_BACKUP):
        os.rename(DEFAULT, UPLAY_BACKUP)
        os.rename(STEAM_BACKUP, DEFAULT)
        print('Switched to steam version')
    elif option == 'uplay' and os.path.exists(UPLAY_BACKUP):
        os.rename(DEFAULT, STEAM_BACKUP)
        os.rename(UPLAY_BACKUP, DEFAULT)
        print('Switched to uplay version')
    else:
        print('Already using %s version.' % option)
