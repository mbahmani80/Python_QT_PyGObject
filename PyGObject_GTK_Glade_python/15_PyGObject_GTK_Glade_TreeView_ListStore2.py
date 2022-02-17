#!/usr/bin/env python3`

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib


class linFitApp(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title='Testing Keypress Events on Treeview')
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(400, 300)
        self.set_border_width(5)

        self.mainBox = Gtk.Box()
        self.scrollTableWindow = Gtk.ScrolledWindow()
        self.scrollTableWindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.mainBox.pack_start(self.scrollTableWindow, False, False, 0)
        self.add(self.mainBox)

        ############################################################################


        #Now to set up the data table
        self.dataTableListStore = Gtk.ListStore(float, float, float, float)
        self.dataTableTreeView = Gtk.TreeView(model=self.dataTableListStore)
        self.dataTableTreeView.props.activate_on_single_click = True
        self.dataTableTreeView.connect("key-press-event", self.onTreeNavigateKeyPress)

        #set up the x column
        self.xColumnTextRenderer = Gtk.CellRendererText()
        self.xColumnTextRenderer.set_property("editable", True)
        self.xColumnTextRenderer.connect("edited", self.onXChanged)
        self.xColumnTreeView = Gtk.TreeViewColumn("x", self.xColumnTextRenderer, text=0)

        #set up the y column
        self.yColumnTextRenderer = Gtk.CellRendererText()
        self.yColumnTextRenderer.set_property("editable", True)
        self.yColumnTextRenderer.connect("edited",self.onYChanged)
        self.yColumnTreeView = Gtk.TreeViewColumn("y", self.yColumnTextRenderer, text=1)

        #set up the dx column
        self.dxColumnTextRenderer = Gtk.CellRendererText()
        self.dxColumnTextRenderer.set_property("editable", True)
        self.dxColumnTextRenderer.connect("edited",self.onDxChanged)
        self.dxColumnTreeView = Gtk.TreeViewColumn("dx", self.dxColumnTextRenderer, text=2)

        #set up the dy column
        self.dyColumnTextRenderer = Gtk.CellRendererText()
        self.dyColumnTextRenderer.set_property("editable", True)
        self.dyColumnTextRenderer.connect("edited",self.onDyChanged)
        self.dyColumnTreeView = Gtk.TreeViewColumn("dy", self.dyColumnTextRenderer, text=3)

        #pack treeview into the scrolled window
        self.scrollTableWindow.add(self.dataTableTreeView)

        #add treeview columns to treeview
        self.dataTableTreeView.append_column(self.xColumnTreeView)
        self.dataTableTreeView.append_column(self.yColumnTreeView)
        self.dataTableTreeView.append_column(self.dxColumnTreeView)
        self.dataTableTreeView.append_column(self.dyColumnTreeView)

        #fill in treeview with some sample data
        self.dataTableListStore.append([0, 4, 0, 0])
        self.dataTableListStore.append([5, 8.2, 0, 0])
        self.dataTableListStore.append([10, 11.7, 0, 0])
        self.dataTableListStore.append([15, 16.5, 0, 0])
        self.dataTableListStore.append([20, 19, 0, 0])
        self.dataTableListStore.append([25, 24.5, 0, 0])
        self.dataTableListStore.append([30, 26.2, 0, 0])



    #define the callbacks for cell editing
    def onXChanged(self, widget, path, number):
        self.dataTableListStore[path][0]=float(number.replace(',', '.'))

    def onYChanged(self, widget, path, number):
        self.dataTableListStore[path][1]=float(number.replace(',', '.'))

    def onDxChanged(self, widget, path, number):
        self.dataTableListStore[path][2]=float(number.replace(',', '.'))

    def onDyChanged(self, widget, path, number):
        self.dataTableListStore[path][3]=float(number.replace(',', '.'))

    #define the callback for keypress events
    def onTreeNavigateKeyPress(self, treeview, event):
        keyname = Gdk.keyval_name(event.keyval)
        path, col = treeview.get_cursor()
        columns = [c for c in treeview.get_columns()] 
        colnum = columns.index(col)        

        if keyname == 'Tab':

            if colnum + 1 < len(columns):
                next_column = columns[colnum + 1]
            else: 
                next_column = columns[0]
            GLib.timeout_add(50,
                             treeview.set_cursor,
                             path, next_column, True)


        elif keyname == 'Return':

            model = treeview.get_model()
            #Check if currently in last row of Treeview
            if path.get_indices()[0] + 1 == len(model):
                path = treeview.get_path_at_pos(0,0)[0]
                #treeview.set_cursor(path, columns[colnum], True)
                GLib.timeout_add(50,
                             treeview.set_cursor,
                             path, columns[colnum], True)
            else:
                path.next()
                #treeview.set_cursor(path, columns[colnum], True)
                GLib.timeout_add(50,
                             treeview.set_cursor,
                             path, columns[colnum], True)
        else:
            pass


#create main application window and start Gtk loop
mainWindow = linFitApp()
mainWindow.connect("delete-event", Gtk.main_quit)
mainWindow.show_all()
Gtk.main()
