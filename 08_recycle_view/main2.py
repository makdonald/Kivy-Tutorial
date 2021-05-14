import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')


import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.boxlayout import BoxLayout


class MyButton(RecycleDataViewBehavior,BoxLayout):
    value = StringProperty()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def add_data(self):
        app = App.get_running_app()
        new_value = len(app.rv_data)
        app.rv_data.append({"value":str(new_value)})


class MyApp(App):
    rv_data = ListProperty()

    def __init__(self, **kwargs):
        mylist = list()
        for i in range(10):
            mylist.append(dict(value=str(i)))
        self.rv_data = mylist
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_string("""
<MyButton>
    orientation: "horizontal"
    Label:
        text: root.value
        color: 0,0,0,1
    Button:
        text: "Press Me"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .5
        on_release: root.add_data()

Screen:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    RecycleView:
        id: rv
        viewclass: "MyButton"
        data: app.rv_data
        RecycleGridLayout:
            cols: 2
            default_size: [0, dp(40)]
            default_size_hint: 1, None
            size_hint_x: 1
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(5)
"""
)

if __name__ == '__main__':
    MyApp().run()