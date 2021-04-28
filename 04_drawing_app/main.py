import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        # we use canvas property which is in Widget class
        with self.canvas:
            Color(0,1,0,.5, mode="rgba")
            Line(points=[0,0,100,100,100,200], width=10)
            Color(1,0,0,.5, mode="rgba")
            self.rect = Rectangle(pos=(0,0), size=(50,50))

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos    
        print("Mouse Down", touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Move", touch)


class MyApp(App):
    def build(self):
        return Touch()

if __name__== "__main__":
    MyApp().run()





