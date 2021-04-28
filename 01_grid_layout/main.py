import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


# class to hold design elements
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        
        # external layout
        self.cols = 1

        # create internal layout
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.fname = TextInput(multiline=False)
        self.inside.add_widget(self.fname)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lname = TextInput(multiline=False)
        self.inside.add_widget(self.lname)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
        

    # define a function which will be called button clisk
    def pressed(self, instance):
        #print('Pressed')
        fname = self.fname.text
        lname = self.lname.text
        email = self.email.text

        print(f'fname {fname}, lname {lname}, email {email}')
        # clear the box after submission
        self.fname.text = ""
        self.lname.text = ""
        self.email.text = ""


# Alternative with my.kv file which hold styles, variables and trigger functions
class MyGrid(Widget):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def submit_btn(self):
        print("First Name: ", self.first_name.text)
        self.first_name.text = ""