import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

# the float layout in kivy and how to dynamically place widgets 
# that will resize appropriately for all screen sizes.

class MyApp(App):
    def build(self):
        return FloatLayout()

if __name__== "__main__":
    MyApp().run()





