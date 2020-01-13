import gi
from .handler import Handler

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Header:
    def __init__(self):
        self.__builder = Gtk.Builder()                  # Initializing builder
        self.__builder.add_from_file('header/header.glade')   # creating object from XML(.glade files)
        self.set_header()
        
        self.handler = Handler(builder=self.__builder)
        
    
    def next(self, controller):
        # there will be page where i was 
        pass
    
    
    def back(self, controller):
        #controller.set_state()
        pass
        
    def get_xml_object(self):
        return self.__builder.get_object('header')

    def destroy(self):
        del self

    def connect_handler(self, controller):
        self.handler.add_controller(controller)
        self.__builder.connect_signals(self.handler)
        
# SETTING HEADER
# --------------------------------------------------------------------------------------------------------------
    def set_header(self):
        header = self.__builder.get_object('header')
        
        header.set_show_close_button(True)

        
        box = self.__builder.get_object('box')
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        button = self.__builder.get_object('left')
        button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        
        button = self.__builder.get_object('right')
        button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))

# SETTING TITLE OF HEADER
# ----------------------------------------------------------------------------------------------------------------------

    def set_title(self, title):
        header = self.__builder.get_object('header')
        header.props.title = title

    def get_back_button(self):
        return self.__builder.get_object('left')

    def get_next_button(self):
        self.__builder.get_object('right')
        
        
        