import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')


from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
#from kivy.app import runTouchApp
from kivy.app import App

# # create layout
# layout = GridLayout(cols=1, spacing=10, size_hint_y=None)

# # Make sure the height is such that there is something to scroll.
# layout.bind(minimum_height=layout.setter('height'))

# # create buttons
# for i in range(100):
#     btn = Button(text=str(i), size_hint_y=None, height=40)
#     # add buttons to layout
#     layout.add_widget(btn)

# # create scroll view
# root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))

# # add layout to root
# root.add_widget(layout)

# runTouchApp(root)

class MyApp(App):

    def build(self):

        # create layout
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # create buttons
        for i in range(100):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            # add buttons to layout
            layout.add_widget(btn)

        
        # create scroll view
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))

        # add layout to root
        root.add_widget(layout)

        return root

if __name__ == '__main__':
    MyApp().run()
