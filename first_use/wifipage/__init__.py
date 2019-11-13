import update_page as update_page
import passwordpage as password_page
from .handler import Handler

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


class WifiPage:
    def __init__(self):
        self.__builder = Gtk.Builder()                  # Initializing builder
        self.__builder.add_from_file('wifipage/wifi.glade')   # creating object from XML(.glade files)


# METHOD TO GO NEXT
# ----------------------------------------------------------------------------------------------------------------------
    def next(self, controller):
        controller.set_state(update_page.UpdatePage())

# METHOD TO GO BACK
# ----------------------------------------------------------------------------------------------------------------------
    def back(self, controller):
        controller.set_state(password_page.PasswordPage())

# METHOD TO GET XML OBJECT
# ----------------------------------------------------------------------------------------------------------------------
    def get_xml_object(self):
        return self.__builder.get_object('wifi')

# METHOD TO DESTROY ITSELF
# ----------------------------------------------------------------------------------------------------------------------
    def destroy(self):
        del self

# METHOD TO CONNECT HANDLER
# ----------------------------------------------------------------------------------------------------------------------
    def connect_handler(self, controller):
        self.__builder.connect_signals(Handler(controller))

# METHOD TO EXECUTE PAGE
# ----------------------------------------------------------------------------------------------------------------------
    def execute(self):
        pass
