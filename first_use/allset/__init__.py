import softwarepage as softwarepage
from .handler import Handler

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GdkPixbuf


class AllSet:

    def __init__(self):
        self.__builder = Gtk.Builder()                  # Initializing builder
        self.__builder.add_from_file('allset/all_set.glade')   # creating object from XML(.glade files)
        
        self.pixbufanim = GdkPixbuf.PixbufAnimation.new_from_file('img/raspberry.gif')
        self.image = self.__builder.get_object("gif")
        self.image.set_from_animation(self.pixbufanim)
        self.image.show()
        
        

    def next(self, controller):
        pass

    def back(self, controller):
        controller.set_state(softwarepage.SoftwarePage())

    def get_xml_object(self):
        return self.__builder.get_object('all_set')

    def destroy(self):
        del self

    def connect_handler(self, controller):
        self.__builder.connect_signals(Handler(controller))
