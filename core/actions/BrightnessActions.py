import os

from core.ui.MessageDialog import error_dialog
from core.utils.ShellUtils import executeScript


class BrightnessActions:
    path = ""
    sudo_pass = ""
    window = None

    def __init__(self, sudo_pass, window):
        self.sudo_pass = sudo_pass
        self.window = window
        print("> INITIALIZING...")
        print("> SCANNING BRIGHTNESS FILE PATH...")
        self.get_brightness_file_path()

        if self.path == "":
            print("<<< FAILURE TO SCANNING BRIGHTNESS FILE PATH...")
            error_dialog(window=self.window, message="ERROR:BRIGHTNESS CONFIG FILE WAS NOT BE SPECIFIED!")

        print("> BRIGHTNESS FILE PATH : " + self.path)

        print("> SETTING PERMISSION OF BRIGHTNESS CONFIG FILE...")
        self.set_config_file_permission()
        print("> PERMISSION OK!")
        print(">>>>>>>>>>> ALL DONE. <<<<<<<<<<<")
        pass

    def get_brightness_file_path(self):
        err, path = executeScript("cd $(dirname $(find /sys -name brightness));pwd")
        if err == 0:
            self.path = str(path, "utf8").strip() + "/brightness"
        return path

    def set_config_file_permission(self):
        err, out = executeScript("echo '%s' | sudo -S chown ${USER:=$(/usr/bin/id -run)}:$USER %s" % (self.sudo_pass,
                                                                                                      self.path))
        if err != 0:
            print("<<< ERROR: FAILURE SET PERMISSION!")
            error_dialog(window=self.window, message="ERROR: FAILURE SET PERMISSION!")

    def get_brightness_num(self):
        err, num = executeScript("cat %s" % self.path)
        return int(num)

    def set_brightness_num(self, value):
        err, num = executeScript("echo %d > %s" % (value, self.path))
        if err == 0:
            return True
        return False
