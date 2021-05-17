import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def info_dialog(window, message):
    dialog = Gtk.MessageDialog(
        transient_for=window,
        flags=0,
        message_type=Gtk.MessageType.INFO,
        buttons=Gtk.ButtonsType.OK,
        text="INFO",
    )
    dialog.format_secondary_text(
        message
    )
    dialog.run()
    print("INFO dialog closed")
    dialog.destroy()


def error_dialog(window, message):
    dialog = Gtk.MessageDialog(
        transient_for=window,
        flags=0,
        message_type=Gtk.MessageType.ERROR,
        buttons=Gtk.ButtonsType.CANCEL,
        text="ERROR",
    )
    dialog.format_secondary_text(message)
    dialog.run()
    print("ERROR dialog closed")
    dialog.destroy()
    exit(message)


def warn_dialog(window, widget):
    dialog = Gtk.MessageDialog(
        transient_for=window,
        flags=0,
        message_type=Gtk.MessageType.WARNING,
        buttons=Gtk.ButtonsType.OK_CANCEL,
        text="This is an WARNING MessageDialog",
    )
    dialog.format_secondary_text(
        "And this is the secondary text that explains things."
    )
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        print("WARN dialog closed by clicking OK button")
    elif response == Gtk.ResponseType.CANCEL:
        print("WARN dialog closed by clicking CANCEL button")

    dialog.destroy()


def question_dialog(window, widget):
    dialog = Gtk.MessageDialog(
        transient_for=window,
        flags=0,
        message_type=Gtk.MessageType.QUESTION,
        buttons=Gtk.ButtonsType.YES_NO,
        text="This is an QUESTION MessageDialog",
    )
    dialog.format_secondary_text(
        "And this is the secondary text that explains things."
    )
    response = dialog.run()
    if response == Gtk.ResponseType.YES:
        print("QUESTION dialog closed by clicking YES button")
    elif response == Gtk.ResponseType.NO:
        print("QUESTION dialog closed by clicking NO button")

    dialog.destroy()