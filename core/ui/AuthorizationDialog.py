import gi

from core.utils.ShellUtils import sudoTest

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class AuthorizationDialog(Gtk.Dialog):
    def __init__(self):
        Gtk.Dialog.__init__(self, title="Authorization", transient_for=Gtk.Window(), flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL
        )
        self.change_entry_back(0)

        self.set_default_size(150, 100)
        box = self.get_action_area()
        self.ok_btn = Gtk.Button(label="OK")
        self.ok_btn.connect('clicked', self.test, self)
        box.add(self.ok_btn)
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Password")
        self.entry.set_visibility(False)
        box = self.get_content_area()
        box.add(self.entry)
        self.entry.connect('changed', self.entry_input)
        self.entry.connect("key-press-event", self.entry_key_pressed)

        self.show_all()

    def get_entry_value(self):
        return self.entry.get_text()

    def test(self, btn, id):
        self.entry.set_sensitive(False)
        self.change_entry_back(2)
        if sudoTest(self.get_entry_value()):
            self.response(Gtk.ResponseType.OK)
        else:
            self.change_entry_back(1)
            self.entry.set_sensitive(True)
            print("FALSE")

    def change_entry_back(self, code):
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        if code == 0:
            css = b"""
                    entry {
                            background: transparent;
                    }
            """
        elif code == 1:
            css = b"""
                    entry {
                            background: red;
                    }
            """
        elif code == 2:
            css = b"""
                    entry {
                            background: #cccccc;
                    }
            """
        else:
            css = b"""
                    entry {
                            background: transparent;
                    }
            """
        provider.load_from_data(css)

    def entry_input(self, widget):
        self.change_entry_back(0)
        pass

    def entry_key_pressed(self, widget, event):
        if event.keyval == 65293:
            self.test(self.ok_btn, 0)
            pass
