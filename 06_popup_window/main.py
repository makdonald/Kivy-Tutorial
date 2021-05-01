import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

# create a popup window in kivy. Popup windows are very easy to create 
# and have a large degree of customization. This tutorial will show you 
# how to create and trigger a popup window.

class Widgets(Widget):
    def btn(self):
        show_popup()

# class with our content for show_popup function
class P(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        #return kv
        return Widgets()

def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None), size=(400,400))

    popupWindow.open()

if __name__== "__main__":
    MyApp().run()





