#!/usr/bin/env python

import pygtk
import gtk

class HelloWorld:
    def delete_event(self, widget, event, data=None):
        return False

    # Another callback
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(520, 240)
        self.window.set_title("unmaintainable code fortunes")
    
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
    
        # Sets the border width of the window.
        self.window.set_border_width(10)
    
        # and the window
        self.window.show()

        vbox = gtk.VBox()
        self.window.add(vbox)
        vbox.show()

        # fortune title
        fortune_title = gtk.Label("<b>your fortune title</b>")
        fortune_title.set_use_markup(True)
        fortune_title.set_alignment(0, 0.5)
        fortune_title.set_justify(gtk.JUSTIFY_LEFT)
        fortune_title.show()

        # fortune description
        fortune_desc = gtk.Label("your fortune description")
        fortune_desc.set_justify(gtk.JUSTIFY_LEFT)
        fortune_desc.set_alignment(0, 0.25)
        fortune_desc.show()

        vbox.pack_start(fortune_title, expand=False)
        vbox.pack_start(fortune_desc)

    def main(self):
        gtk.main()

hello = HelloWorld()
hello.main()
