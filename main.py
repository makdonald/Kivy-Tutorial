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

class Touch(Widget):
    button = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("Mouse Down", touch)
        self.button.opacity = 0.5

    def on_touch_move(self, touch):
        print("Mouse Move", touch)


    def on_touch_up(self, touch):
        print("Mouse Up", touch)
        self.button.opacity = 1



class MyApp(App):
    def build(self):
        return Touch()

if __name__== "__main__":
    MyApp().run()





