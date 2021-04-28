import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# navigating between multiple screens using a screenmanager in kivy. 
# It will show you how to create multiple windows/screens and 
# transition between them.

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

# linke .kv file with application
kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__== "__main__":
    MyMainApp().run()





