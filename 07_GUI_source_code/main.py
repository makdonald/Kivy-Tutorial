import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase

# kivy GUI example and walk through the source code. This kivy example 
# is fairly complex and deals with multiple screens. The example is a logi
#  and create account form. You have the ability to create an account, 
# login and see information based on your current user. 

class CreateAccountWindow(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.username.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                # add the user to database
                db.add_user(self.email.text, self.password.text, self.username.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.username.text = ""

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            # set the current user in MainWindow(Screen)
            MainWindow.current = self.email.text
            self.reset()
            # go to main window
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, username, created = db.get_user(self.current)
        self.n.text = "Account Name: " + username
        self.email.text = "Email: " + self.current
        self.created.text = "Createdf On: " + created

# class used to manage Screens and moving things
class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login', content=Label(text='Invalid user name or password.'), size_hint=(None, None), size=(400, 400))

    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='Please fill in all inputs with valid information.'),size_hint=(None, None), size=(400, 400))

    pop.open()


# link .kv file with application
kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name='login'), CreateAccountWindow(name='create'), MainWindow(name='main')]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class MyApp(App):
    def build(self):
        return sm


if __name__== "__main__":
    MyApp().run()





