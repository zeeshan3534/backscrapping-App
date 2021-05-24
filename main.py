from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
# from database import DataBase
import requests
import json

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()
firebase_url = "https://kivydb-bc692-default-rtdb.firebaseio.com/"
res = requests.get(url=firebase_url + "Username" + ".json").json()
res1 = requests.get(url=firebase_url + "Password" + ".json").json()
# y = res1.split()
class LoginWindow(Screen):

    email = ObjectProperty(None)
    password = ObjectProperty(None)

    # y = res1.text
    def loginBtn(self):
        global st
        st = 0
        for i in self.email.text:
            if i.isnumeric():
                st = eval(i) + st


        if self.email.text == "" or self.password.text == "":
            invalidForm()


        elif self.email.text not in res[st] or self.password.text not in res1[st]:
            invalidLogin()
        elif self.email.text in res[st] and self.password.text in res1[st]:
            file = open("abc.txt", "w")
            file.seek(0)
            # first_char = file.read(1)
            file.write(f"{self.email.text}:{self.password.text}")
            file.close()
            sm.current = "main"

class MainWindow(Screen):
    # n = ObjectProperty(None)
    def logout(self):
        print("logout is called")
        f = open('abc.txt', 'r+')
        f.truncate(0)
        f.close()
        sm.current = "login"

class WindowManager(ScreenManager):
    pass

mykv = """
<LoginWindow>:
    name: "login"

    email: email
    password:password
    MDFloatLayout:
        MDLabel:
            text:"Login"
            pos_hint: {"center_y":.85}
            font_style:"H3"
            halign:"center"
            theme_text_color :"Custom"
            text_color: 0,0,0,1
        MDLabel:
            text:"SEO HOME"
            pos_hint: {"center_y":.7}
            font_style:"H5"
            halign:"center"
            theme_text_color :"Custom"
            text_color: 0,0,0,1

        MDTextField:
            hint_text: "Enter your Username"
            id: email
            pos_hint: {"center_x": 0.5 , "center_y":0.6}
            current_hint_text_color:0,0,0,1
            size_hint_x: 0.8
        MDTextField:
            hint_text: "Enter your Password"
            id: password
            pos_hint: {"center_x": 0.5 , "center_y":0.45}
            current_hint_text_color:0,0,0,1
            size_hint_x: 0.8
            password:True
            
        MDRaisedButton:
            text:"Log In"
            pos_hint: {"center_x": 0.5 , "center_y":0.3}
            size_hint_x: 0.5
            on_release:root.loginBtn()


<MainWindow>:
    name: "main"
    Screen:

    NavigationLayout:

        ScreenManager:
            id:screen_manager
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "SEO HOME"
                        anchor_title: "center"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation:"vertical"
                padding:'20dp'
                spacing:'10dp'
                MDLabel:
                    text:"   WELCOME"
                    font_style:"Subtitle1"
                    size_hint_y:None
                    height:self.texture_size[1]
                    id:my_label
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon:"logout"
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.logout()
                                    



    

"""
kv = Builder.load_string(mykv)


























sm = WindowManager()
# db = DataBase("users.txt")



class MyMainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        file = open("abc.txt", "r")
        file.seek(0)
        first_char = file.read(1)
        screens = [LoginWindow(name="login"), MainWindow(name="main")]
        for screen in screens:
            sm.add_widget(screen)
        sm.current = "login"
        if first_char != "":
            sm.current = "main"
            file.close()
            return sm
        else:
            return sm
MyMainApp().run()