import os

from kivy.uix.widget import Widget
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        print("INIT W: " + str(self.width) + " H:" + str(self.height))

    def on_parent(self, widget, parent):
        #print("ON PARENT W: " + str(self.width) + " H:" + str(self.height))
        pass

    def on_size(self, *args):
        print("ON SIZE W: " + str(self.width) + " H:" + str(self.height))
        #self.perspective_point_x = self.width/2
        #self.perspective_point_y = self.height * .75

    def on_perspective_point_x(self, widget, value):
        print("PX: " + str(value))

    def on_perspective_point_y(self, widget, value):
        print("PY: " + str(value))


class SpaceWayApp(App):
    pass


if __name__ == '__main__':
    SpaceWayApp().run()