import kivy
import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from bs4 import BeautifulSoup

class Myclass(GridLayout):
    def __init__(self,**kwargs):
        super(Myclass, self).__init__(**kwargs)

        self.cols = 1
        self.add_widget(Label(text="url:"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.submit = Button(text = "Submit")
        self.submit.bind(on_press = self.script)
        self.add_widget(self.submit)

    def script(self,instance):
        url = self.name.text
        # print(url)
        s = requests.session()
        m = {"url": url,
                "submit": "Submit"
             }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }
        a =s.post("https://demo.atozseotools.com/mozrank-checker/output",m,headers=headers)
        x = a.content
        soup1 = BeautifulSoup(x, 'lxml')
        lst = []
        counter = 0
        for tagb in soup1.find_all("td"):
            if counter <= 5:
                lst.append(tagb.text)
            else:
                pass
        s = requests.session()
        m = {
            "ckwebsite": url,
            "submitter": "Check"
        }
        a = s.post("https://websiteseochecker.com/website-traffic-checker/",m,headers = headers)
        counter = 0
        lst2 = []
        soup2 = BeautifulSoup(a.content, 'lxml')
        for tagb in soup2.find_all("td"):
            if counter <= 5:
                lst2.append(tagb.text)
            else:
                pass
        self.add_widget(Label(text=f"{lst} ,{lst2[1:5]}"))
        # print(lst)
        # print(lst2[1:4])





class Myapp(App):
    def build(self):
        return Myclass()

Myapp().run()