#!/usr/bin/env python

import pygtk
import gtk

class HelloWorld:
    def delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?'
        # type dialogs.
        print "delete event occurred"

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False

    # Another callback
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(520, 240)
    
        # When the window is given the "delete_event" signal (this is given
        # by the window manager, usually by the "close" option, or on the
        # titlebar), we ask it to call the delete_event () function
        # as defined above. The data passed to the callback
        # function is NULL and is ignored in the callback function.
        self.window.connect("delete_event", self.delete_event)
    
        # Here we connect the "destroy" event to a signal handler.  
        # This event occurs when we call gtk_widget_destroy() on the window,
        # or if we return FALSE in the "delete_event" callback.
        self.window.connect("destroy", self.destroy)
    
        # Sets the border width of the window.
        self.window.set_border_width(10)
    
        # and the window
        self.window.show()

        vbox = gtk.VBox()
        self.window.add(vbox)
        vbox.show()

        # fortune title
        fortune_title = gtk.Label("your fortune title")
        fortune_title.show()

        # fortune description
        fortune_desc = gtk.Label("your fortune description")
        fortune_desc.show()

        vbox.pack_start(fortune_title, expand=False)
        vbox.pack_start(fortune_desc)

    def main(self):
        gtk.main()

hello = HelloWorld()
hello.main()
