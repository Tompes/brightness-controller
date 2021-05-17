import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self, controller):
        self.controller = controller
        Gtk.Window.__init__(self, title="Chrome OS Brightness Controller")
        self.set_border_width(10)
        list_box = Gtk.ListBox()
        list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(list_box)

        row_1 = Gtk.ListBoxRow()
        row_1.set_selectable(False)
        list_box.add(row_1)

        self.value_label = Gtk.Label(label="Brightness:%d" % self.controller.get_brightness_num())
        row_1.add(self.value_label)

        row_2 = Gtk.ListBoxRow()
        list_box.add(row_2)
        self.scale_bar = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL,
                                   adjustment=Gtk.Adjustment(value=self.controller.get_brightness_num(), lower=5,
                                                             upper=100, step_increment=1))
        self.scale_bar.set_draw_value(False)
        self.scale_bar.connect("value-changed", self.changeBrightness)
        row_2.add(self.scale_bar)

        row_3 = Gtk.ListBoxRow()
        list_box.add(row_3)
        row_3_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_3.add(row_3_box)
        down_btn = Gtk.Button(label="<<")
        up_btn = Gtk.Button(label=">>")
        down_btn.connect("clicked", self.changBrightnessDown)
        up_btn.connect("clicked", self.changBrightnessUp)
        row_3_box.pack_start(down_btn, True, True, 0)
        row_3_box.pack_start(up_btn, True, True, 0)

    def start(self):
        win = self
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def changeBrightness(self, widget):
        self.controller.set_brightness_num(widget.get_value())
        self.value_label.set_text("Brightness: %d" % widget.get_value())

    def changBrightnessUp(self, widget):
        current_num = self.controller.get_brightness_num()
        self.scale_bar.set_value(min(current_num + 5, 100))

    def changBrightnessDown(self, widget):
        current_num = self.controller.get_brightness_num()
        self.scale_bar.set_value(max(current_num - 5, 0))

    def on_button_clicked(self, widget):
        print("Hello World")
