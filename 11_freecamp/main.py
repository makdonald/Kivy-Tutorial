import os

from kivy.uix.widget import Widget
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty, BooleanProperty
#from kivy.lang import Builder


from kivy.metrics import dp

#kv = Builder.load_file("stylesheet.kv")

class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty('1')
    my_text_input_str = StringProperty("Value")
    #slider_value_text = StringProperty('50')
   
    def on_button_click(self):
        if self.count_enabled == True:
            print('button clicked')
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print('toggle state:',widget.state)
        if widget.state == 'normal':
            widget.text = 'OFF'
            self.count_enabled = False
        else:
            widget.text = 'ON'
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch:", widget.active)

    # def on_slider_value(self, widget):
    #     print("Slider value:", int(widget.value))
        #self.slider_value_text = str(int(widget.value))

    def on_text_validate(self, widget):
        self.my_text_input_str = widget.text


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = 'rl-tb'
        for x in range(100):
            #size = dp(100) + x*10
            size = dp(100)
            b = Button(text=str(x+1), size_hint=(None,None), size=(size,size))
            self.add_widget(b)

# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation ='vertical'
        b1 = Button(text = 'A')
        b2 = Button(text = 'B')
        b3 = Button(text = 'C')
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
'''

class MainWidget(Widget):
    pass

# class MyApp(App):
#     def build(self):
#         return MainWidget()

class myApp(App):
    pass

if __name__ == '__main__':
    myApp().run()
