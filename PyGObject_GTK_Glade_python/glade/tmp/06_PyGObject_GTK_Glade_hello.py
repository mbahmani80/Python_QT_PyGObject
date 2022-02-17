#!/usr/bin/env python3
#===============================================================================
# 
#          FILES:
#                06_PyGObject_GTK_Glade_hello.py
#                06_PyGObject_GTK_Glade_hello.glade
#
#         USAGE: ./06_PyGObject_GTK_Glade_hello.py
# 
#   DESCRIPTION: This program creates a simple form with a label. 
#				 The form was designed via Glade then import to the 
#				 program. This way, the application interface will be 
#				 developed very quickly.
#                
# 
#       OPTIONS: ---
#  REQUIREMENTS: GTK+, Glade, Python3
#          BUGS: ---
#         NOTES: PyGTK Glade tutorial
#        AUTHOR: Mahdi Bahmani (), 
#  ORGANIZATION: www.itstorage.co
#       CREATED: 13.05.2020 18:59:07
#   LAST EDITED: 
#      REVISION: 1.1
#===============================================================================

import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow():
    def __init__(self):
        builder = Gtk.Builder()
        
        builder.add_from_file('glade/06_PyGObject_GTK_Glade_hello.glade')
        builder.connect_signals(self)
        self.label = builder.get_object('label')
        self.label.set_text('Hello World')

        window = builder.get_object('main_window')
        window.connect('delete-event', Gtk.main_quit)
        window.show_all()


if __name__ == '__main__':
    win = MyWindow()
    Gtk.main()
