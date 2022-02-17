#!/usr/bin/python3
#
# Filename: 01_PyGObject_GTK_simple_form.py
#
# PyGObject / PyGTK tutorial 
#
# Simple PyGObject form
#
# Author: Mahdi Bahmani
# Website: itstorage.co
# Last edited: 2020/03/24 23:49

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#-----------------------------------------------------------------------
# https://pygobject.readthedocs.io/en/latest/getting_started.html

#   Create Widgets
#   Create a new window
window = Gtk.Window()

#  Set attributes
window.set_default_size(370, 200)

# Register callbacks
window.connect("destroy", Gtk.main_quit)

# Pack everything and display
window.show_all()

# GTK main loop
Gtk.main()

