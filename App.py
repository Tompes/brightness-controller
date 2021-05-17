import gi

from core.utils.ShellUtils import sudoTest

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from core.actions.BrightnessActions import BrightnessActions
from core.ui.AuthorizationDialog import AuthorizationDialog
from core.ui.MainWindow import MainWindow


def validate_response(dialog, response_id):
    # validate
    if response_id == Gtk.ResponseType.OK:
        dialog.destroy()
    else:
        print("Something went wrong")
    return True


if __name__ == "__main__":
    sudo_pass = ""
    if not sudoTest(""):
        dialog = AuthorizationDialog()
        response = dialog.run()
        dialog.connect("response", validate_response)

        if response == Gtk.ResponseType.OK:
            print(dialog.get_entry_value())
            if sudoTest(dialog.get_entry_value()):
                sudo_pass = dialog.get_entry_value()
                print('pass')
                dialog.destroy()

                controller = BrightnessActions(sudo_pass=sudo_pass, window=Gtk.Window())
                window = MainWindow(controller)
                window.start()

            else:
                print('wrong')
                exit("WRONG PASS")
                # dialog.dialog_ok_btn.stop_emission_by_name("destroy")
                # dialog.entry.set_text("")
                # pass  # DO SOMETHING
        elif response == Gtk.ResponseType.CANCEL:
            # dialog.destroy()
            exit("PERMISSION DENIED!")
    else:
        controller = BrightnessActions(sudo_pass=sudo_pass, window=Gtk.Window())
        window = MainWindow(controller)
        window.start()