#! usr/bin/env python 3

import webbrowser, sys, pyperclip

sys.argv #['mapit.py', '870', 'Valencia', 'St.']
if len(sys.argv)>1:
    #['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else :
    address = pyperclip.paste()

webbrowser.open('https://www.google.fr/maps/place/'+address)
