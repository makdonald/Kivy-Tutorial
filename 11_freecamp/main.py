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
from kivy.properties import StringProperty, BooleanProperty, Clock

from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
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

class CanvasExample1(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0,1,0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(500,300,150,100), width=5)
            # create instance of rectangle for move_rect()
            self.rect = Rectangle(pos=(500,100), size=(150,100))

    def move_rect(self):
        print('clicked the button', self.width, self.height)
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)

        diff = self.width - (x+w)
        if diff < inc:
            inc = diff

        x += inc
        y += inc
        self.rect.pos = (x,y)

        # if y < self.height - h and x < self.width - w and y > 0 and x > 0:
        #     x -= inc
        #     y -= inc
            
        #     self.rect.pos = (x, y)
        # else:
        #     print('stop moving because its a boundry of screen')

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(3)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/90)

    def on_size(self, *args):
        print("on size : " + str(self.width) + ", " + str(self.height))
        #self.ball.pos = (self.width/2, self.height/2)
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

    def update(self, dt):
        #print("update")
        x, y = self.ball.pos
        x += self.vx
        y += self.vy

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = - self.vy

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx

        if y < 0:
            y = 0
            self.vy = -self.vy

        if x < 0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x, y)

class CanvasExample6(Widget):
    pass





if __name__ == '__main__':
    myApp().run()
