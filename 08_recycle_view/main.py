import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

from kivy.app import App
from kivy.uix.recycleview import RecycleView

class RV(RecycleView):
    def __init__(self):
        super().__init__()
        content = ['first button', 'second button', 'third button']
        self.data = [{'text': item} for item in content]

class MyApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    MyApp().run()