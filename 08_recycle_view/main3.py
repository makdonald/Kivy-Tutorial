import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')


from kivy.app import App, ObjectProperty 
from kivy.uix.recycleview import RecycleView 
from kivy.lang import Builder
from kivy.uix.button import Button

KV = """
<RV>: 
    viewclass: 'CustomButton' # defines the viewtype for the data items. 
    orientation: "vertical"
    spacing: 40
    padding:10, 10
    space_x: self.size[0]/3

    RecycleBoxLayout: 
        color:(0, 0.7, 0.4, 0.8) 
        default_size: None, dp(56) 
        default_size_hint: 0.8, None
        size_hint_y: None
        height: self.minimum_height 
        orientation: 'vertical' # defines the orientation of data items
"""
Builder.load_string(KV)

class CustomButton(Button):
    root_widget = ObjectProperty()

    def on_release(self, **kwargs):
        super().on_release(**kwargs)
        self.root_widget.btn_callback(self)

class RV(RecycleView):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        self.data = [{'text': str(x), 'root_widget': self} for x in range(100)]

    def btn_callback(self, btn):
        print(btn, btn.text)

class SampleApp(App): 
    def build(self):
        return RV() 

SampleApp().run()