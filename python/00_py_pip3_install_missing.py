import pip
import sys
import os



#import os, vlc, eyed3
#from itertools import count
#from threading import Event
#import gi
#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk, GLib, Gio, GObject, GdkX11, GdkPixbuf
#gi.require_version('GdkX11', '3.0')

#import time, datetime
#from datetime import timedelta

#from multiprocessing.dummy import Pool as ThreadPool
#from os.path import basename, expanduser, isfile, join as joined



#'wheel','PyQt5','PyGObject','mysqlclient','mysql_connector_python','pip','setuptools','eyed3')]:
data = (['vlc','python_vlc'],['eyed3','eyed3'],['time','Time'],
        ['datetime','DateTime'], ['wheel','wheel'],['gi','PyGObject'],
        ['mysqlclient','mysqlclient'], 
        ['mysql.connector','mysql_connector_python'],
        
        )
for m, pkg in data:
    try:
        setattr(sys.modules[__name__], m, __import__(m))
    except ImportError:
        #pip.main(['install', pkg])
        os.system("sudo pip3 install "+ pkg)
        setattr(sys.modules[__name__], m, __import__(m))
